from django.db import models

from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel, ObjectList,
                                         StreamFieldPanel, TabbedInterface)

from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from .blocks import (SectionBlock)


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

