from djbs import djbst_settings, djbs_constants


def sets(request):
    return {
        "djbs": djbst_settings,
        "djbsc": djbs_constants,
    }
