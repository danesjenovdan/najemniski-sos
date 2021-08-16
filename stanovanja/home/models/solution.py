from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from wagtail.admin.edit_handlers import (FieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel


class SolutionCategory(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Ime kategorije"),
    )
    slug = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Ključ (če je prazno se avtomatsko ustvari iz imena)"),
    )
    color = models.CharField(
        max_length=32,
        verbose_name=_(
            "Barva (veljavni vsi css formati, npr. rgb(255, 255, 255), #fff ali #ffffff)"
        ),
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
        FieldPanel("color"),
    ]

    class Meta:
        verbose_name = "Kategorija rešitev"
        verbose_name_plural = "Kategorije rešitev"


class RentalStory(models.Model):
    description = models.TextField(
        verbose_name=_("Besedilo zgodbe"),
    )
    icon = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Ikona"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Ime uporabnika"),
    )
    email = models.EmailField(
        verbose_name=_("E-mail uporabnika"),
    )
    address = models.CharField(
        max_length=255,
        verbose_name=_("Naslov uporabnika"),
    )
    private = models.BooleanField(
        default=False,
        verbose_name=_("Zgodba ni za javno objavo"),
    )
    approved = models.BooleanField(
        default=False,
        verbose_name=_("Pregledano (samo pregledane zgodbe so prikazane na strani)"),
    )
    displayed_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_("Prikazano ime in naslov uporabnika"),
    )

    def __str__(self):
        if (self.approved == True):
            return self.displayed_name
        else:
            return 'ČAKA PREGLED ADMINISTRATORJA'

    panels = [
        FieldPanel("description"),
        ImageChooserPanel("icon"),
        FieldPanel("name"),
        FieldPanel("email"),
        FieldPanel("address"),
        FieldPanel("private"),
        FieldPanel("approved"),
        FieldPanel("displayed_name"),
    ]

    class Meta:
        verbose_name = "Uporabniška zgodbaaaaa"
        verbose_name_plural = "Uporabniške zgodbe"

