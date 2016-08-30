# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .libs.tag_cloud import TagCloud
from .models import Blog, Tag, Category

__author__ = "liuzhijun"


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        page = dict()
        page['comments'] = True
        page['path'] = self.request.path
        page['title'] = u"关于"
        current_site = Site.objects.get_current()
        page['permalink'] = "".join(["http://", current_site.domain, "/about"])
        context['page'] = page
        return context


class TagListView(ListView):
    template_name = 'page.html'
    context_object_name = 'tag_list'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        tag_list = context.get("tag_list")
        # 有博文的tag
        for tag in tag_list:
            blog_count = Blog.objects.filter(tags__pk=tag.id).count()
            tag.blog_count = blog_count

        max_count = max(tag_list, key=lambda tag: tag.blog_count).blog_count
        min_count = min(tag_list, key=lambda tag: tag.blog_count).blog_count

        tag_cloud = TagCloud(min_count, max_count)

        for tag in tag_list:
            tag_font_size = tag_cloud.get_tag_font_size(tag.blog_count)
            color = tag_cloud.get_tag_color(tag.blog_count)
            tag.color = color
            tag.font_size = tag_font_size

        page = dict()
        page['type'] = 'tags'
        page['title'] = u"分类"
        context['page'] = page
        return context


class CategoryListView(ListView):
    template_name = "page.html"
    context_object_name = "categories"
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        categories = context.get("categories")
        for c in categories:
            blog_count = Blog.objects.filter(category__pk=c.id).count()
            c.blog_count = blog_count

        page = dict()
        page['type'] = 'categories'
        page['title'] = u"标签"
        context['page'] = page
        return context


class ArchiveView(ListView):
    template_name = "archive.html"
    context_object_name = "blog_list"

    def get_queryset(self):
        posts = Blog.objects.filter(status='p', is_public=True).order_by('-publish_time')
        year = None
        for post in posts:
            if post.add_time.year != year:
                post.year = post.add_time.year
                year = post.year
        return posts


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
        return Blog.objects.filter(**query_condition).order_by('-publish_time')


class BlogListByCategoryView(ListView):
    template_name = 'category.html'
    paginate_by = settings.PAGE_SIZE
    context_object_name = "blog_list"

    def get_queryset(self):
        # 只显示状态为发布且公开的文章列表
        query_condition = dict({'status': 'p', 'is_public': True})
        query_condition['category__id'] = self.kwargs['pk']
        return Blog.objects.filter(**query_condition).order_by('-publish_time')

    def get_context_data(self, **kwargs):
        context = super(BlogListByCategoryView, self).get_context_data(**kwargs)
        page = dict()
        page['category'] = self.kwargs['cat_name']
        context['page'] = page
        return context


class BlogListByTagView(ListView):
    template_name = "tag.html"
    context_object_name = "blog_list"
    paginate_by = settings.PAGE_SIZE

    def get_queryset(self):
        return Blog.objects.filter(tags__title=self.kwargs['tag_name']).order_by('-publish_time')

    def get_context_data(self, **kwargs):
        context = super(BlogListByTagView, self).get_context_data(**kwargs)
        page = dict()
        page['tag'] = self.kwargs['tag_name']
        page['url'] = self.request.path
        context['page'] = page
        return context


class BlogDetailView(DetailView):
    """
    文章详情
    """
    model = Blog
    template_name = "post.html"

    def get_object(self, queryset=None):
        blog = super(BlogDetailView, self).get_object(queryset)
        if blog.link != self.kwargs['blog_link']:
            raise Http404()

        if blog.status == 'd' or (not blog.is_public and self.request.user != blog.author):
            raise PermissionDenied
        # 阅读数增1
        blog.access_count += 1
        blog.save(modified=False)
        return blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        current_post = context.get("object")
        from django.contrib.sites.models import Site
        current_site = Site.objects.get_current()
        page = dict()
        page['comments'] = True
        page['title'] = current_post.title
        page['permalink'] = "http://" + current_site.domain + current_post.get_absolute_url()
        page['path'] = current_post.get_absolute_url
        context['page'] = page

        next_post = None
        prev_post = None
        try:
            prev_post = Blog.objects.filter(status='p', is_public=True, pk__lt=current_post.id).order_by('-pk')[0]
            next_post = Blog.objects.filter(status='p', is_public=True, pk__gt=current_post.id).order_by('pk')[0]

        except IndexError:
            pass

        context['next_post'] = next_post
        context['prev_post'] = prev_post
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
