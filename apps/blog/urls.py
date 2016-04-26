#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import BlogDetailView
from .views import BlogListView
from .views import TagListView

urlpatterns = [url(r'^tag/(?P<tag_name>[\w,-]+)$', BlogListView.as_view(), name='tag'),
               url(r'^category/(?P<cat_name>\w+)$', BlogListView.as_view(), name='category'),
               url(r'^tags$', TagListView.as_view(), name='tag_list'),
               url(r'^$', BlogListView.as_view(), name="home"),
               url(r'^(?P<pk>\d+)/(?P<blog_link>[\w,-]+)$', BlogDetailView.as_view(), name='blog_detail'),

               ]
