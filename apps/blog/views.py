# -*- coding: utf-8 -*-

__author__ = "liuzhijun"

import random
from django.conf import settings
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.syndication.views import Feed
from .models import Blog, Tag
from django.core.exceptions import PermissionDenied

from .libs.tag_cloud import TagCloud

from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about_active'] = True
        return context


class TagListView(ListView):
    template_name = 'tag_list.html'
    context_object_name = 'tag_list'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        tag_list = context.get("tag_list")
        # 有博文的tag
        tag_list_have_blog = []
        for tag in tag_list:
            blog_count = Blog.objects.filter(tags__pk=tag.id).count()
            if blog_count > 0:
                tag.blog_count = blog_count
                tag_list_have_blog.append(tag)

        max_count = max(tag_list_have_blog, key=lambda tag: tag.blog_count).blog_count
        min_count = min(tag_list_have_blog, key=lambda tag: tag.blog_count).blog_count

        tag_cloud = TagCloud(min_count, max_count)

        for tag in tag_list_have_blog:
            tag_font_size = tag_cloud.get_tag_font_size(tag.blog_count)
            color = tag_cloud.get_tag_color(tag.blog_count)
            tag.color = color
            tag.font_size = tag_font_size

        context['tag_list'] = tag_list_have_blog
        context['tag_active'] = True
        return context


class BlogListView(ListView):
    template_name = 'index.html'
    paginate_by = settings.PAGE_SIZE
    context_object_name = "blog_list"

    def get_queryset(self):
        # 只显示状态为发布且公开的文章列表
        query_condition = {
            'status': 'p',
            'is_public': True
        }

        if 'tag_name' in self.kwargs:
            query_condition['tags__title'] = self.kwargs['tag_name']
        elif 'cat_name' in self.kwargs:
            query_condition['category__title'] = self.kwargs['cat_name']

        return Blog.objects.filter(**query_condition).order_by('-publish_time')

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        tag_name = self.kwargs.get('tag_name')
        if tag_name:
            context['tag_title'] = tag_name

            context['tag_description'] = ''
        else:
            print('index active')
            context['index_active'] = True

        # 最近文章
        return context


class BlogDetailView(DetailView):
    """
    文章详情
    """
    model = Blog
    template_name = "post_detail.html"

    def get_object(self, queryset=None):
        blog = super(BlogDetailView, self).get_object(queryset)
        if blog.status == 'd' or (not blog.is_public and self.request.user != blog.author):
            raise PermissionDenied
        # 阅读数增1
        blog.access_count += 1
        blog.save(modified=False)
        return blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        current_post = context.get("object")

        # 随机文章
        count = Blog.objects.filter(status='p', is_public=True).count()
        randint = random.randint(0, count - 5)
        try:
            random_posts = Blog.objects.exclude(pk=current_post.id).filter(status='p', is_public=True)[
                           randint:randint + 5]
        except IndexError:
            random_posts = None
        context['random_posts'] = random_posts
        return context


class LatestPosts(Feed):
    """
    RSS 输出
    """
    title = "foofish 的笔录"
    link = "/"

    def items(self):
        blogs = Blog.objects.filter(status='p', is_public=True).all().order_by('-publish_time')[:10]
        return blogs

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.snippet
