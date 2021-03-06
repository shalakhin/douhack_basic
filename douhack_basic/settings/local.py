import os
from ._base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'douhack_basic',
        'USER': 'os',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SOUTH_TESTS_MIGRATE = False
SOUTH_DATABASE_ADAPTER = 'south.db.psycopg2'
SKIP_SOUTH_TESTS = True

EMAIL_HOST = os.environ['MAILTRAP_HOST']
EMAIL_HOST_USER = os.environ['MAILTRAP_USER_NAME']
EMAIL_HOST_PASSWORD = os.environ['MAILTRAP_PASSWORD']
EMAIL_PORT = os.environ['MAILTRAP_PORT']
EMAIL_USE_TLS = False

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)
