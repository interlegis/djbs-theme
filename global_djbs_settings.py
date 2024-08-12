from pathlib import Path
from djbs.djbs_constants import *

BASE_DIR = Path(__file__).resolve().parent.parent

DJBSTHEME_DEFAULTS = {
    "SEARCH_URL": None,
    "SEARCH_PARAM": None,
    "MENU_FILE": BASE_DIR / "menu_conf.yaml",
    "CHECK_AS_SWITCH": True,
    "FILTER_STYLE": FILTER_STYLE_CLASSIC,
    "FIELDSET_STYLE": STYLE_CARD,
    "INLINESET_STYLE": STYLE_CARD,
    "BADGERIZE_FACETS": True,
    "TOOL_ICONS": {
        "add": "bi bi-plus-square",
        "default": "bi bi-wrench-adjustable-circle",
        "delete_selected": "bi bi-trash3",
        "history": "bi bi-clock-history",
        "viewsite": "bi bi-globe2",
    },
}
