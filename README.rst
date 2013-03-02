===============
kotti_wysihtml5
===============

wysihtml5 for Kotti.

Setup
=====

To activate the kotti_wysihtml5 add-on in your Kotti site, you need to
add an entry to the ``kotti.configurators`` setting in your Paste
Deploy config.  If you don't have a ``kotti.configurators`` option,
add one.  The line in your ``[app:main]`` section could then look like
this::

  kotti.configurators = kotti_wysihtml5.kotti_configure

With this, you'll be able to use wysihtml5 in your Kotti site.


.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
