# Generated by Django 3.2.6 on 2021-08-25 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0051_auto_20210824_1555"),
    ]

    operations = [
        migrations.AddField(
            model_name="solutionpage",
            name="new_problem_form",
            field=models.BooleanField(default=False),
        ),
    ]
