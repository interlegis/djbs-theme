.. _context-variables-label:

Context variables
=================

:synopsis: variables injected into template context


Djbs-theme has a context processor `djbs.context_processors.sets` that injects
two variables into the context of templates. These variables are:

djbs
----

This is a dictionary with all djbs theme settings 
(see :ref:`setting-variable-label`) updated with the `settings.py` 
customizations.

``djbs`` are accessed in admin and widget templates to check the developer 
preferences about theme look and fill and behavior.

djbsc
-----

Contains the djbs-theme constants. Used to avoid dirty comparisions like 
``if filter_style == "accordion"``, replacing them by more assertive 
``if filter_style == djbsc.FILTER_STYLE_ACCORDION`` style.

The following constants are present in ``djbsc`` variable:

.. code-block:: python

    FILTER_STYLE_ACCORDION = "accordion"
    FILTER_STYLE_CLASSIC = "classic"
    FILTER_STYLE_DROPDOWN = "dropdown"
    FILTER_STYLE_FORM = "form"

    STYLE_CARD = "card"
    STYLE_ACCORDION = "accordion"
    STYLE_TAB = "tab"
