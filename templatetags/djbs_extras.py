import re
import yaml
from pathlib import Path
from urllib.parse import parse_qs
from django import template
from django.contrib.admin.views.main import PAGE_VAR
from django.utils.safestring import mark_safe
from .. import djbst_settings
from ..global_djbs_settings import ADMIN_CHANGEABLES

register = template.Library()


@register.inclusion_tag("menus/menu.html", takes_context=True)
def show_menu(context, menu_id):
    if isinstance(djbst_settings["MENU_FILE"], Path):
        menu_file = djbst_settings["MENU_FILE"]
    else:
        menu_file = Path(djbst_settings["MENU_FILE"])
    if menu_file.exists() and menu_file.is_file():
        menus = yaml.load(menu_file.open(), yaml.FullLoader)
        return {"menu_items": menus[menu_id], "request": context.request}
    return {}


@register.simple_tag
def tool_icon(tool_name, obj=None, classes="", **kwargs):
    if obj is not None:
        action = None
        if hasattr(obj, tool_name):
            action = getattr(obj, tool_name)
        elif hasattr(obj, "model_admin") and hasattr(obj.model_admin, tool_name):
            action = getattr(obj.model_admin, tool_name)
        if hasattr(action, "djbs_icon"):
            icon_name = action.djbs_icon
        else:
            icon_name = tool_name
    if icon_name in djbst_settings["ICONS"]:
        icon_class = djbst_settings["ICONS"][icon_name]
    else:
        icon_class = icon_name
    attrs = " ".join(
        [f"{key.replace('_','-')}='{value}'" for key, value in kwargs.items()]
    )
    return mark_safe(
        djbst_settings["ICON_TAG_PATTERN"].format(
            icon=icon_class, classes=classes, attrs=attrs
        )
    )


@register.simple_tag
def icon(icon_name, classes="", **kwargs):
    attrs = " ".join(
        [f"{key.replace('_','-')}='{value}'" for key, value in kwargs.items()]
    )
    if icon_name not in djbst_settings["ICONS"]:
        icon_name = "default"
    return mark_safe(
        djbst_settings["ICON_TAG_PATTERN"].format(
            icon=djbst_settings["ICONS"][icon_name], classes=classes, attrs=attrs
        )
    )


@register.simple_tag
def get_theme_var(var_name, obj=None):
    return (
        getattr(obj, var_name)
        if hasattr(obj, var_name)
        else djbst_settings[var_name] if var_name in djbst_settings else ""
    )


@register.simple_tag
def page_link(cl, i):
    return cl.get_query_string({PAGE_VAR: i})


@register.filter
@mark_safe
def badgerize(faceted_label):
    if not djbst_settings["BADGERIZE_FACETS"]:
        return faceted_label
    m = re.search("(.*) \((.*)\)", str(faceted_label))
    if m is None:
        return faceted_label
    else:
        label, count = m.groups()
        return (
            f"<span class='me-auto'>{ label }</span>"
            f"<span class='badge text-bg-secondary'>{ count }</span>"
        )


@register.simple_tag
def no_filter_params(cl):
    filters = cl.params.copy()
    for spec in cl.filter_specs:
        if spec.lookup_kwarg in filters:
            del filters[spec.lookup_kwarg]
    # if filters:
    #     return "?" + "&".join(
    #         [urlencode({k: v}) for k, l in filters.items() for v in l]
    #     )
    return filters


@register.filter
def valueof(querystr, param):
    if param in querystr:
        return parse_qs(querystr[1:])[param][0]
    return ""


@register.simple_tag(takes_context=True)
def djbs_admin(context, admin):
    djbs = context.get("djbs")
    if djbs:
        for key in ADMIN_CHANGEABLES:
            if hasattr(admin, key.lower()):
                djbs[key] = getattr(admin, key.lower())
    return ""


