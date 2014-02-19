from django.conf.urls import patterns, url
import views

urlpatterns = patterns(views,
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
    url(r'^hello/', views.hello),
    url(r'^index/', views.index),
)
