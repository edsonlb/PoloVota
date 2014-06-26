# This Python file uses the following encoding: utf-8
"""
File Settings.py
"""

import os
import sys
from dj_database_url import parse as db_url
from decouple import config
from unipath import Path

if 'HEROKU_SECRET_EMAIL_HOST' in os.environ:
    # READ: https://devcenter.heroku.com/articles/config-vars RUNS REMOTE ON HEROKU
    EMAIL_HOST = os.environ['HEROKU_SECRET_EMAIL_HOST']
    EMAIL_HOST_USER = os.environ['HEROKU_SECRET_EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['HEROKU_SECRET_EMAIL_HOST_PASSWORD']
    DEFAULT_FROM_EMAIL = os.environ['HEROKU_SECRET_DEFAULT_FROM_EMAIL']
    SECRET_KEY = os.environ['HEROKU_SECRET_KEY_SETTINGS']
    HOST_WWW = 'http://polovota.herokuapp.com/'
    DEBUG = False
else:
    # SEE SETTINGS_SECRET_EXAMPLE.PY (RENAME THE FILE TO: settings_secret.py ) RUNS LOCALHOST
    from settings_secret import * 
    EMAIL_HOST = SECRET_EMAIL_HOST
    EMAIL_HOST_USER = SECRET_EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD = SECRET_EMAIL_HOST_PASSWORD
    DEFAULT_FROM_EMAIL = SECRET_DEFAULT_FROM_EMAIL
    SECRET_KEY = SECRET_KEY_SETTINGS
    HOST_WWW = 'http://127.0.0.1:8000/'
    DEBUG = True


BASE_DIR = Path(__file__).parent

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

AUTH_USER_MODEL = 'persons.Person'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

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

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
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


