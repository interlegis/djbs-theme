# djbs-theme
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/interlegis/djbs-theme/blob/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/interlegis/djbs-theme/blob/main/README.pt-br.md)

Django Admin Bootstrap theme

djbs is a theme for django-admin based on the bootstrap framework. It is an adaptation of the django.contrib.admin app templates and the django.forms templates to use bootstrap components.

## Requirements:

- Python>3.10
- Django>5.1

## External packages (via CDN):

- Bootstrap=5.3

## getting it

You can get djbs-theme by using pip:

```
$ pip install djbs-theme
```

If you want to install it from source, pip directly from git repository:

```
$ pip install git+https://github.com/interlegis/djbs-theme.git
```


## Installing it

To enable `djbs-theme` in your project you need to add `djbs` and `django.forms` to `INSTALLED_APPS` in your project's `settings.py` file, just before the `'django.contrib.admin'` entry:

```python
    INSTALLED_APPS = (
        ...
        'djbs',
        'django.forms',
        'django.contrib.admin',
        ...
    )
```

Set the form renderer to TemplatesSetting, adding the above code:

```python
    FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
```

Add `djbs.context_processors.sets` to the `context_processors` list inside `OPTIONS`:

```python
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "djbs.context_processors.sets",
                ],
            },
        },
    ]
```

## Customizing

To customize the `djbs-theme` you need to add a `DJBSTHEME` dictionary into your projects `settings.py` file.

The default `djbs-theme` settings is:

```python
    DJBSTHEME_DEFAULTS = {
        "SEARCH_URL": None,
        "SEARCH_PARAM": None,
        "MENU_FILE": BASE_DIR / "menu_conf.yaml",
        "CHECK_AS_SWITCH": True,
        "FILTER_STYLE": FILTER_STYLE_CLASSIC,
        "FIELDSET_STYLE": STYLE_CARD,
        "INLINESET_STYLE": STYLE_CARD,
        "BADGERIZE_FACETS": True,
        "ICON_SOURCE": "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
        "ICON_TAG_PATTERN": '<i class="{icon} {classes}" {attrs}></i>',
        "ICONS": {
            "add": "bi bi-plus-square",
            "back": "bi bi-arrow-left-short",
            "check": "bi bi-check2",
            "check-all": "bi bi-check-all",
            "chevron-left": "bi bi-chevron-left",
            "chevron-right": "bi bi-chevron-right",
            "copy": "bi bi-copy",
            "default": "bi bi-wrench-adjustable-circle",
            "delete": "bi bi-trash3",
            "delete_selected": "bi bi-trash3",
            "dismiss": "bi bi-x",
            "edit": "bi bi-pencil-square",
            "forward": "bi bi-chevron-double-right",
            "help": "bi bi-question-circle",
            "hide": "bi bi-eye-slash",
            "history": "bi bi-clock-history",
            "link": "bi bi-link-45deg",
            "list-view": "bi bi-card-list",
            "remove": "bi bi-eraser",
            "rewind": "bi bi-chevron-double-left",
            "save": "bi bi-save",
            "search": "bi bi-search",
            "show": "bi bi-eye",
            "theme-auto": "bi bi-circle-half",
            "theme-light": "bi bi-sun-fill",
            "theme-dark": "bi bi-moon-stars-fill",
            "user": "bi bi-person-fill",
            "viewsite": "bi bi-globe2",
        },
    }
```

You can override any settings. Omitted settings remain the default setting.

## Documentation

The djbs-theme documentation is in development yet.

## Contribute

To set up a development environment (assuming you have an Ubuntu installation with Python3 already installed):

  - Install the venv module:

    ```bash
    $ sudo apt update && sudo apt install python3-venv
    ```

  - Create the project directory:

    ```bash
    $ mkdir djbs-theme && cd djbs-theme
    ```

  - Create a virtualenv in the project:
    
    ```bash
    $ python3 -m venv .venv/djbs-theme
    ```

  - Activate the virtualenv:
    
    ```bash
    $ source .venv/djbs-theme/bin/activate
    ```

  - Install the necessary python packages:
    
    ```bash
    $ pip install pip ipython django pyYaml django-debug-toolbar --upgrade
    ```

  - Create the django-project:

    ```bash
    $ django-admin startproject djbstheme .
    ```

  - Clone this repository into your project:
    
    ```bash
    $ git clone https://github.com/interlegis/djbs-theme.git djbs
    ```

  - Configure the project by changing the application's `settings.py`.

    - Use your preferred text editor to edit the `./djbstheme/settings.py` file.
    - Find the `INSTALLED_APPS` list and add, before the `'django.contrib.admin'` app, the `'djbs'` and `'django.forms'` apps.
    - Add the `FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'` configuration.
    - add `"djbs.context_processors.sets"` to the `context_processors` list inside `OPTIONS`.

That's it! Your project is configured.
