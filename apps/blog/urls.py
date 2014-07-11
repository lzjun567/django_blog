from django.conf.urls import patterns, url
#import views
#
#urlpatterns = patterns(views,
#    # Examples:
#    # url(r'^$', 'django_blog.views.home', name='home'),
#    url(r'^hello/', views.hello),
#    url(r'^index$', views.index),
#    url(r'^$', views.index),
#    url(r'^(?P<blog_id>\d+)/(?P<blog_link>\w*)$', views.blog_detail),
#)

urlpatterns = patterns('apps.blog.views',

    #url(r'^index$', 'index', name='index'),
    url(r'^$', 'blog_home'),
    url(r'^(?P<blog_id>\d+)/(?P<blog_link>[\w,-]*)$', 'blog_detail', name='blog_detail'),
    url(r'^author/(?P<username>\w+)$', 'author_blogs', name='author_blogs'),
    url(r'^archives$', 'archives', name='archives'),
    url(r'^tag/(?P<tag_title>[\w,-]*)$','tag', name='tag'),
)
