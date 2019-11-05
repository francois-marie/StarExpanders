#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# Package meta-data.
NAME = 'StarExpanders'
DESCRIPTION = ''
URL = ''
EMAIL = ''
AUTHOR = ''
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

REQUIRED = [
        'cqc',
        'numpy',
        'scipy',
        'twisted',
        'networkx',
        'flake8',
        'click',
        'daemons'
        'simulaqron'
    ]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
 	packages=find_packages(exclude=('tests')),
	install_requires=REQUIRED,
    zip_safe=False,
    include_package_data=True,
)

