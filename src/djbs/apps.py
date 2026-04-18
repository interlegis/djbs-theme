import importlib
import select
from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from .global_djbs_settings import DJBSTHEME_DEFAULTS


class djbsConfig(AppConfig):
    name = "djbs"
    verbose_name = "Django Bootstrap Theme"

    def ready(self):
        user_djbs_settings = getattr(settings, "DJBSTHEME", DJBSTHEME_DEFAULTS)
        if hasattr(settings, "DJBSTHEME"):
            if not isinstance(user_djbs_settings, dict):
                raise ImproperlyConfigured("DJBS_THEME settings must be a dict")
            user_djbs_settings = self._deep_merge(
                user_djbs_settings, DJBSTHEME_DEFAULTS
            )
        setattr(settings, "DJBSTHEME", user_djbs_settings)
        return super().ready()

    def _deep_merge(self, user_dict, default_dict):
        merged_dict = dict()
        for key, default_value in default_dict.items():
            if key in user_dict:
                user_value = user_dict[key]
                if isinstance(default_value, dict):
                    if not isinstance(user_value, dict):
                        raise ImproperlyConfigured(
                            "DJBSTHEME theme setting %s must be a dict" % (key)
                        )
                    user_value = self._deep_merge(user_value, default_value)
            else:
                if isinstance(default_value, dict):
                    user_value = default_value.copy()
                else:
                    user_value = default_value
            merged_dict[key] = user_value
        return merged_dict
