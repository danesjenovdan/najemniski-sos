from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.core import serializers
from django.template.response import TemplateResponse
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (StreamFieldPanel, InlinePanel, FieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from .blocks import (SectionBlock)
from .solution import (SolutionCategory, RentalStory, UserProblem)
from ..forms import RentalStoryForm, UserProblemSubmissionForm


class ContentPage(Page):
    body = StreamField(
        [('section', SectionBlock())],
        verbose_name=_('Vsebina'),
        default='',
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
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
            if 'new_story' in request.POST:
                rental_story_form = RentalStoryForm(request.POST)

                if rental_story_form.is_valid():
                    rental_story_form.save()
                    rental_story_form = RentalStoryForm()
                    """
                    send_mail(
                        'Nova najemniška zgodba',
                        'Forma tekst',
                        None,
                        ['patricija.brecko@gmail.com'],
                        fail_silently=False,
                    )
                    """
                    return HttpResponseRedirect(request.path)
                else:
                    return TemplateResponse(
                        request,
                        self.get_template(request),
                        self.get_context(request, rental_story_form=rental_story_form, user_problem_form=UserProblemSubmissionForm())
                    )

            if 'new_problem' in request.POST:
                user_problem_form = UserProblemSubmissionForm(request.POST)
                if user_problem_form.is_valid():
                    user_problem_form.save()
                    user_problem_form = UserProblemSubmissionForm()
                    return HttpResponseRedirect(request.path)
                else:
                    return TemplateResponse(
                        request,
                        self.get_template(request),
                        self.get_context(request, rental_story_form=RentalStoryForm(), user_problem_form=user_problem_form)
                    )

            return HttpResponseRedirect(request.path)


class SolutionPage(Page):
    body = StreamField(
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
    user_problem = models.ForeignKey(UserProblem, null=True, on_delete=models.SET_NULL, limit_choices_to={'approved': False}, verbose_name=_("Uporabniški problem"))

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
        ImageChooserPanel("image"),
        FieldPanel("claps_no"),
        FieldPanel("category", widget=forms.Select),
        FieldPanel("user_problem", widget=forms.Select), # widget=forms.SelectMultiple
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]
