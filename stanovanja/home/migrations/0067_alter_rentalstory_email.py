# Generated by Django 3.2.22 on 2023-12-14 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0066_storyformpage_thank_you_page"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rentalstory",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="E-mail uporabnika"
            ),
        ),
    ]
