"""
Django settings for compare_cars_prices project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import os.path
import posixpath
from local_settings import *

import djcelery
from cars_scrapping import *

djcelery.setup_loader()
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',    
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',    
#     'django.template.loaders.eggs.Loader',
)

#site infos
# SITE_NAME = 'comapare_car_prices'# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.redirects',   
    'rest_framework',
    'compare_cars',
    'cars_scrapping',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'djangular.middleware.DjangularUrlMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',    
    'django.middleware.locale.LocaleMiddleware', 
)

ROOT_URLCONF = 'compare_cars_prices.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
            ],
        },
    },
]



WSGI_APPLICATION = 'compare_cars_prices.wsgi.application'

# The backend used to store task results - because we're going to be 
# using RabbitMQ as a broker, this sends results back as AMQP messages
CELERY_RESULT_BACKEND = "amqp"
CELERY_IMPORTS = ("cars_scrapping.tasks", )
CELERY_ALWAYS_EAGER = True

# Rabbit MQ settings
BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_PASSWORD = "mypassword"
BROKER_USER = "myuser"
BROKER_VHOST = "myvhost"
#BROKER_URL = "amqp://myuser:mypassword@localhost:5672//"

BROKER_URL = 'amqp://guest:guest@localhost:5672/'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    "runs-every-30-seconds": {
        "task": "cars_scrapping.tasks.hello",
        "schedule": timedelta(seconds=30),
        "args": (),
    },
}

STATIC_URL = '/static/'

 
