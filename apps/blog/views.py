from django.shortcuts import (render, redirect,
                              get_object_or_404, get_list_or_404)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Blog, Tag
from django_blog.settings.common import PAGE_SIZE


def about(request):
    return render(request, 'about.html')

def blog_home(request):
    return redirect('home', permanent=True)


def not_found(request):
    return render(request, '404.html', {})


def admin_criteria(request):
    """
        if not login or not super user ,
        then return all published and public articles
    """
    criteria = {'status': 'p'}
    if not (request.user and request.user.is_superuser):
        criteria['is_public'] = True
    return criteria


def index(request):
    blog_list = get_list_or_404(
        Blog.objects.order_by('-publish_time'),
        **admin_criteria(request)
    )

    paginator = Paginator(blog_list, PAGE_SIZE)
    page_num = request.GET.get('p') or 1
    print page_num
    try:
        blogs = paginator.page(page_num)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'blogs': blogs, 'page_num': int(page_num)+1})


def blog_detail(request, blog_id, blog_link=''):
    blog = get_object_or_404(Blog,
                             pk=blog_id,
                             **admin_criteria(request)
    )
    blog.access_count += 1
    blog.save()
    return render(request, 'post.html', {'blog': blog})


def author_blogs(request, username):
    blog_list = get_list_or_404(
        Blog.objects.order_by('-publish_time'),
        author__username=username,
        **admin_criteria(request)
    )

    paginator = Paginator(blog_list, PAGE_SIZE)
    page_num = request.GET.get('p') or 1
    print page_num
    try:
        blogs = paginator.page(page_num)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'blogs': blogs, 'page_num': page_num+1})


def archives(request):
    blogs = get_list_or_404(Blog.objects.order_by('-publish_time'),
                            **admin_criteria(request))
    return render(request, 'archives.html', {'blogs': blogs})


def tag(request, tag_title):
    """
    query blogs by tags
    """
    blogs = get_list_or_404(Blog.objects.order_by('-publish_time'),
                            tags__in=Tag.objects.filter(title=tag_title),
                            **admin_criteria(request)
    )

    return render(request, 'archives.html', {'blogs': blogs})

