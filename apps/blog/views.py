# -*- coding: utf-8 -*-

from django.shortcuts import (render, redirect,
                              get_object_or_404, get_list_or_404)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

from .models import Blog, Tag


def about(request):
    return render(request, 'about.html')


def blog_home(request):
    return redirect('home', permanent=True)


def not_found(request):
    return render(request, '404.html', {})


def _query_blogs(request, pagination=False, **criteria):
    """
    根据指定条件查询blog
    pagination:是否分页返回
    criteria： 查询的key-value对
    如果 pagination=True, 返回blog list和page_num
    如果 pagination=False, 返回blog list
    page_num = -1 表示不能在分页了
    """
    # “发布”状态
    criteria['status'] = 'p'
    if not (request.user and request.user.is_superuser):
        criteria['is_public'] = True
    blog_list = get_list_or_404(Blog.objects.order_by('-publish_time'), **criteria)
    if pagination is True:
        paginator = Paginator(blog_list, settings.PAGE_SIZE)
        page_num = request.GET.get('p', 1)
        print paginator.num_pages
        try:
            blogs = paginator.page(page_num)
        except PageNotAnInteger:
            page_num = 1
            blogs = paginator.page(page_num)
        except EmptyPage:
            page_num = -1
            blogs = paginator.page(paginator.num_pages)
        finally:
            if int(page_num) == paginator.num_pages:
                page_num = -1
        return blogs, int(page_num) + 1
    else:
        return blog_list


def index(request):
    """
    首页
    """
    blogs, next_page = _query_blogs(request, pagination=True)
    return render(request, 'index.html', {'blogs': blogs, 'page_num': next_page})


def blog_detail(request, blog_id, blog_link=''):
    """
    文章详情
    """
    blog = _query_blogs(request, pk=blog_id)[0]
    blog.access_count += 1
    blog.save()
    return render(request, 'post.html', {'blog': blog})


def author_blogs(request, username):
    """
    返回username创建的blog
    """
    blogs, next_page = _query_blogs(request, pagination=True, author__username=username)
    return render(request, 'index.html', {'blogs': blogs, 'page_num': next_page})


def archives(request):
    blogs = _query_blogs(request)
    return render(request, 'archives.html', {'blogs': blogs})


def tag(request, tag_title):
    """
    query blogs by tags
    """
    blogs = _query_blogs(request, tags__in=Tag.objects.filter(title=tag_title))
    return render(request, 'archives.html', {'blogs': blogs})

