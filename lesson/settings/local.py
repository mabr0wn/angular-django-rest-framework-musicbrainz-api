from .base import *

import os

SECRET_KEY = 'DJANGO_SECRET_KEY'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'musicbrainz_db',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
