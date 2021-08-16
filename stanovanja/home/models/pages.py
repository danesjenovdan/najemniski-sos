from django.db import models
from django import forms
from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (StreamFieldPanel, InlinePanel, FieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from django.utils.translation import gettext_lazy as _
from wagtail.search import index
from .blocks import (SectionBlock)
from .solution import (SolutionCategory, RentalStory, UserProblem)
from ..forms import RentalStoryForm, UserProblemSubmissionForm


class HomePage(Page):
    body = StreamField(
        [('section', SectionBlock())],
        verbose_name=_('Vsebina'),
        default='',
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class ContentPage(Page):
    body = StreamField(
        [('section', SectionBlock())],
        verbose_name=_('Vsebina'),
        default='',
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        all_solutions = SolutionPage.objects.all().live()
        context["categories"] = (
            SolutionCategory.objects.all()
        )
        context["rental_stories"] = (
            RentalStory.objects.filter(approved=True, private=False)
        )

        if request.method == 'GET':
            # filter promises by search query, if there is one in url params
            search_query = request.GET.get("query", None)
            if search_query:
                all_solutions = all_solutions.search(
                    search_query,
                    operator="and",
                ).get_queryset()
            categories = request.GET.getlist("category", None)
            print(categories)
            if categories:
                all_solutions = all_solutions.filter(category_id__in=categories)
                context["chosen_categories"] = [int(i) for i in categories]

            rental_story_form = RentalStoryForm()
            user_problem_form = UserProblemSubmissionForm()

        if request.method == 'POST':
            rental_story_form = RentalStoryForm(request.POST)
            user_problem_form = UserProblemSubmissionForm(request.POST)

            print(request)

            if rental_story_form.is_valid():
                rental_story_form.save()
                rental_story_form = RentalStoryForm()

            if user_problem_form.is_valid():
                user_problem_form.save()
                user_problem_form = UserProblemSubmissionForm()

        context["solutions"] = all_solutions
        context["rental_story_form"] = rental_story_form
        context["user_problem_form"] = user_problem_form

        return context


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
