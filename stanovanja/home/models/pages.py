from django.db import models
from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from .blocks import (SectionBlock)
from wagtail.admin.edit_handlers import (StreamFieldPanel, FieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from django.utils.translation import gettext_lazy as _


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

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
        ImageChooserPanel("image"),
    ]
