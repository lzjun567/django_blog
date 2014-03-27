"""
/app
Django settings for django_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import time
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xhcg42=d%md&1jcy$c8%#p5e+59!)25v$m$%uq*^1hfx%23i+p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

STATIC_URL = '/static/'

#for deployment, collects the static files into STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')

#STATICFILES_DIRS = (
#        os.path.join(BASE_DIR, "static"),
#)

TEMPLATE_DIRS =  (
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),        
    os.path.join(BASE_DIR, 'django_blog/apps/blog/templates').replace('\\','/'),        
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.contrib.messages.context_processors.messages',
    'apps.blog.processor.tag_list',
)


ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'reversion',
    'apps.blog',
    'pagedown',
    'south',
    'apps.bootstrap_pagination',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_blog.urls'

WSGI_APPLICATION = 'django_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
TIME_ZONE = 'Etc/GMT%+-d'%(time.timezone/3600)
LANGUAGE_CODE = 'zh-cn'
SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = False

#TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    #'plugins': [
    #        "advlist autolink lists link image charmap print preview anchor",
    #        "searchreplace visualblocks code fullscreen",
    #        "insertdatetime media table contextmenu paste moxiemanager"
    #    ],
    #'theme': "simple",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
#TINYMCE_COMPRESSOR = True

PAGE_SIZE = 6

#compressor
INSTALLED_APPS += ("compressor",)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
)
