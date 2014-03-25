from django.conf.urls import patterns, include, url
from django.contrib import admin

import apps.blog.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.blog.views.index', name='home'),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^grappelli/',include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap.xml', 'apps.blog.views.sitemap'),
    url(r'^baidu_verify_3ymtDfPE09.html', 'apps.blog.views.baidu'),
    url(r'404', 'apps.blog.views.not_found'),

    
)
