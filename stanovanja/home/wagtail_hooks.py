from django.utils.html import escape
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from wagtail.core import hooks

from .models import SolutionCategory, RentalStory


class SolutionCategoryAdmin(ModelAdmin):
    model = SolutionCategory
    menu_icon = "group"
    list_display = ("name",)


class RentalStoryAdmin(ModelAdmin):
    model = RentalStory
    menu_icon = "group"
    list_display = ("name",)


class SolutionGroup(ModelAdminGroup):
    menu_label = "Rešitve"
    menu_icon = "folder-open-inverse"
    menu_order = 200
    items = (
        SolutionCategoryAdmin,
        RentalStoryAdmin,
    )


modeladmin_register(SolutionGroup)
