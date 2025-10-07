Installation instructions
=========================

:synopsis: Installing djbs-theme

Installing
----------

You can use pip to install djbs-theme for usage::

  $ pip install djbs-theme

Development
-----------

Djbs-theme is hosted on github::

 https://github.com/interlegis/djbs-theme/

Source code can be accessed by performing a Git clone.

Tracking the development version of *django bootstrap theme* should be
pretty stable and will keep you up-to-date with the latest fixes.

  $ pip install -e git+https://github.com/interlegis/djbs-theme.git#egg=djbs-theme

You find the sources in src/djbs-theme now.

You can verify that the application is available on your PYTHONPATH by opening 
a python interpreter and entering the following commands:

::

  >>> import djbs
  >>> djbs.VERSION
  (1, 0, 0, 'DEV')

Keep in mind that the current code in the git repository may be different from 
the packaged release. It may contain bugs and backwards-incompatible changes 
but most likely also new goodies to play with.


Configuration
-------------

To enable `djbs-theme` in your project you need to add `djbs` and 
`django.forms` to `INSTALLED_APPS` in your project's `settings.py` file, just 
before the `'django.contrib.admin'` entry:

.. code-block:: python
   
   INSTALLED_APPS = (
      ...
      'djbs',
      'django.forms',
      'django.contrib.admin',
      ...
   )

Set the form renderer to TemplatesSetting, adding the above code:

.. code-block:: python

   FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

Add `djbs.context_processors.sets` to the `context_processors` list 
inside `OPTIONS`:

.. code-block:: python

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

The next time you run your project and access the admin app, voila! it will 
already have the new theme!