from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.core import serializers
from django.contrib import messages
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from wagtail.core import blocks, fields
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (StreamFieldPanel, InlinePanel, FieldPanel, MultiFieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
import requests
import json
from .blocks import (SectionBlock)
from .solution import (SolutionCategory, RentalStory, UserProblem)
from ..forms import RentalStoryForm, UserProblemSubmissionForm


class ContentPage(Page):
    body = fields.StreamField(
        [('section', SectionBlock())],
        verbose_name=_('Vsebina'),
        default='',
    )

    modal_title = models.CharField(max_length=255, verbose_name=_('Naslov v modalnem oknu'), blank=True)
    modal_description = models.CharField(max_length=1024, verbose_name=_('Opis v modalnem oknu'), blank=True)
    modal_form_checkbox = models.CharField(max_length=255, verbose_name=_('Forma - prvi checkbox'), blank=True)
    modal_form_checkbox2 = models.CharField(max_length=255, verbose_name=_('Forma - drugi checkbox'), blank=True)
    modal_form_button = models.CharField(max_length=255, verbose_name=_('Forma - tekst na gumbu'), blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('modal_title'),
            FieldPanel('modal_description'),
            FieldPanel('modal_form_checkbox'),
            FieldPanel('modal_form_checkbox2'),
            FieldPanel('modal_form_button'),
        ],
        heading="Modalno okno za novo najemniško zgodbo",
        )

    ]

    def get_context(self, request, rental_story_form=None, user_problem_form=None):

        context = super().get_context(request)

        solutions = SolutionPage.objects.all().live()

        context["categories"] = (
            SolutionCategory.objects.all()
        )

        rental_stories = RentalStory.objects.filter(approved=True, private=False)
        context["rental_stories"] = rental_stories
        rental_stories_stringified = serializers.serialize("json", rental_stories, fields=('lat', 'lng', 'description', 'icon', 'displayed_name'))
        context["rental_stories_stringified"] = rental_stories_stringified

        if request.method == 'GET':
            # filter promises by search query, if there is one in url params
            search_query = request.GET.get("query", None)
            if search_query:
                solutions = solutions.search(
                    search_query,
                    operator="and",
                ).get_queryset()
            categories = request.GET.getlist("category", None)
            print(categories)
            if categories:
                solutions = solutions.filter(category_id__in=categories)
                context["chosen_categories"] = [int(i) for i in categories]

            rental_story_form = RentalStoryForm()
            user_problem_form = UserProblemSubmissionForm()

        context["solutions"] = solutions
        context["rental_story_form"] = rental_story_form
        context["user_problem_form"] = user_problem_form

        return context

    def serve(self, request):

        if request.method == 'GET':
            return TemplateResponse(
                request,
                self.get_template(request),
                self.get_context(request)
            )

        if request.method == 'POST':
            headers = {
                "Authorization": settings.PODPRI_SEND_EMAIL_TOKEN,
                "content-type": "application/json"
            }

            if 'new_story' in request.POST:
                rental_story_form = RentalStoryForm(request.POST)

                if rental_story_form.is_valid():
                    new_rental_story = rental_story_form.save()
                    rental_story_form = RentalStoryForm()
                    messages.add_message(request, messages.SUCCESS, 'Hvala za oddano izkušnjo', extra_tags='story')

                    # send an email to admin
                    payload = {
                        "title": "Nova uporabniška zgodba",
                        "content": f"<html>" \
                            f"<body>" \
                                f"<p><strong>Ime:</strong> {new_rental_story.name}</p>" \
                                f"<p><strong>Naslov:</strong> {new_rental_story.address}</p>" \
                                f"<p><strong>E-naslov:</strong> {new_rental_story.email}</p>" \
                                f"<p><strong>Opis:</strong> {new_rental_story.description}</p>" \
                            f"</body>" \
                        f"</html>",
                        "description": "Najemniški SOS - nova uporabniška zgodba",
                        "segments": [22]
                    }

                    r = requests.post('https://podpri.djnd.si/api/create-and-send-custom-email/', data = json.dumps(payload), headers=headers)
                    print(r.json())

                    return HttpResponseRedirect(request.path)
                else:
                    messages.add_message(request, messages.ERROR, 'Nekaj je šlo narobe :(', extra_tags='story')
                    return TemplateResponse(
                        request,
                        self.get_template(request),
                        self.get_context(request, rental_story_form=rental_story_form, user_problem_form=UserProblemSubmissionForm())
                    )

            if 'new_problem' in request.POST:
                user_problem_form = UserProblemSubmissionForm(request.POST)
                if user_problem_form.is_valid():
                    new_user_problem = user_problem_form.save()
                    user_problem_form = UserProblemSubmissionForm()
                    messages.add_message(request, messages.SUCCESS, 'Hvala za oddan problem!', extra_tags='problem')

                    # send an email to admin
                    payload = {
                        "title": "Nov uporabniški problem",
                        "content": f"<html>" \
                            f"<body>" \
                                f"<p><strong>E-naslov:</strong> {new_user_problem.email}</p>" \
                                f"<p><strong>Opis:</strong> {new_user_problem.description}</p>" \
                            f"</body>" \
                        f"</html>",
                        "description": "Najemniški SOS - nov uporabniški problem",
                        "segments": [22]
                    }

                    r = requests.post('https://podpri.djnd.si/api/create-and-send-custom-email/', data = json.dumps(payload), headers=headers)
                    print(r.json())

                    return HttpResponseRedirect(request.path)
                else:
                    messages.add_message(request, messages.ERROR, 'Nekaj je šlo narobe :(', extra_tags='problem')
                    return TemplateResponse(
                        request,
                        self.get_template(request),
                        self.get_context(request, rental_story_form=RentalStoryForm(), user_problem_form=user_problem_form)
                    )

            return HttpResponseRedirect(request.path)


class SolutionPage(Page):
    body = fields.StreamField(
        [("text", blocks.RichTextBlock(label=_("Obogateno besedilo"),),)],
        null=True,
        blank=True,
        verbose_name=_("Vsebina"),
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Slika'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    claps_no = models.IntegerField(verbose_name=_("Število ploskov"), default=0)
    category = models.ForeignKey(SolutionCategory, null=True, on_delete=models.SET_NULL)
    related_problems = fields.StreamField(
        [('problem', blocks.PageChooserBlock(label=_("Povezava do problema"))),],
        blank=True,
        null=True,
        min_num=0,
        max_num=3,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
        ImageChooserPanel("image"),
        FieldPanel("claps_no"),
        FieldPanel("category", widget=forms.Select),
        StreamFieldPanel("related_problems"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]


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

