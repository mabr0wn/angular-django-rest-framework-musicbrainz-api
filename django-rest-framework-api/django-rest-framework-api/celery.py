from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django, settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-rest-framework-api.settings.base')

from django.conf import settings

# Pointing to the instance of the library
app = Celery('django-rest-framework-api')

"""
Using a string here means worker doesn't have to serialize
the configuration object to child processes.
 - namespace='Celery' means all celery-related configurations keys
should have a 'CELERY_' prefix.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
"""
# Load task modules from all register information.
app.autodiscover_tasks()

# Will dump its own request information.
@app.task(bind=True)
def debug_true(self):
    print('Request: {0!r}'.format(self.request))
