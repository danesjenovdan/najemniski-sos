from django.utils.translation import gettext_lazy as _
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class ContentBlock(blocks.StreamBlock):
    headline = blocks.StructBlock(
        [
            ('title', blocks.CharBlock(label=_('Naslov'))),
            ('description', blocks.RichTextBlock(required=False, label=_('Opis'))),
            ('image_left', ImageChooserBlock(required=False, label=_('Slika na levi'))),
            ('image_right', ImageChooserBlock(required=False, label=_('Slika na desni'))),
        ],
        label=_('Naslov'),
        template='home/blocks/headline.html',
        icon='title',
    )

    class Meta:
        label = _('Vsebina')
        icon = 'snippet'


class ColorSectionBlock(blocks.StructBlock):
    color = blocks.ChoiceBlock(
        choices=[
            ('white', 'Bela'),
            ('yellow', 'Rumena'),
            ('purple', 'Vijolična'),
            ('gradientGreenYellow', 'Gradient zelena - rumena'),
            ('gradientPurpleGreen', 'Gradient vijolična - zelena'),
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


