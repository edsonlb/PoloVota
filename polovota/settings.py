# This Python file uses the following encoding: utf-8
"""
Arquivo Settings.py Padrao
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from dj_database_url import parse as db_url
from decouple import config
from unipath import Path
from settings_secret import *

BASE_DIR = Path(__file__).parent

#User = Person
AUTH_USER_MODEL = 'persons.Person'

#Email Configuration
EMAIL_HOST = SECRET_EMAIL_HOST
EMAIL_HOST_USER = SECRET_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = SECRET_EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = SECRET_DEFAULT_FROM_EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#HOST_WWW = 'http://polovota.herokuapp.com/'
HOST_WWW = 'http://127.0.0.1:8000/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY_SETTINGS

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

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

ROOT_URLCONF = 'polovota.urls'

WSGI_APPLICATION = 'polovota.wsgi.application'

DATABASES = {
    'default': config(
    'DATABASE_URL',
    default='sqlite:///'+BASE_DIR.child('db.sqlite3'),
    cast=db_url),
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

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
