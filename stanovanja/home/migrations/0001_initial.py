# -*- coding: utf-8 -*-
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(on_delete=models.CASCADE, parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StreamBlock([('color_section', wagtail.core.blocks.StructBlock([('color', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'Bela'), ('yellow', 'Rumena'), ('purple', 'Vijolična'), ('gradientGreenYellow', 'Gradient zelena - rumena'), ('gradientPurpleGreen', 'Gradient vijolična - zelena')], label='Barva')), ('body', wagtail.core.blocks.StreamBlock([('headline', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.RichTextBlock(label='Opis', required=False)), ('image_left', wagtail.images.blocks.ImageChooserBlock(label='Slika na levi', required=False)), ('image_right', wagtail.images.blocks.ImageChooserBlock(label='Slika na desni', required=False))], icon='title', label='Naslov', template='home/blocks/headline.html'))]))]))]))], default='', verbose_name='Vsebina')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
