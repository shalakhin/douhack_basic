import os
from ._base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DOUHACK_DB_NAME', ''),
        'USER': os.getenv('DOUHACK_DB_USER', ''),
        'PASSWORD': os.getenv('DOUHACK_DB_PASSWORD', ''),
        'HOST': os.getenv('DOUHACK_DB_HOST', ''),
        'PORT': os.getenv('DOUHACK_DB_PORT', ''),
    }
}
