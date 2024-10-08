# Generated by Django 3.2.6 on 2021-08-16 08:25

import wagtail.core.blocks
import wagtail.core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0029_alter_solutionpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="solutionpage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "text",
                        wagtail.core.blocks.RichTextBlock(label="Obogateno besedilo"),
                    )
                ],
                blank=True,
                null=True,
                verbose_name="Vsebina",
            ),
        ),
    ]
