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
        current_site = Site.objects.get_current()
        # 页面信息
        context['page'] = dict(comments=True,
                               path=self.request.path,
                               title=u'关于',
                               permalink="".join(["http://", current_site.domain, "/about"]))
        return context


class TagsView(ListView):
    template_name = 'page.html'
    context_object_name = 'tag_list'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagsView, self).get_context_data(**kwargs)
        tag_list = context.get("tag_list")

        for tag in tag_list:
            blog_count = Blog.objects.filter(tags__pk=tag.id).count()
            tag.blog_count = blog_count

        max_count = min_count = 0
        if len(tag_list) > 0:
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


class CategoriesView(ListView):
    template_name = "page.html"
    context_object_name = "categories"
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        categories = context.get("categories")
        for c in categories:
            blog_count = Blog.objects.filter(category__pk=c.id).count()
            c.blog_count = blog_count

        page = dict()
        page['type'] = 'categories'
        page['title'] = u"标签"
        context['page'] = page
        return context


class BasePostListView(ListView):
    paginate_by = settings.PAGE_SIZE
    context_object_name = "posts"


class ArchiveView(BasePostListView):
    """
    文章归档
    """
    template_name = "archive.html"

    def get_queryset(self):
        posts = Blog.objects.published().public()
        year = None
        for post in posts:
            if post.publish_time.year != year:
                post.year = post.publish_time.year
                year = post.year
        return posts


class BlogListView(BasePostListView):
    """
    首页
    """
    template_name = 'index.html'
    queryset = Blog.objects.published().public()


class BlogsWithCategoryView(BasePostListView):
    """
    指定分类的文章列表
    """
    template_name = 'category.html'

    def get_queryset(self):
        return Blog.objects.published().public().filter(category__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(BlogsWithCategoryView, self).get_context_data(**kwargs)
        context['page'] = dict(category=self.kwargs['cat_name'], url=self.request.path)
        return context


class BlogsWithTagView(BasePostListView):
    """
    指定标签下的文章列表
    """
    template_name = "tag.html"

    def get_queryset(self):
        return Blog.objects.published().public().filter(tags__title=self.kwargs['tag_name'])

    def get_context_data(self, **kwargs):
        context = super(BlogsWithTagView, self).get_context_data(**kwargs)
        context['page'] = dict(tag=self.kwargs['tag_name'], url=self.request.path)
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
    from django.utils.feedgenerator import Atom1Feed
    feed_type = Atom1Feed
    title = "foofish 的笔录"
    link = "/"

    def items(self):
        blogs = Blog.objects.filter(status='p', is_public=True).all().order_by('-publish_time')[:10]
        return blogs

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.snippet
