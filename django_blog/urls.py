from django.conf.urls import patterns, include, url
from django.contrib import admin

import apps.blog.urls
import xadmin

xadmin.autodiscover()

from xadmin.plugins import xversion
#xversion.registe_models()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
    url(r'^blog/', include(apps.blog.urls)),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/',include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),


)
