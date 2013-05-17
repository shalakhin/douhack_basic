import os
from ._base import *
import dj_database_url

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
)

EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_USE_TLS = True

DEBUG = False
