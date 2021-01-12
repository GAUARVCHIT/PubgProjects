from .base import *
import os
import django_heroku

SECRET_KEY = os.environ.get('SECRET_KEY')

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

ALLOWED_HOSTS = ['esportslover.herokuapp.com']

django_heroku.settings(locals())