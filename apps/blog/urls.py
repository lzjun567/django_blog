#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import BlogDetailView
from .views import BlogListView

urlpatterns = patterns('apps.blog.views',
                       url(r'^$', BlogListView.as_view(), name="home"),
                       url(r'^(?P<pk>\d+)/(?P<blog_link>[\w,-]*)$', BlogDetailView.as_view(), name='blog_detail'),
                       )
