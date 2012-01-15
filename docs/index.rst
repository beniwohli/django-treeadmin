django-treeadmin
================

django-treeadmin is a complement to models that are `django-mptt`_-enabled.
It provides a drag-&-drop interface to modify the tree.

It was originally developed as part of `FeinCMS`_. They deserve all the kudos
for this.

.. _django-mptt: https://github.com/django-mptt/django-mptt
.. _FeinCMS: http://www.feinheit.ch/media/labs/feincms/

Prerequisites
-------------

If you want to use django-treeadmin, make sure that the following points are fulfilled:

 * your project uses ``staticfiles``, either through Django's
   :mod:`django.contrib.staticfiles` (part of Django since 1.3) or
   `django-staticfiles`_.
 * your model uses ``django-mptt``

.. _django-staticfiles: https://github.com/jezdez/django-staticfiles

Usage
-----

To activate the treeadmin, inherit from :class:`treeadmin.admin.TreeAdmin` in
your ``admin.py``::

    from django.contrib import admin
    from treeadmin.admin import TreeAdmin

    from myapp.models import MyModel


    class MyModelAdmin(TreeAdmin):
        pass


    admin.site.register(MyModel, MyModelAdmin)

.. warning::

    If your project uses `johnny-cache`_, make sure to inherit from
    :class:`JohnnyCacheAwareTreeAdmin` instead of
    :class:`~treeadmin.admin.TreeAdmin`. It tries to get around some cache
    invalidation problems that occur when django-mptt is used together with
    johnny-cache.

    If the state of the tree is mission-critical for your project, it's
    probably best to add its table to ``JOHNNY_TABLE_BLACKLIST``. Please
    refer to johnny-cache's documentation for more information.

.. _johnny-cache: http://packages.python.org/johnny-cache/

``TreeAdmin`` Options
---------------------

.. class:: treeadmin.admin.TreeAdmin

The behaviour of the tree admin can be influenced with a couple of class
attributes:

.. attribute:: TreeAdmin.filter_include_ancestors

    Controls if ancestors should be displayed on a filtered list

    By default, it is set to ``False``.

    .. note::

        This corresponds to the ``FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS``
        setting in FeinCMS.

.. attribute:: TreeAdmin.enable_object_permissions

    If set to ``True``, permission checks will be made on the object level.
    Make sure to have an authentication backend that supports object level
    permissions, or weird things will happen.

    By default, it is set to ``False``.

    .. note::

        This corresponds to the ``FEINCMS_TREE_EDITOR_OBJECT_PERMISSIONS``
        setting in FeinCMS.

.. attribute:: TreeAdmin.jquery_use_google_cdn

    If set to ``True``, jQuery and jQuery UI are loaded from Google's CDN.

    By default, it is set to ``False``.

    ..note::

        This corresponds to the ``FEINCMS_ADMIN_MEDIA_HOTLINKING`` setting
        in FeinCMS.

.. attribute:: TreeAdmin.jquery_no_conflict

    If set to ``True``, loads jQuery in the ``noconflict`` mode.

    By default, it is set to ``False``.

    .. note::

        This correspnds to the ``FEINCMS_JQUERY_NO_CONFLICT`` setting in
        FeinCMS.