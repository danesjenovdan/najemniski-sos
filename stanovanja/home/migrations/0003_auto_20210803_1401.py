# Generated by Django 3.2.6 on 2021-08-03 12:01

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "section",
                        wagtail.core.blocks.StreamBlock(
                            [
                                (
                                    "color_section",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "color",
                                                wagtail.core.blocks.ChoiceBlock(
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
                                                wagtail.core.blocks.StreamBlock(
                                                    [
                                                        (
                                                            "headline",
                                                            wagtail.core.blocks.StructBlock(
                                                                [
                                                                    (
                                                                        "title",
                                                                        wagtail.core.blocks.CharBlock(
                                                                            label="Naslov"
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "description",
                                                                        wagtail.core.blocks.RichTextBlock(
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
    ]
