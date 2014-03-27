from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_blog.sitemaps import BlogSitemap
from django_blog.sitemaps import StaticViewSitemap

admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap,
    'static': StaticViewSitemap
}

urlpatterns = patterns('',
    # Examples:
    url(r'^about$','apps.blog.views.about', name='about'),
    url(r'^$', 'apps.blog.views.index', name='home'),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^grappelli/',include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^baidu_verify_3ymtDfPE09.html', 'apps.blog.views.baidu'),
    url(r'404', 'apps.blog.views.not_found'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',{'sitemaps':sitemaps}),

    
)
