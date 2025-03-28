VERSION = (1, 0, 0, "DEV")


def get_version(version):
    """Dynamically calculate the version based on VERSION tuple."""
    if len(version) > 2 and version[2] is not None:
        if len(version) == 4:
            str_version = "%s.%s.%s.%s" % version
        elif isinstance(version[2], int):
            str_version = "%s.%s.%s" % version[:3]
        else:
            str_version = "%s.%s_%s" % version[:3]
    else:
        str_version = "%s.%s" % version[:2]

    return str_version


__version__ = get_version(VERSION)


def get_djbst_settings():
    from django.conf import settings
    from .global_djbs_settings import DJBSTHEME_DEFAULTS

    if hasattr(settings, "DJBSTHEME"):
        for key, value in settings.DJBSTHEME.items():
            if isinstance(value, dict):
                DJBSTHEME_DEFAULTS[key].update(value)
            else:
                DJBSTHEME_DEFAULTS[key] = value
    return DJBSTHEME_DEFAULTS
