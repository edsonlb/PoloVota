# This Python file uses the following encoding: utf-8
"""
Arquivo Settings.py
"""

import os
import sys
from dj_database_url import parse as db_url
from decouple import config
from unipath import Path

if sys.argv[1] == 'runserver':
    from settings_secret import * #SEE SETTINGS_SECRET_EXAMPLE.PY (RENAME THE FILE TO: settings_secret.py )

BASE_DIR = Path(__file__).parent

AUTH_USER_MODEL = 'persons.Person'

EMAIL_HOST = 'HEROKU_SECRET_EMAIL_HOST'

EMAIL_HOST_USER = 'HEROKU_SECRET_EMAIL_HOST_USER'

EMAIL_HOST_PASSWORD = 'HEROKU_SECRET_EMAIL_HOST_PASSWORD'

DEFAULT_FROM_EMAIL = 'HEROKU_SECRET_DEFAULT_FROM_EMAIL'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

HOST_WWW = 'http://polovota.herokuapp.com/'
#HOST_WWW = 'http://127.0.0.1:8000/'

SECRET_KEY = HEROKU_SECRET_KEY_SETTINGS

DEBUG = (sys.argv[1] == 'runserver')

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'polovota.urls'

WSGI_APPLICATION = 'polovota.wsgi.application'

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR.child('staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
    )

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'persons',
    'projects',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': config(
    'DATABASE_URL',
    default='sqlite:///'+BASE_DIR.child('db.sqlite3'),
    cast=db_url),
}


