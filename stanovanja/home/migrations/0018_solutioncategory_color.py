# Generated by Django 3.2.6 on 2021-08-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0017_auto_20210811_0944"),
    ]

    operations = [
        migrations.AddField(
            model_name="solutioncategory",
            name="color",
            field=models.CharField(
                default="#FFF",
                max_length=32,
                verbose_name="Barva (veljavni vsi css formati, npr. rgb(255, 255, 255), #fff ali #ffffff)",
            ),
            preserve_default=False,
        ),
    ]
