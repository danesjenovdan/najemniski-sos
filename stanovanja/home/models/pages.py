from django.db import models
from django import forms
from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (StreamFieldPanel, FieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from django.utils.translation import gettext_lazy as _
from .blocks import (SectionBlock)
from .solution import (SolutionCategory, RentalStory)
from ..forms import RentalStoryForm


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

        context["solutions"] = (
            SolutionPage.objects.all().live()
        ) # TO DO: PAGINATION!
        context["categories"] = (
            SolutionCategory.objects.all()
        )
        context["rental_stories"] = (
            RentalStory.objects.filter(approved=True, private=False)
        )

        if request.method == 'POST':
            rental_story_form = RentalStoryForm(request.POST)
            if rental_story_form.is_valid():
                rental_story_form.save()
                rental_story_form = RentalStoryForm()
        else:
            rental_story_form = RentalStoryForm()

        context["rental_story_form"] = rental_story_form

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

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
        ImageChooserPanel("image"),
        FieldPanel("claps_no"),
        FieldPanel("category", widget=forms.Select),
    ]
