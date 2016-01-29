# -*- coding: utf-8 -*-
import random
from django.conf import settings
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.syndication.views import Feed
from .models import Blog


def baidu(request):
    return render(request, 'baidu_verify_3ymtDfPE09.html')


def about(request):
    return render(request, 'about.html')


def not_found(request):
    return render(request, '404.html', {})


class BlogListView(ListView):
    model = Blog
    # 只显示状态为发布且公开的文章列表
    queryset = Blog.objects.filter(status='p', is_public=True)
    template_name = 'post_list.html'
    paginate_by = settings.PAGE_SIZE
    ordering = "-publish_time"
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    """
    文章详情
    """
    model = Blog
    template_name = "post_detail.html"

    def get_object(self, queryset=None):
        blog = super(BlogDetailView, self).get_object(queryset)
        # 阅读数增1
        blog.access_count += 1
        blog.save()
        return blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        current_post = context.get("object")

        # 随机文章
        count = Blog.objects.filter(status='p', is_public=True).count()
        randint = random.randint(0, count)
        print(count, randint)
        try:
            random_post = Blog.objects.filter(status='p', is_public=True)[randint:randint + 1][0]
        except IndexError:
            random_post = None
        try:
            next_post = Blog.objects.filter(pk__lt=current_post.id).order_by('-pk')[0]
        except IndexError:
            next_post = None

        context['next_post'] = next_post
        context['random_post'] = random_post
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
