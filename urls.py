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
                       url(r'^about$', 'apps.blog.views.about', name='about'),
                       url(r'^blog/', include('apps.blog.urls', namespace='blog')),
                       url(r'^$', include('apps.blog.urls', namespace='blog')),
                       url(r'^wedding/', include('apps.wedding.urls', namespace='wedding')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'404', 'apps.blog.views.not_found'),
                       url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
