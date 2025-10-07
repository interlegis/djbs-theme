.. djbs-theme documentation master file, created by
   sphinx-quickstart on Thu Mar 27 12:26:29 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to djbs-theme documentation!
====================================

djbs (acronym for DJango BootStrap) is a theme for django-admin based on the 
bootstrap framework. It is an adaptation of the django.contrib.admin app 
templates and the django.forms templates to use bootstrap library, with a 
modern and pleasant look.

These also include template tags and filters that make building your templates 
easier.

Getting Started
===============

You can get djbs-theme by using pip::

 $ pip install djbs-theme

If you want to install it from source, pip directly from git repository::

 $ pip install git+https://github.com/interlegis/djbs-theme.git

For more detailed instructions check out our :doc:`installation_instructions`. 
Enjoy.

Compatibility with versions of Python and Django
=================================================

We follow the Django guidelines for supported Python and Django versions. 
See more at `Django Supported Versions <https://docs.djangoproject.com/en/dev/internals/release-process/#supported-versions>`_

This might mean the djbs-theme may work with older or unsupported versions 
but we do not guarantee it and most likely will not fix bugs related to 
incompatibilities with older versions.

Contents
========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation_instructions
   settings_and_customization
   admin_index
   model_admin_options
   admin_changelist
   menu_system
   template_tags_and_filters
   context_variables

Releases
========


+---------+------------------------------------------------------------------+
| Release | Description                                                      |
+=========+==================================================================+
|  1.0.4  | * Add sphinx documentation                                       |
|         | * Change menu to use icon template tag                           |
|         | * Correct ModelAdmin property names                              |
|         | * update templates                                               |
+---------+------------------------------------------------------------------+
|  1.0.3  | Fix template to use correct `stacked_cols` property name         |
+---------+------------------------------------------------------------------+
|  1.0.2  | Increases the top margin of the submit row to highlight the      |
|         | inlines                                                          |
+---------+------------------------------------------------------------------+
|  1.0.1  | Add the possibility to define the number of data columns in      |
|         | StackedInlines and show or hide `original` column in admin       |
|         | inlines.                                                         |
+---------+------------------------------------------------------------------+
|  1.0.0  | Fisrt stable version                                             |
+---------+------------------------------------------------------------------+

