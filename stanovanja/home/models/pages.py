import json

import requests
from django import forms
from django.conf import settings
from django.contrib import messages
from django.core import serializers
from django.core.mail import send_mail
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks, fields
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from ..forms import RentalStoryForm, UserProblemSubmissionForm
from .blocks import NewProblemSection, SectionBlock
from .solution import RentalStory, SolutionCategory, UserProblem


class ContentPage(Page):
    body = fields.StreamField(
        [("section", SectionBlock())],
        verbose_name=_("Vsebina"),
        default="",
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    def get_context(self, request, user_problem_form=None):
        context = super().get_context(request)

        solutions = SolutionPage.objects.all().live().order_by("-first_published_at")

        context["categories"] = SolutionCategory.objects.all()

        rental_stories = RentalStory.objects.filter(
            approved=True, private=False
        ).order_by("?")
        context["rental_stories"] = rental_stories
        rental_stories_stringified = serializers.serialize(
            "json",
            rental_stories,
            fields=("lat", "lng", "description", "icon", "displayed_name"),
        )
        context["rental_stories_stringified"] = rental_stories_stringified

        try:
            context["new_rental_story_page"] = StoryFormPage.objects.first()
        except:
            context["new_rental_story_page"] = None

        if request.method == "GET":
            # filter promises by search query, if there is one in url params
            search_query = request.GET.get("query", None)
            if search_query:
                solutions = solutions.search(
                    search_query,
                    operator="and",
                ).get_queryset()
            categories = request.GET.getlist("category", None)
            if categories:
                solutions = solutions.filter(category_id__in=categories)
                context["chosen_categories"] = [int(i) for i in categories]

            user_problem_form = UserProblemSubmissionForm()

        context["solutions"] = solutions
        context["user_problem_form"] = user_problem_form

        return context

    def serve(self, request):
        if request.method == "GET":
            return TemplateResponse(
                request, self.get_template(request), self.get_context(request)
            )

        if request.method == "POST":
            headers = {
                "Authorization": settings.PODPRI_SEND_EMAIL_TOKEN,
                "content-type": "application/json",
            }

            if "new_problem" in request.POST:
                user_problem_form = UserProblemSubmissionForm(request.POST)

                if user_problem_form.is_valid():
                    new_user_problem = user_problem_form.save()
                    user_problem_form = UserProblemSubmissionForm()
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        "Hvala za oddan problem!",
                        extra_tags="problem",
                    )

                    # send an email to admin
                    payload = {
                        "title": "Nov uporabniški problem",
                        "content": f"<html>"
                        f"<body>"
                        f"<p><strong>E-naslov:</strong> {new_user_problem.email}</p>"
                        f"<p><strong>Opis:</strong> {new_user_problem.description}</p>"
                        f"</body>"
                        f"</html>",
                        "description": "Najemniški SOS - nov uporabniški problem",
                        "segments": [19],
                    }

                    r = requests.post(
                        "https://podpri.lb.djnd.si/api/create-and-send-custom-email/",
                        data=json.dumps(payload),
                        headers=headers,
                    )

                    # send an email to user
                    payload = {
                        "email": new_user_problem.email,
                        "email_template_id": 243,
                    }

                    r = requests.post(
                        "https://podpri.lb.djnd.si/api/send-email/",
                        data=json.dumps(payload),
                        headers=headers,
                    )

                    return HttpResponseRedirect(request.path)
                else:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        "Nekaj je šlo narobe :(",
                        extra_tags="problem",
                    )
                    return TemplateResponse(
                        request,
                        self.get_template(request),
                        self.get_context(
                            request,
                            user_problem_form=user_problem_form,
                        ),
                    )

            return HttpResponseRedirect(request.path)


class SolutionPage(Page):
    body = fields.StreamField(
        [
            (
                "text",
                blocks.RichTextBlock(
                    label=_("Obogateno besedilo"),
                ),
            )
        ],
        null=True,
        blank=True,
        verbose_name=_("Vsebina"),
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Slika"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    claps_no = models.IntegerField(verbose_name=_("Število ploskov"), default=0)
    category = models.ForeignKey(
        SolutionCategory,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Kategorija"),
    )
    related_problems = fields.StreamField(
        [
            ("problem", blocks.PageChooserBlock(label=_("Povezava do problema"))),
        ],
        blank=True,
        null=True,
        min_num=0,
        max_num=3,
        verbose_name=_("Povezani problemi"),
    )
    new_problem_section = fields.StreamField(
        [
            (
                "section",
                blocks.StructBlock(
                    [
                        ("new_problem", NewProblemSection()),
                        (
                            "background_color",
                            blocks.ChoiceBlock(
                                choices=[
                                    ("white", "Bela"),
                                    ("yellow", "Rumena"),
                                    ("purple", "Vijolična"),
                                    ("gradient_green_yellow", "Zeleno-rumena"),
                                    ("gradient_purple_green", "Vijolično-zelena"),
                                ],
                                default="white",
                                label=_("Barva"),
                            ),
                        ),
                    ],
                    label=_("Sekcija"),
                ),
            ),
        ],
        null=True,
        blank=True,
        max_num=1,
        verbose_name=_("Sekcija za oddat nov problem"),
    )
    meta_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
        ImageChooserPanel("image"),
        FieldPanel("claps_no"),
        FieldPanel("category", widget=forms.Select),
        StreamFieldPanel("related_problems"),
        StreamFieldPanel("new_problem_section"),
        ImageChooserPanel("meta_image"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]

    def get_context(self, request, user_problem_form=None):
        context = super().get_context(request)

        if request.method == "GET":
            user_problem_form = UserProblemSubmissionForm()

        context["user_problem_form"] = user_problem_form
        return context

    def serve(self, request):
        if request.method == "GET":
            return TemplateResponse(
                request, self.get_template(request), self.get_context(request)
            )

        if request.method == "POST":
            headers = {
                "Authorization": settings.PODPRI_SEND_EMAIL_TOKEN,
                "content-type": "application/json",
            }
            user_problem_form = UserProblemSubmissionForm(request.POST)
            if user_problem_form.is_valid():
                new_user_problem = user_problem_form.save()
                user_problem_form = UserProblemSubmissionForm()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Hvala za oddan problem!",
                    extra_tags="problem",
                )

                # send an email to admin
                payload = {
                    "title": "Nov uporabniški problem",
                    "content": f"<html>"
                    f"<body>"
                    f"<p><strong>E-naslov:</strong> {new_user_problem.email}</p>"
                    f"<p><strong>Opis:</strong> {new_user_problem.description}</p>"
                    f"</body>"
                    f"</html>",
                    "description": "Najemniški SOS - nov uporabniški problem",
                    "segments": [19],
                }
                r = requests.post(
                    "https://podpri.lb.djnd.si/api/create-and-send-custom-email/",
                    data=json.dumps(payload),
                    headers=headers,
                )

                # send an email to user
                payload = {"email": new_user_problem.email, "email_template_id": 243}
                r = requests.post(
                    "https://podpri.lb.djnd.si/api/send-email/",
                    data=json.dumps(payload),
                    headers=headers,
                )

                return HttpResponseRedirect(request.path)
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "Nekaj je šlo narobe :(",
                    extra_tags="problem",
                )
                return TemplateResponse(
                    request,
                    self.get_template(request),
                    self.get_context(request, user_problem_form=user_problem_form),
                )

        return HttpResponseRedirect(request.path)


class NewsletterPage(Page):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Opis"),
    )
    body = fields.StreamField(
        [("rich_text", blocks.RichTextBlock())],
        null=True,
        blank=True,
        verbose_name=_("Vsebina"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Urejanje naročnine"
        verbose_name_plural = "Urejanja naročnin"


class StoryFormPage(Page):
    intro_text = RichTextField(
        null=True,
        blank=True,
        verbose_name=_("Besedilo pred obrazcem"),
    )
    discrimination_text = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Navodilo za opis diskriminacije"),
    )
    rental_story_text = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Navodilo za najemniške izkušnje"),
    )
    thank_you_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro_text"),
        FieldPanel("discrimination_text"),
        FieldPanel("rental_story_text"),
        FieldPanel("thank_you_page"),
    ]

    def get_context(self, request, rental_story_form=None):
        context = super().get_context(request)
        if request.method == "GET":
            rental_story_form = RentalStoryForm()
            context["rental_story_form"] = rental_story_form
        return context

    def serve(self, request):
        if request.method == "GET":
            return TemplateResponse(
                request, self.get_template(request), self.get_context(request)
            )

        if request.method == "POST":
            headers = {
                "Authorization": settings.PODPRI_SEND_EMAIL_TOKEN,
                "content-type": "application/json",
            }

            rental_story_form = RentalStoryForm(request.POST)

            if rental_story_form.is_valid():
                new_rental_story = rental_story_form.save()
                rental_story_form = RentalStoryForm()

                # send an email to admin
                payload = {
                    "title": "Nova uporabniška zgodba",
                    "content": f"<html>"
                    f"<body>"
                    f"<p><strong>Ime:</strong> {new_rental_story.name}</p>"
                    f"<p><strong>Naslov:</strong> {new_rental_story.address}</p>"
                    f"<p><strong>E-naslov:</strong> {new_rental_story.email}</p>"
                    f"<p><strong>Opis:</strong> {new_rental_story.description}</p>"
                    f"</body>"
                    f"</html>",
                    "description": "Najemniški SOS - nova uporabniška zgodba",
                    "segments": [19],
                }

                r = requests.post(
                    "https://podpri.lb.djnd.si/api/create-and-send-custom-email/",
                    data=json.dumps(payload),
                    headers=headers,
                )

                # send an email to user
                payload = {
                    "email": new_rental_story.email,
                    "email_template_id": 244,
                }

                r = requests.post(
                    "https://podpri.lb.djnd.si/api/send-email/",
                    data=json.dumps(payload),
                    headers=headers,
                )

                if self.thank_you_page:
                    return HttpResponseRedirect(self.thank_you_page.get_url())
                else:
                    return HttpResponseRedirect("/")
            else:
                return TemplateResponse(
                    request,
                    self.get_template(request),
                    self.get_context(
                        request,
                        rental_story_form=rental_story_form,
                    ),
                )

    class Meta:
        verbose_name = "Oddaja najemniške izkušnje"
        verbose_name_plural = "Oddaja najemniške izkušnje"
