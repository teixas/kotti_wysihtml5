import os

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

install_requires = [
    'js.bootstrap_wysihtml5',
    'Kotti',
],

setup(
    name='kotti_wysihtml5',
    version='0.1.1',
    description="wysihtml5 for Kotti",
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: MIT License",
    ],
    author='Nuno Teixeira',
    author_email='teixas@gmail.com',
    url='https://github.com/teixas/kotti_wysihtml5',
    keywords='wysihtml5 bootstrap image browser kotti cms pylons pyramid',
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
      'fanstatic.libraries':
          ['wysihtml5 = kotti_wysihtml5:library', ],
    },
    message_extractors={
        "kotti_wysihtml5": [
            ("**.py", "lingua_python", None),
            ("**.pt", "lingua_xml", None),
        ],
    },
)
