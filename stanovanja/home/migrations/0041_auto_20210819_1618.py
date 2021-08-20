# Generated by Django 3.2.6 on 2021-08-19 14:18

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_alter_contentpage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='modal_description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Opis v modalnem oknu'),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='modal_form_button',
            field=models.CharField(blank=True, max_length=255, verbose_name='Forma - tekst na gumbu'),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='modal_form_checkbox',
            field=models.CharField(blank=True, max_length=255, verbose_name='Forma - prvi checkbox'),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='modal_form_checkbox2',
            field=models.CharField(blank=True, max_length=255, verbose_name='Forma - drugi checkbox'),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='modal_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Naslov v modalnem oknu'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StreamBlock([('color_section', wagtail.core.blocks.StructBlock([('color', wagtail.core.blocks.ChoiceBlock(choices=[('white', 'Bela'), ('yellow', 'Rumena'), ('purple', 'Vijolična'), ('gradient_green_yellow', 'Zeleno-rumena'), ('gradient_purple_green', 'Vijolično-zelena')], label='Barva')), ('body', wagtail.core.blocks.StreamBlock([('headline', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('title_position', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Sredinska'), ('start', 'Leva')], label='Poravnava naslova')), ('description', wagtail.core.blocks.RichTextBlock(label='Opis', required=False)), ('image_left', wagtail.images.blocks.ImageChooserBlock(label='Slika na levi', required=False)), ('image_right', wagtail.images.blocks.ImageChooserBlock(label='Slika na desni', required=False)), ('buttons', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('underlined', 'Samo podčrtan'), ('normal', 'Z obrobo'), ('background', 'Z obrobo in ozadjem')], label='Stil gumba')), ('arrow', wagtail.core.blocks.BooleanBlock(default=False, label='Gumb s puščico', required=False)), ('text', wagtail.core.blocks.CharBlock(label='Besedilo na gumbu')), ('page', wagtail.core.blocks.PageChooserBlock(label='Stran'))], label='Gumb'))], label='Gumbi', required=False))], icon='title', label='Naslov (večji)', template='home/blocks/headline.html')), ('headline_small', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('title_position', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Sredinska'), ('start', 'Leva')], label='Poravnava naslova')), ('description', wagtail.core.blocks.RichTextBlock(label='Opis', required=False)), ('image_left', wagtail.images.blocks.ImageChooserBlock(label='Slika na levi', required=False)), ('image_right', wagtail.images.blocks.ImageChooserBlock(label='Slika na desni', required=False)), ('buttons', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('underlined', 'Samo podčrtan'), ('normal', 'Z obrobo'), ('background', 'Z obrobo in ozadjem')], label='Stil gumba')), ('arrow', wagtail.core.blocks.BooleanBlock(default=False, label='Gumb s puščico', required=False)), ('text', wagtail.core.blocks.CharBlock(label='Besedilo na gumbu')), ('page', wagtail.core.blocks.PageChooserBlock(label='Stran'))], label='Gumb'))], label='Gumbi', required=False))], icon='title', label='Naslov (manjši)', template='home/blocks/headline_small.html')), ('newsletter', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.RichTextBlock(label='Opis', required=False)), ('image_right', wagtail.images.blocks.ImageChooserBlock(label='Slika na desni', required=False)), ('submit_button', wagtail.core.blocks.CharBlock(label='Besedilo na gumbu')), ('checkbox_text', wagtail.core.blocks.CharBlock(label='Tekst ob checkboxu'))], icon='title', label='Obvestilnik', template='home/blocks/newsletter.html')), ('share_and_care', wagtail.core.blocks.StructBlock([('left_box', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.RichTextBlock(label='Opis', required=False))], label='Leva škatla')), ('right_box', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.RichTextBlock(label='Opis', required=False))], label='Desna škatla'))], icon='title', label='Deli naprej', template='home/blocks/share_and_care.html')), ('frequent_questions', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.RichTextBlock(label='Opis', required=False)), ('button1', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Besedilo na gumbu')), ('page', wagtail.core.blocks.PageChooserBlock(label='Stran'))], label='Prvi gumb')), ('button2', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Besedilo na gumbu')), ('page', wagtail.core.blocks.PageChooserBlock(label='Stran'))], label='Drugi gumb')), ('button3', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Besedilo na gumbu')), ('page', wagtail.core.blocks.PageChooserBlock(label='Stran'))], label='Tretji gumb')), ('button4', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Besedilo na gumbu')), ('page', wagtail.core.blocks.PageChooserBlock(label='Stran'))], label='Četrti gumb')), ('button_redirect', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Besedilo na gumbu')), ('page', wagtail.core.blocks.PageChooserBlock(label='Stran'))], label='Gumb za preusmeritev'))], icon='title', label='Pogosta vprašanja', template='home/blocks/frequent_questions.html')), ('image_section', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.RichTextBlock(label='Opis', required=False)), ('buttons', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('underlined', 'Samo podčrtan'), ('normal', 'Z obrobo'), ('background', 'Z obrobo in ozadjem')], label='Stil gumba')), ('arrow', wagtail.core.blocks.BooleanBlock(default=False, label='Gumb s puščico', required=False)), ('text', wagtail.core.blocks.CharBlock(label='Besedilo na gumbu')), ('page', wagtail.core.blocks.PageChooserBlock(label='Stran'))], label='Gumb'))], label='Gumbi', required=False)), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('image', 'Slika'), ('map', 'Zemljevid')], label='Slika ali zemljevid?')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Slika', required=False))], icon='title', label='Sekcija s sliko ali zemljevidom', template='home/blocks/image_section.html')), ('solutions_list', wagtail.core.blocks.StructBlock([('filter_categories_label', wagtail.core.blocks.CharBlock(label='Navodilo za filtriranje po kategorijah')), ('search_input_label', wagtail.core.blocks.CharBlock(label='Navodilo za iskanje')), ('search_input_placeholder', wagtail.core.blocks.CharBlock(label='Placeholder za iskalno polje'))], icon='title', label='Seznam rešitev', template='home/blocks/solutions_list_section.html')), ('rental_stories_list', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(label='Besedilo na gumbu'))], icon='title', label='Seznam uporabniških zgodb', template='home/blocks/stories_list_section.html')), ('new_problem_form', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.RichTextBlock(label='Opis', required=False)), ('problem_input_placeholder', wagtail.core.blocks.CharBlock(label='Placeholder za opis problema')), ('email_input_placeholder', wagtail.core.blocks.CharBlock(label='Placeholder za email')), ('checkbox_text', wagtail.core.blocks.CharBlock(label='Tekst ob checkboxu')), ('submit_button', wagtail.core.blocks.CharBlock(label='Tekst na gumbu'))], icon='title', label='Forma za oddat nov problem', template='home/blocks/new_problem_section.html')), ('new_story_form', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Naslov')), ('description', wagtail.core.blocks.RichTextBlock(label='Opis', required=False)), ('image_left', wagtail.images.blocks.ImageChooserBlock(label='Slika na levi', required=False)), ('image_right', wagtail.images.blocks.ImageChooserBlock(label='Slika na desni', required=False)), ('submit_button', wagtail.core.blocks.CharBlock(label='Tekst na gumbu za prikaz forme'))], icon='title', label='Sekcija za oddat novo najemniško zgodbo', template='home/blocks/new_story_section.html'))]))]))]))], default='', verbose_name='Vsebina'),
        ),
    ]
