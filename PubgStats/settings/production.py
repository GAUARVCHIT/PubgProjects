from .base import *
import os
import django_heroku

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'PUBG_DEV_DB',
        'USER': 'postgres',
        'PASSWORD': 'postgres1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = False

ALLOWED_HOSTS = ['esportslover.herokuapp.com']

django_heroku.settings(locals())