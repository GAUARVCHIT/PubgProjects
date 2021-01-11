from .base import *
import os
import django_heroku

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['esportslover.herokuapp.com']

django_heroku.settings(locals())