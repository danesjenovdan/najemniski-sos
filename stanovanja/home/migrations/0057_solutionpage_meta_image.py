# Generated by Django 3.2.6 on 2021-10-19 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0056_auto_20210830_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutionpage',
            name='meta_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
