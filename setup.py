#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os

from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()

setup(
    name='angular-django-rest-framework-musicbrainz-api',
    version='0.1dev',
    packages=['django-rest-framework-api',],
    license='License :: MIT License',
    long_description=read('README.md'),
)