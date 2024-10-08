# Generated by Django 3.2.6 on 2021-08-16 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0030_alter_solutionpage_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProblem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(verbose_name="Besedilo zgodbe")),
                ("email", models.EmailField(max_length=254, verbose_name="E-mail")),
                (
                    "contact_permission",
                    models.BooleanField(
                        default=False, verbose_name="Lahko me kontaktirate"
                    ),
                ),
            ],
            options={
                "verbose_name": "Oddan problem",
                "verbose_name_plural": "Oddani problemi",
            },
        ),
        migrations.AlterModelOptions(
            name="rentalstory",
            options={
                "verbose_name": "Uporabniška zgodba",
                "verbose_name_plural": "Uporabniške zgodbe",
            },
        ),
    ]
