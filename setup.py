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
    description='A Django restFul project, with Angular.',
    author='Matthew D. Brown',
    author_email='mattd429@gmail.com',
    maintainer='Matthew D. Brown',
    maintainer_email='mattd429@gmail.com',
    url='https://murmuring-bastion-26669.herokuapp.com/',
    version='0.1dev',
    packages=['django-rest-framework-api',],
    license='MIT',
    long_description=read('README.md'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Framework :: Django',
                 'Framework :: Django :: 1.8',
                 'Framework :: Django :: 1.9',
                 'Framework :: Django :: 1.10',
                 'Framework :: Django :: 1.11',
                 'Framework :: Django :: 2.0',
                 'Framework :: Django :: 2.1',
                 'Framework :: Django :: 2.2',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: Implementation :: CPython',
                 'Programming Language :: Python :: Implementation :: PyPy',
                 'Topic :: Software Development :: Testing',
                 ],
    # the following makes a plugin available to pytest
    # entry_points={'pytest0912': ['django = django-rest-framewrok-api.plugin']}
    )