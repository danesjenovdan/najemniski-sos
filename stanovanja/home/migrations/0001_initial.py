# -*- coding: utf-8 -*-
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0040_page_draft_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        on_delete=models.CASCADE,
                        parent_link=True,
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="ContentPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "section",
                                wagtail.blocks.StreamBlock(
                                    [
                                        (
                                            "color_section",
                                            wagtail.blocks.StructBlock(
                                                [
                                                    (
                                                        "color",
                                                        wagtail.blocks.ChoiceBlock(
                                                            choices=[
                                                                ("white", "Bela"),
                                                                ("yellow", "Rumena"),
                                                                ("purple", "Vijolična"),
                                                                (
                                                                    "gradientGreenYellow",
                                                                    "Gradient zelena - rumena",
                                                                ),
                                                                (
                                                                    "gradientPurpleGreen",
                                                                    "Gradient vijolična - zelena",
                                                                ),
                                                            ],
                                                            label="Barva",
                                                        ),
                                                    ),
                                                    (
                                                        "body",
                                                        wagtail.blocks.StreamBlock(
                                                            [
                                                                (
                                                                    "headline",
                                                                    wagtail.blocks.StructBlock(
                                                                        [
                                                                            (
                                                                                "title",
                                                                                wagtail.blocks.CharBlock(
                                                                                    label="Naslov"
                                                                                ),
                                                                            ),
                                                                            (
                                                                                "description",
                                                                                wagtail.blocks.RichTextBlock(
                                                                                    label="Opis",
                                                                                    required=False,
                                                                                ),
                                                                            ),
                                                                            (
                                                                                "image_left",
                                                                                wagtail.images.blocks.ImageChooserBlock(
                                                                                    label="Slika na levi",
                                                                                    required=False,
                                                                                ),
                                                                            ),
                                                                            (
                                                                                "image_right",
                                                                                wagtail.images.blocks.ImageChooserBlock(
                                                                                    label="Slika na desni",
                                                                                    required=False,
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        icon="title",
                                                                        label="Naslov",
                                                                        template="home/blocks/headline.html",
                                                                    ),
                                                                )
                                                            ]
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                        default="",
                        verbose_name="Vsebina",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
