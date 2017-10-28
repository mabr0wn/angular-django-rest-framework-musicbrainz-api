"""
Let's break down what happens in the first module,
first we import absolute imports from the future,
so that our celery.py module won't clash with the library
"""

from __future__ import absolute_import, unicode_literals
# This will make sure the app is always import when
# Django starts so that shared_task decorator will use this app.
from .celery import app as celery_app

__all__ = ['celery_app']
