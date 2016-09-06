#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import ArchiveView
from .views import BlogDetailView
from .views import BlogsWithCategoryView
from .views import BlogListView
from .views import BlogsWithTagView
from .views import CategoriesView
from .views import TagsView

urlpatterns = [url(r"^tag/(?P<tag_name>[\w,-]+)$", BlogsWithTagView.as_view(), name="tag"),
               url(r"^category/(?P<pk>\d+)/(?P<cat_name>\w+)$", BlogsWithCategoryView.as_view(), name="category"),
               url(r"^tags$", TagsView.as_view(), name="tag_list"),
               url(r"^categories$", CategoriesView.as_view(), name="category_list"),
               url(r"^archives", ArchiveView.as_view(), name="archives"),
               url(r"^$", BlogListView.as_view(), name="home"),
               url(r"^(?P<pk>\d+)/(?P<blog_link>[\w,-]+)$", BlogDetailView.as_view(), name="blog_detail"),

               ]
