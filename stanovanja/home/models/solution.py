from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from wagtail.admin.edit_handlers import (FieldPanel)


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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Kategorija rešitev"
        verbose_name_plural = "Kategorije rešitev"
