from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from wagtail.admin.edit_handlers import (FieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey


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


class UserProblem(models.Model):
    description = models.TextField(
        verbose_name=_("Besedilo zgodbe"),
    )
    email = models.EmailField(
        verbose_name=_("E-mail"),
    )
    contact_permission = models.BooleanField(
        default=False,
        verbose_name=_("Lahko me kontaktirate"),
    )
    approved = models.BooleanField(
        default=False,
        verbose_name=_("Pregledano s strani administratorja (samo pregledane zgodbe so prikazane na strani)"),
    )

    panels = [
        FieldPanel("description"),
        FieldPanel("email"),
        FieldPanel("contact_permission"),
        FieldPanel("approved"),
    ]

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Oddan problem"
        verbose_name_plural = "Oddani problemi"


class RentalStory(models.Model):
    description = models.TextField(
        verbose_name=_("Besedilo zgodbe"),
    )
    icon = models.CharField(
        null=True,
        blank=True,
        max_length=24,
        verbose_name=_("Ikona"),
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
        verbose_name=_("Pregledano s strani administratorja (samo pregledane zgodbe so prikazane na strani)"),
    )
    displayed_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_("Prikazano ime in naslov uporabnika"),
    )
    lat = models.DecimalField(
         null=True,
         blank=True,
         max_digits=10,
         decimal_places=7,
         verbose_name=_("Zemljepisna širina"),
    )
    lng = models.DecimalField(
         null=True,
         blank=True,
         max_digits=10,
         decimal_places=7,
         verbose_name=_("Zemljepisna dolžina"),
    )

    def __str__(self):
        return self.description

    panels = [
        FieldPanel("description"),
        FieldPanel("icon"),
        FieldPanel("name"),
        FieldPanel("email"),
        FieldPanel("address"),
        FieldPanel("private"),
        FieldPanel("approved"),
        FieldPanel("displayed_name"),
        FieldPanel("lat"),
        FieldPanel("lng"),
    ]

    class Meta:
        verbose_name = "Najemniška izkušnja"
        verbose_name_plural = "Najemniške izkušnje"

