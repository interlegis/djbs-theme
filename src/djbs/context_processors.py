from django.conf import settings
from . import djbs_constants
from .global_djbs_settings import DJBSTHEME_DEFAULTS


def sets(request):
    djbs_settings = getattr(settings, "DJBSTHEME", DJBSTHEME_DEFAULTS)
    return {
        "djbs": djbs_settings,
        "djbsc": djbs_constants,
    }
