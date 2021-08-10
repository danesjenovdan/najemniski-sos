# Generated by Django 3.2.6 on 2021-08-09 13:58

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_solutionpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solutionpage',
            name='full_text',
        ),
        migrations.AddField(
            model_name='solutionpage',
            name='body',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock(label='Obogateno besedilo'))], blank=True, null=True, verbose_name='Vsebina'),
        ),
    ]
