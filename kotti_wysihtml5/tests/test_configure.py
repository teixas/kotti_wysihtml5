from kotti_wysihtml5 import includeme
from kotti_wysihtml5 import kotti_configure


def test_kotti_configure():
    settings = {
        'kotti.includes': '',
        'pyramid_deform.template_search_path': 'foo',
    }

    kotti_configure(settings)

    assert settings['kotti.includes'] == ' kotti_wysihtml5'
    assert settings['pyramid_deform.template_search_path'] == \
        'kotti_wysihtml5:templates/deform foo'


def test_includeme(config):
    includeme(config)
