# Generated by Django 3.2.22 on 2023-12-14 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("home", "0065_alter_contentpage_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="storyformpage",
            name="thank_you_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
    ]
