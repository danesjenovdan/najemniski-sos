from django.utils.html import escape
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from wagtail.core import hooks
from wagtail.core.rich_text import LinkHandler

from .models import RentalStory, SolutionCategory, UserProblem


class NewTabExternalLinkHandler(LinkHandler):
    identifier = "external"

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs["href"]
        return '<a href="%s" target="_blank">' % escape(href)


# Run hook with order=1 so it runs after admin is loaded (default order=0) and overrides rules
@hooks.register("register_rich_text_features", order=1)
def register_extra_rich_text_features(features):
    features.register_link_type(NewTabExternalLinkHandler)


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
    items = (RentalStoryAdmin,)


class SolutionGroup(ModelAdminGroup):
    menu_label = "Problemi in rešitve"
    menu_icon = "folder-open-inverse"
    menu_order = 300
    items = (SolutionCategoryAdmin, UserProblemAdmin)


modeladmin_register(StoriesGroup)
modeladmin_register(SolutionGroup)
