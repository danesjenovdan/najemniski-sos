from django.utils.html import escape
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from wagtail.core import hooks

from .models import SolutionCategory, RentalStory, UserProblem


class SolutionCategoryAdmin(ModelAdmin):
    model = SolutionCategory
    menu_icon = "group"
    list_display = ("name",)


class RentalStoryAdmin(ModelAdmin):
    model = RentalStory
    menu_icon = "group"
    list_display = ("name", "email", "description", "approved")


class UserProblemAdmin(ModelAdmin):
    model = UserProblem
    menu_icon = "group"
    list_display = ("email", "contact_permission", "description", "approved")


class StoriesGroup(ModelAdminGroup):
    menu_label = "Najemniške izkušnje"
    menu_icon = "folder-open-inverse"
    menu_order = 200
    items = (
        RentalStoryAdmin,
    )


class SolutionGroup(ModelAdminGroup):
    menu_label = "Problemi in rešitve"
    menu_icon = "folder-open-inverse"
    menu_order = 300
    items = (
        SolutionCategoryAdmin,
        UserProblemAdmin
    )


modeladmin_register(StoriesGroup)
modeladmin_register(SolutionGroup)
