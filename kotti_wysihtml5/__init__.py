# -*- coding: utf-8 -*-

from fanstatic import Library

library = Library('kotti_wysihtml5', 'static')


def kotti_configure(settings):
    settings['kotti.includes'] += ' kotti_wysihtml5'
    settings['pyramid_deform.template_search_path'] = (
        'kotti_wysihtml5:templates/deform ' +
        settings['pyramid_deform.template_search_path'])


def includeme(config):
    config.scan("kotti_wysihtml5")
