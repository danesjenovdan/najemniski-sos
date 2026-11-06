from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import (
    FieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import StreamField

from .blocks import ExternalLinkBlock, PageLinkBlock


@register_setting(icon="cog")
class MetaSettings(BaseSiteSetting):
    header_links = StreamField(
        [
            ("page_link", PageLinkBlock()),
            ("external_link", ExternalLinkBlock()),
        ],
        verbose_name=_("Povezave v glavi"),
    )
    footer_links = StreamField(
        [
            ("page_link", PageLinkBlock()),
            ("external_link", ExternalLinkBlock()),
        ],
        verbose_name=_("Povezave v nogi"),
    )

    link_tab_panels = [
        FieldPanel("header_links"),
        FieldPanel("footer_links"),
    ]

    facebook = models.URLField(
        null=True,
        blank=True,
    )
    twitter = models.URLField(
        null=True,
        blank=True,
    )
    instagram = models.URLField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )

    social_tab_panels = [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("instagram"),
        FieldPanel("email"),
    ]

    meta_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    meta_description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    meta_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    share_email_text = models.TextField(
        null=True,
        blank=True,
    )
    share_twitter_text = models.TextField(
        null=True,
        blank=True,
    )

    meta_tab_panels = [
        FieldPanel("meta_title"),
        FieldPanel("meta_description"),
        FieldPanel("meta_image"),
        FieldPanel("share_email_text"),
        FieldPanel("share_twitter_text"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(link_tab_panels, heading="Seznam povezav"),
            ObjectList(social_tab_panels, heading="Socialna omrežja"),
            ObjectList(meta_tab_panels, heading="Meta opisi"),
        ]
    )

    class Meta:
        verbose_name = "Meta nastavitve"
