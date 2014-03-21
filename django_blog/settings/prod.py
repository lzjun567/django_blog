from common import *

DEBUG = False
TEMPLATE_LOADERS = (
    (
        'django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
    ),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'django_blog',
	'USER': '',
	'PASSWORD':'',
    }
}

ALLOWED_HOSTS = ['foofish.net','www.foofish.net']
