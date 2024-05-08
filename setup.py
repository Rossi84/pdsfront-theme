# -*- coding: utf-8 -*-

"""Sphinx CW theme"""

import codecs
import json

from setuptools import setup

package_file = codecs.open('package.json', 'r', 'utf-8')
package_data = json.load(package_file)


setup(
    name = 'pdsfront_theme',
    version = package_data['version'],
    license = package_data['license'],
    author = 'Team per la Trasformazione Digitale - AgID',
    description = __doc__,
    long_description = codecs.open('README.md', 'r', 'utf-8').read(),
    zip_safe = False,
    packages = ['pdsfront_theme', 'pdsfront-theme'],
    package_data = {'pdsfront_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/icons/*.*',
        'static/js/*.js',
        'static/*.png',
        'static/*.svg',
        'static/font/*.*',
        'data/*.*',
    ]},
    include_package_data = True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'pdsfront_theme = pdsfront_theme'
        ]
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation'
    ],
    install_requires = [
        'PyYAML'
    ]
)
