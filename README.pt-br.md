# djbs-theme
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/interlegis/djbs-theme/blob/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/interlegis/djbs-theme/blob/main/README.pt-br.md)

Tema Bootstrap para Django Admin

djbs é um tema para o django-admin baseado no framework Bootstrap. É uma adaptação dos templates do app django.contrib.admin e dos templates do django.forms para utilizar componentes do Bootstrap.

## Requisitos:

- Python>3.10
- Django>5.1

## Pacotes externos (via CDN):

- Bootstrap=5.3

## obtendo-o

Você pode obter o djbs-theme usando pip:

```
$ pip install djbs-theme
```

## Instalando-o

Para habilitar o `djbs-theme` em seu projeto, você precisa adicionar `djbs` e `django.forms` ao `INSTALLED_APPS` no arquivo `settings.py` do seu projeto, logo antes da entrada `'django.contrib.admin'`:

```python
    INSTALLED_APPS = (
        ...
        'djbs',
        'django.forms',
        'django.contrib.admin',
        ...
    )
```

Defina o renderizador de formulários para TemplatesSetting, adicionando o código abaixo:

```python
    FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
```

Adicione `djbs.context_processors.sets` à lista de `context_processors` dentro de `OPTIONS`:

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

## Customizando

Para customizar o `djbs-theme`, você precisa adicionar um dicionário `DJBSTHEME` no arquivo `settings.py` do seu projeto.

As configurações padrão do `djbs-theme` são:

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

Você pode sobrescrever qualquer configuração. Configurações omitidas permanecem com as definições padrão.

## Documentação

A documentação do djbs-theme ainda está em desenvolvimento.

## Contribuir

Para configurar um ambiente de desenvolvimento (assumindo que você tenha uma instalação do Ubuntu com Python3 já instalado):

  - Instale o módulo venv:

    ```bash
    $ sudo apt update && sudo apt install python3-venv
    ```

  - Crie o diretório do projeto:

    ```bash
    $ mkdir djbs-theme && cd djbs-theme
    ```

  - Crie um virtualenv no projeto:
    
    ```bash
    $ python3 -m venv .venv/djbs-theme
    ```

  - Ative o virtualenv:
    
    ```bash
    $ source .venv/djbs-theme/bin/activate
    ```

  - Instale os pacotes python necessários:
    
    ```bash
    $ pip install pip ipython django pyYaml django-debug-toolbar --upgrade
    ```

  - Crie o projeto django:

    ```bash
    $ django-admin startproject djbstheme .
    ```

  - Clone este repositório em seu projeto:
    
    ```bash
    $ git clone https://github.com/interlegis/djbs-theme.git djbs
    ```

  - Configure o projeto alterando o arquivo `settings.py` da aplicação.

    - Use seu editor de texto preferido para editar o arquivo `./djbstheme/settings.py`.
    - Encontre a lista `INSTALLED_APPS` e adicione, antes do app `'django.contrib.admin'`, os apps `'djbs'` e `'django.forms'`.
    - Adicione a configuração `FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'`.
    - Adicione `"djbs.context_processors.sets"` à lista `context_processors` dentro de `OPTIONS`.

É isso! Seu projeto está configurado.