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

DEBUG = True

ALLOWED_HOSTS = ['esportslover.herokuapp.com','127.0.0.1:8000']

django_heroku.settings(locals())