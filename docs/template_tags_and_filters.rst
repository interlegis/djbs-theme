.. _template_tags_and_filters-label:

Custom template tags and filters
================================

*Djbs-theme* provides some custom template tags and filters that provide useful 
functionality in page rendering. Add a ``{% load djbs_extras %}`` at the 
beginning of your templates to access this set of tags and filters. This 
document describes each *djbs-theme* tag and filter.

Filters
-------

``badgerize``
^^^^^^^^^^^^^

Convert a string with pattern ``"(?P<label>.*) \((?P<count>.*)\)"`` to the 
HTML snippet ``f"<span class='me-auto'>{ label }</span><span class='badge 
text-bg-secondary'>{ count }</span>"``. Used to convert faceted filter labels
(see `Dango admin documentation <https://docs.djangoproject.com/en/5.1/ref/
contrib/admin/#django.contrib.admin.ModelAdmin.show_facets>`__)
to a bootstrap badge layout.

Sample usage:

.. code-block:: django

    {{ choice.display|badgerize }}


``dateisoformat``
^^^^^^^^^^^^^^^^^

Convert a date string in django ``DATE_INPUT_FORMAT`` to a isoformat to be 
used as value in HTML ``<input type="date">``.

Sample usage:

.. code-block:: django

    {% load djbs_extras %}
    <input type="date"
       name="{{ widget.name }}"
       {% if widget.value != None %} value="{{ widget.value|dateisoformat }}"{% endif %}
       {% include "django/forms/widgets/attrs.html" %}
       style="width: max-content;">

``fileimage``
^^^^^^^^^^^^^

Return a image URL representing the file given by `FieldFile`. If the file is
an image file, return the `FieldFile.url` itself, elsewhere return a link to
an static icon image representing the file type.

Sample usage:

.. code-block:: django

    {% load djbs_extras %}
    <img src="{{ widget.value|fileimage }}" alt="{{ widget.value }}" 
    title="{{ widget.value }}">

The static icon images has the name defined by `<file suffix>.jpg` pattern.
These files are located in `<static_root>/img/djbs_icons/`. Djbs-theme come
with icon images for csv, doc, docx, json, odp, ods, odt, pdf, xls, xlsx file
types.

If the file suffix in `FiledFile` has no corresponding static icon image, the
`img/djbs_icons/unknown.jpg` static url is returned.

developers can add another static icon images putting any file with the name in
pattern `<file suffix>.jpg` in a `static/img/djbs_icons` folder in any 
application.

``filename``
^^^^^^^^^^^^

Extract the *name* part from a full-path file string.

Sample usage:

.. code-block:: django

    {{ filepath|filename }}

For example, suppose you have ``"/tmp/mytempfiles/temp001.txt"`` as the value 
of var ``filepath`` in the above code, then the result will be *temp001.txt*

``filesuffix``
^^^^^^^^^^^^^^

Extract the file suffix from a full-path file string.

Sample usage:

.. code-block:: django

    {{ filepath|filename }}

For example, suppose you have ``"/tmp/mytempfiles/temp001.txt"`` as the value 
of var ``filepath`` in the above code, then the result will be *txt*

``valueof``
^^^^^^^^^^^

Given a querystring and a parameter name, returns the value assigned to that 
parameter in the querystring. If the requested parameter does not exist in the 
querystring, returns an empty string.

Sample usage:

.. code-block:: django

        <option value="{{ choice.query_string|valueof:spec.lookup_kwarg|iriencode }}"{% if choice.selected %} selected{% endif %}>{{ choice.display }}</option>

Tags
----

``icon``
^^^^^^^^

Given a icon name, generates a HTML snippet what represents that icon. Extra 
classes can be passed as a string, and also another attributes as named 
parameters.

Sample usage:

.. code-block:: django

    {% icon "theme-dark" "me-2 opacity-50" aria_label="Dark theme color" %}


The above code will generate an HTML snippet for "theme dark" icon, with 
additional classes ``me-2`` and ``opacity-50`` and an ``aria-label`` attribute.

.. note::
    The ``-`` (minus) symbol in the attribute name must be replaced by ``_`` 
    (underscore) in the tag.

``no_filter_params``
^^^^^^^^^^^^^^^^^^^^

Given an admin ChangeList instance, returns a dictionary with all query 
parameters what are not a filter parameter.

Sample usage:

.. code-block:: django
    
    {% no_filter_params cl as nfp %}
    {% for p,v in nfp.items %}
      <input type="hidden" name="{{ p }}" value="{{ v }}">
    {% endfor %}