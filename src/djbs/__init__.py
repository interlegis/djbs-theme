from django.conf import settings
from .global_djbs_settings import DJBSTHEME_DEFAULTS

if hasattr(settings, "DJBSTHEME"):
    for key, value in settings.DJBSTHEME.items():
        if isinstance(value, dict):
            DJBSTHEME_DEFAULTS[key].update(value)
        else:
            DJBSTHEME_DEFAULTS[key] = value

djbst_settings = DJBSTHEME_DEFAULTS
