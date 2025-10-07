.. _menu-system-label:

Menu system
===========

:synopsis: Defining a custom menu

The djbs-theme includes a simplified built-in menu system that works through 
the use of the *show_menu* template tag 
(see :ref:`template_tags_and_filters-label`).

Menu structure file
-------------------

The information needed to build the menu should be provided in a YAML file 
referenced by the ``MENU_FILE`` in :ref:`setting-variable-label` 
(default: ``BASE_DIR / "menu_conf.yaml"``).

Multiple menus can be defined. Each menu must have an ID and one or more 
options, or menu items. The best way to explain the menu_conf.yaml file is 
with an example:

.. code-block:: yaml

    admin_menu:
      - title: Superuser settings
        icon: bi bi-gear
        children:
          - title: User list
            icon: bi bi-person-circle
            view_name: admin:auth_user_changelist
          - title: User groups
            icon: bi bi-people-fill
            view_name: admin:auth_group_changelist
    main_menu:
      - title: Reports
        icon: bi bi-bar-chart
        view_name: reports:dashboard
    anonymous_menu:
      - title: Login
        icon: bi bi-box-arrow-in-right
        view_name: admin:login


Three menus are defined here: ``admin_menu``, ``main_menu`` and 
``anonymous_menu``. The ``admin_menu`` has only one option (Superuser 
settings), with its sub-options (children): User list and User groups. The 
other two menus has a similar structure.

Menu item definition
--------------------

Each menu item can contain the following fields:

* ``title``: the actual title of the menu item.
* ``icon`` (optional): The class of the icon that should appear along with 
  the option title. If omitted, the default icon (gear) will be shown.
* ``view_name``: a system view name that can be resolved by the ``url`` 
  template tag, or
* ``external_url``: an external URL to the system.
* ``querystr`` (optional): a query-string that should be added to the target 
  url of the menu option.
* ``children`` (optional): a list of sub-options that will be shown for that 
  menu item.

If both ``view_name`` and ``external_url`` are specified for the same menu 
item, preference will be given to the url obtained from ``view_name``.


Sidenav menu template
---------------------

By default, *djbs-theme* displays a menu named ``admin_menu`` for logged-in 
users who are superusers, a menu named ``main_menu`` for users who are staff 
members, and a menu named ``anonymous_menu`` for anonymous users.

You can modify this behavior by overwriting the 
``djbs/menus/sidenav_menu.html`` template and defining the display rules you 
want. This template renders the menus and is defined like this:

.. code-block:: django 

  {% load static djbs_extras %} 
  <ul class="navbar-nav flex-column mt-4"> 
    {% if user.is_superuser %} 
      {% show_menu "admin_menu" %} 
    {% endif %} 
    {% if user.is_staff %} 
      {% show_menu "main_menu" %} 
    {% endif %} 
    {% if user.is_anonymous %} 
      {% show_menu "anonymous_menu" %} 
    {% endif %} 
  </ul>