from common import *

DEBUG=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# MySQL 
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'django_blog',
#        'USER':'root',
#        'PASSWORD':'',
#        'HOST':'',
#        'PORT':'',
#    }
#}

INSTALLED_APPS += ("debug_toolbar",)

ALLOWED_HOSTS = ['localhost',]

MIDDLEWARE_CLASSES += (
    'middleware.profile.ProfilerMiddleware',
)

