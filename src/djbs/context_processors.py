from . import get_djbst_settings, djbs_constants


def sets(request):
    return {
        "djbs": get_djbst_settings(),
        "djbsc": djbs_constants,
    }
