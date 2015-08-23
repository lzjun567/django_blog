#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('apps.blog.views',

                       url(r'^$', 'blog_home'),
                       url(r'^page/(?P<page_num>\d+)', 'index'),
                       url(r'^(?P<blog_id>\d+)/(?P<blog_link>[\w,-]*)$', 'blog_detail', name='blog_detail'),
                       url(r'^author/(?P<username>\w+)$', 'author_blogs', name='author_blogs'),
                       url(r'^archives/(?P<page_num>\d?)$', 'archives', name='archives'),
                       url(r'^tag/(?P<tag_title>[\w,-]*)$', 'tag', name='tag'),
)

