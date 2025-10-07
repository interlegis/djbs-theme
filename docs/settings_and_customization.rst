Settings and customization
==========================

:synopsis: Setting up and customizing djbs-theme

.. _setting-variable-label:

Setting djbs-theme variable
---------------------------

djbs-theme has a set of configuration variables that can be changed to modify 
the theme's operation globally.

To customize djbs-theme, add the ``DJBSTHEME`` variable to the project's 
settings.py file, which should be a dictionary with the settings you want to 
change.

The default djbs-theme settings are as follows:

.. code-block:: python

    DJBSTHEME = {
        "SEARCH_URL": None,
        "SEARCH_PARAM": None,
        "MENU_FILE": BASE_DIR / "menu_conf.yaml",
        "CHECK_AS_SWITCH": True,
        "FILTER_STYLE": FILTER_STYLE_CLASSIC,
        "FIELDSET_STYLE": STYLE_CARD,
        "INLINESET_STYLE": STYLE_CARD,
        "BADGERIZE_FACETS": True,
        "STACKED_COLS": 2,
        "HIDE_ORIGINAL": False,
        "ICON_SOURCE": "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
        "ICON_TAG_PATTERN": '<i class="{icon} {classes}" {attrs}></i>',
        "ICONS": {
          "add": "bi bi-plus-square",
          "alert": "bi bi-exclamation-circle",
          "back": "bi bi-arrow-left-short",
          "check": "bi bi-check2",
          "check-all": "bi bi-check-all",
          "chevron-left": "bi bi-chevron-left",
          "chevron-right": "bi bi-chevron-right",
          "config": "bi bi-gear",
          "copy": "bi bi-copy",
          "csv": "bi bi-filetype-csv",
          "default": "bi bi-wrench-adjustable-circle",
          "delete": "bi bi-trash3",
          "delete_selected": "bi bi-trash3",
          "dismiss": "bi bi-x",
          "doc": "bi bi-file-earmark-word",
          "docx": "bi bi-file-earmark-word",
          "edit": "bi bi-pencil-square",
          "error": "bi bi-x-circle",
          "export": "bi bi-arrow-down-circle",
          "export_admin_action": "bi bi-arrow-down-circle",
          "export-all": "bi bi-arrow-down-circle-fill",
          "filter": "bi bi-filter-circle",
          "forward": "bi bi-chevron-double-right",
          "help": "bi bi-question-circle",
          "hide": "bi bi-eye-slash",
          "history": "bi bi-clock-history",
          "import": "bi bi-cloud-download",
          "info": "bi bi-info-circle",
          "link": "bi bi-link-45deg",
          "list-view": "bi bi-card-list",
          "login": "bi bi-box-arrow-left",
          "logout": "bi bi-box-arrow-in-right",
          "map": "bi bi-globe-americas",
          "map-location": "bi bi-geo-alt",
          "map-cross": "bi bi-crosshair",
          "pdf": "bi bi-filetype-pdf",
          "play": "bi bi-play-circle",
          "print": "bi bi-printer",
          "remove": "bi bi-eraser",
          "report": "bi bi-printer",
          "rewind": "bi bi-chevron-double-left",
          "save": "bi bi-save",
          "search": "bi bi-search",
          "show": "bi bi-eye",
          "theme-auto": "bi bi-circle-half",
          "theme-light": "bi bi-sun-fill",
          "theme-dark": "bi bi-moon-stars-fill",
          "user": "bi bi-person-fill",
          "viewsite": "bi bi-globe2",
          "xls": "bi bi-file-earmark-excel",
          "xlsx": "bi bi-file-earmark-excel",
          "xml": "bi bi-filetype-xml",
        },
    }

``SEARCH_URL``
^^^^^^^^^^^^^^

Default: ``None``

A url name that responds to the general search of the site (see `Django 
documentation <https://docs.djangoproject.com/en/dev/ref/templates/builtins/#url>`_).
If ``None`` the search form will not be shown.

``SEARCH_PARAM``

^^^^^^^^^^^^^^^^

Default: ``None``

The name of the parameter in which the search function expects to receive the 
searched text.

``MENU_FILE``
^^^^^^^^^^^^^

Default: ``BASE_DIR / "menu_conf.yaml"``

The full path of the YAML file that contains the menu description. See 
:ref:`menu-system-label`

``CHECK_AS_SWITCH``
^^^^^^^^^^^^^^^^^^^

Default: ``True``

defines whether checkboxes should be shown as switches. See `Bootstrap 
documentation. <https://getbootstrap.com/docs/5.3/forms/checks-radios/#switches>`_

``FILTER_STYLE``
^^^^^^^^^^^^^^^^

Default: ``djbs_constants.FILTER_STYLE_CLASSIC``

Defines the style of the changelist filters. The options are:

* ``djbs_constants.FILTER_STYLE_ACCORDION``: Filters are accordion panels and
  their options are checkboxes,
* ``djbs_constants.FILTER_STYLE_CLASSIC``: Classic Django style with just 
  bootstrap added,
* ``djbs_constants.FILTER_STYLE_DROPDOWN``: Each filter is a dropdown menu,
* ``djbs_constants.FILTER_STYLE_FORM``: Uses an HTML form where each filter is
  a select field. Filters are applied only when the submit button is clicked.

``FIELDSET_STYLE``
^^^^^^^^^^^^^^^^^^

Default: ``djbs_constants.STYLE_CARD``

Defines the style of the changeform fieldsets. The options are:

* ``djbs_constants.STYLE_CARD``: each fieldset are displayed as a card,
* ``djbs_constants.STYLE_ACCORDION``: Uses bootstrap accordeon for fieldsets,
* ``djbs_constants.STYLE_TAB``: Uses bootstrap tabs for fieldsets.


``INLINESET_STYLE``
^^^^^^^^^^^^^^^^^^^

Default: ``djbs_constants.STYLE_CARD``

Defines the style of the changeform inlines. The options are:

* ``djbs_constants.STYLE_CARD``: each fieldset are displayed as a card,
* ``djbs_constants.STYLE_ACCORDION``: Uses bootstrap accordeon for fieldsets,
* ``djbs_constants.STYLE_TAB``: Uses bootstrap tabs for fieldsets.

``BADGERIZE_FACETS``
^^^^^^^^^^^^^^^^^^^^

Default: ``True``

Defines whether the Django filter facets will be displayed as badges. See 
`Bootstrap documentation. <https://getbootstrap.com/docs/5.3/components/badge/>`__

``STACKED_COLS``
^^^^^^^^^^^^^^^^

Default: (int) 2

Defines the number of data columns to `admin.StackedInline` admin inlines.

``HIDE_ORIGINAL``
^^^^^^^^^^^^^^^^^

Default: (bool) False

defines whether the `original` column in ``admin.TabularInline`` should be
hidden or shown.


``ICON_SOURCE``
^^^^^^^^^^^^^^^

Default: ``https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css``

The icon fonts stylesheet URL that will be added to HEAD on each HTML page.

``ICON_TAG_PATTERN``
^^^^^^^^^^^^^^^^^^^^

Default: ``"<i class="{icon} {classes}" {attrs}></i>"``

The F-string pattern for composing icon tags. It must contain the following 
placeholders:

* ``{icon}``: will be replaced by the class that identifies the icon,
* ``{classes}``: additional classes for icon tags,
* ``{attrs}``: Any other HTML attributes that will be inserted into the icon tags.

``ICONS``
^^^^^^^^^

A dictionary where the key defines the name of the icon and the value defines 
its class.
