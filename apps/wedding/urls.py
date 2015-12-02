#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('apps.wedding.views',
                       url(r'^$', "index"),
                       url(r'^add_comments/', 'add_comments'),
                       )
