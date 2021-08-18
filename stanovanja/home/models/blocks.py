from django.utils.translation import gettext_lazy as _
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


class ExternalLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(label=_('Ime'))
    url = blocks.URLBlock(label=_('Povezava'))

    class Meta:
        label = _('Zunanja povezava')
        icon = 'link'


class PageLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=False, label=_('Ime'), help_text=_('Če je prazno se uporabi naslov strani.'))
    page = blocks.PageChooserBlock(label=_('Stran'))

    class Meta:
        label = _('Povezava do strani')
        icon = 'link'


class ButtonsBlock(blocks.StreamBlock):
    button = blocks.StructBlock(
    [
        ('style', blocks.ChoiceBlock(
          choices = [
              ('underlined', 'Samo podčrtan'),
              ('normal', 'Z obrobo'),
              ('background', 'Z obrobo in ozadjem')
          ],
          label=_('Stil gumba'),
        )),
        ('arrow', blocks.BooleanBlock(default=False, label=_('Gumb s puščico'), required=False)),
        ('text', blocks.CharBlock(label=_('Besedilo na gumbu'))),
        ('page', blocks.PageChooserBlock(label=_('Stran'))),
    ],
    label=_('Gumb'),)

    class Meta:
        label = _('Gumbi')
        icon = 'snippet'


class ContentBlock(blocks.StreamBlock):
    headline = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('title_position', blocks.ChoiceBlock(
                choices = [
                    ('center', 'Sredinska'),
                    ('start', 'Leva')
                ],
                label=_('Poravnava naslova'),
            )),
            ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
            ('image_left', ImageChooserBlock(required=False, label=_('Slika na levi'))),
            ('image_right', ImageChooserBlock(required=False, label=_('Slika na desni'))),
            ('buttons', ButtonsBlock(required=False, label=_('Gumbi'))),
        ],
        label=_('Naslov (večji)'),
        template='home/blocks/headline.html',
        icon='title',
    )
    headline_small = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('title_position', blocks.ChoiceBlock(
                choices = [
                    ('center', 'Sredinska'),
                    ('start', 'Leva')
                ],
                label=_('Poravnava naslova'),
            )),
            ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
            ('image_left', ImageChooserBlock(required=False, label=_('Slika na levi'))),
            ('image_right', ImageChooserBlock(required=False, label=_('Slika na desni'))),
            ('buttons', ButtonsBlock(required=False, label=_('Gumbi'))),
        ],
        label=_('Naslov (manjši)'),
        template='home/blocks/headline_small.html',
        icon='title',
    )
    newsletter = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
            ('image_right', ImageChooserBlock(required=False, label=_('Slika na desni'))),
            ('submit_button', blocks.CharBlock(label=_('Besedilo na gumbu'))),
            ('checkbox_text', blocks.CharBlock(label=_('Tekst ob checkboxu'))),
        ],
        label=_('Obvestilnik'),
        template='home/blocks/newsletter.html',
        icon='title',
    )
    share_and_care = blocks.StructBlock(
        [
            ('left_box', blocks.StructBlock(
                [
                  ('title', blocks.CharBlock(label=_('Naslov'))),
                  ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
                ],
                label=_('Leva škatla'),
            )),
            ('right_box', blocks.StructBlock(
                [
                    ('title', blocks.CharBlock(label=_('Naslov'))),
                    ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
                ],
                label=_('Desna škatla'),
            )),
        ],
        label=_('Deli naprej'),
        template='home/blocks/share_and_care.html',
        icon='title',
    )
    frequent_questions = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
            ('button1', blocks.StructBlock(
                [
                    ('text', blocks.CharBlock(label=_('Besedilo na gumbu'))),
                    ('page', blocks.PageChooserBlock(label=_('Stran'))),
                ],
                label=_('Prvi gumb'),
            )),
            ('button2', blocks.StructBlock(
                [
                    ('text', blocks.CharBlock(label=_('Besedilo na gumbu'))),
                    ('page', blocks.PageChooserBlock(label=_('Stran'))),
                ],
                label=_('Drugi gumb'),
            )),
            ('button3', blocks.StructBlock(
                [
                    ('text', blocks.CharBlock(label=_('Besedilo na gumbu'))),
                    ('page', blocks.PageChooserBlock(label=_('Stran'))),
                ],
                label=_('Tretji gumb'),
            )),
            ('button4', blocks.StructBlock(
                [
                    ('text', blocks.CharBlock(label=_('Besedilo na gumbu'))),
                    ('page', blocks.PageChooserBlock(label=_('Stran'))),
                ],
                label=_('Četrti gumb'),
            )),
            ('button_redirect', blocks.StructBlock(
                [
                    ('text', blocks.CharBlock(label=_('Besedilo na gumbu'))),
                    ('page', blocks.PageChooserBlock(label=_('Stran'))),
                ],
                label=_('Gumb za preusmeritev'),
            )),
        ],
        label=_('Pogosta vprašanja'),
        template='home/blocks/frequent_questions.html',
        icon='title',
    )
    image_section = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
            ('buttons', ButtonsBlock(required=False, label=_('Gumbi'))),
            ('display', blocks.ChoiceBlock(
                choices=[
                    ('image', 'Slika'),
                    ('map', 'Zemljevid'),
                ],
                label=_('Slika ali zemljevid?'),
            )),
            ('image', ImageChooserBlock(required=False, label=_('Slika'))),
        ],
        label=_('Sekcija s sliko ali zemljevidom'),
        template='home/blocks/image_section.html',
        icon='title',
    )
    solutions_list = blocks.StructBlock(
        [
            ('filter_categories_label', blocks.CharBlock(label=_('Navodilo za filtriranje po kategorijah'))),
            ('search_input_label', blocks.CharBlock(label=_('Navodilo za iskanje'))),
            ('search_input_placeholder', blocks.CharBlock(label=_('Placeholder za iskalno polje'))),
        ],
        label=_('Seznam rešitev'),
        template='home/blocks/solutions_list_section.html',
        icon='title',
    )
    rental_stories_list = blocks.StructBlock(
        [
            ('button_text', blocks.CharBlock(label=_('Besedilo na gumbu'))),
        ],
        label=_('Seznam uporabniških zgodb'),
        template='home/blocks/stories_list_section.html',
        icon='title',
    )
    new_problem_form = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
            ('problem_input_placeholder', blocks.CharBlock(label=_('Placeholder za opis problema'))),
            ('email_input_placeholder', blocks.CharBlock(label=_('Placeholder za email'))),
            ('checkbox_text', blocks.CharBlock(label=_('Tekst ob checkboxu'))),
            ('submit_button', blocks.CharBlock(label=_('Tekst na gumbu'))),
        ],
        label=_('Forma za oddat nov problem'),
        template='home/blocks/new_problem_section.html',
        icon='title',
    )
    new_story_form = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
            ('image_left', ImageChooserBlock(required=False, label=_('Slika na levi'))),
            ('image_right', ImageChooserBlock(required=False, label=_('Slika na desni'))),
            ('submit_button', blocks.CharBlock(label=_('Tekst na gumbu za prikaz forme'))),
            ('modal_title', blocks.CharBlock(label=_('Naslov v modalnem oknu'))),
            ('modal_description', blocks.CharBlock(label=_('Opis v modalnem oknu'))),
            ('modal_form_checkbox1', blocks.CharBlock(label=_('Forma - prvi checkbox'))),
            ('modal_form_checkbox2', blocks.CharBlock(label=_('Forma - drugi checkbox'))),
            ('modal_form_button', blocks.CharBlock(label=_('Forma - tekst na gumbu'))),

        ],
        label=_('Sekcija za oddat novo najemniško zgodbo'),
        template='home/blocks/new_story_section.html',
        icon='title',
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        return context

    class Meta:
        label = _('Vsebina')
        icon = 'snippet'


class ColorSectionBlock(blocks.StructBlock):
    color = blocks.ChoiceBlock(
        choices=[
            ('white', 'Bela'),
            ('yellow', 'Rumena'),
            ('purple', 'Vijolična'),
            ('gradient_green_yellow', 'Zeleno-rumena'),
            ('gradient_purple_green', 'Vijolično-zelena'),
        ],
        label=_('Barva'),
    )
    body = ContentBlock()

    class Meta:
        label = _('Vsebinski odsek z barvo')
        template = 'home/blocks/color_section.html'
        icon = 'snippet'


class SectionBlock(blocks.StreamBlock):
    color_section = ColorSectionBlock()

    class Meta:
        label = _('Vsebinski odsek')
        template = 'home/blocks/section.html'
        icon = 'snippet'


