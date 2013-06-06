# -*- coding: utf-8 -*-

from fanstatic import Library
from fanstatic import Resource

from js.bootstrap_wysihtml5 import bootstrap_wysihtml5

library = Library('kotti_wysihtml5', 'static')
kotti_wysihtml5 = Resource(library,
                           'kotti_wysihtml5.js',
                           depends=[bootstrap_wysihtml5, ])


def kotti_configure(settings):
    settings['kotti.includes'] += ' kotti_wysihtml5'
    settings['pyramid_deform.template_search_path'] = (
        'kotti_wysihtml5:templates/deform ' +
        settings['pyramid_deform.template_search_path'])


def includeme(config):
    config.scan("kotti_wysihtml5")
    try:
        # kotti >= 0.8
        from js.deform import resource_mapping
        edit_needed = resource_mapping['tinymce'] = \
            [kotti_wysihtml5, ]
    except ImportError:  # pragma: no cover
        # kotti < 0.8
        from kotti.static import edit_needed
        edit_needed.add(kotti_wysihtml5)
