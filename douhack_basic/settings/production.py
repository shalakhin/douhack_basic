from ._base import *

import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
)

DEBUG = False
