from pathlib import Path
from djbs.djbs_constants import *

BASE_DIR = Path(__file__).resolve().parent.parent

DJBSTHEME_DEFAULTS = {
    "MENU_FILE": BASE_DIR / "menu_conf.yaml",
    "CHECK_AS_SWITCH": True,
    "FILTER_STYLE": FILTER_STYLE_FORM,
    "FIELDSET_STYLE": STYLE_TAB,
    "INLINESET_STYLE": STYLE_TAB,
    "BADGERIZE_FACETS": True,
    "TOOL_ICONS": {
        "add": "bi bi-plus-square",
        "default": "bi bi-wrench-adjustable-circle",
        "delete_selected": "bi bi-trash3",
        "history": "bi bi-clock-history",
        "viewsite": "bi bi-globe2",
    },
}
