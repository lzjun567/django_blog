from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import apps.blog.urls
print apps.blog.urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
     url(r'^blog/', include(apps.blog.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
