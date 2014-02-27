from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Blog, Tag
from django_blog.settings.common import PAGE_SIZE

# Create your views here.

def hello(request):
    return render(request, 'hello.html')

def index(request):
    
    blog_list = get_list_or_404(Blog.objects.order_by('-publish_time'), status='p')
    paginator =  Paginator(blog_list, PAGE_SIZE)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'blogs':blogs})


def blog_detail(request,blog_id, blog_link=''):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog-post.html', {'blog':blog})

def author_blogs(request, username):
    blogs = get_list_or_404(Blog, author__username=username)
    return render(request, 'index.html',{'blogs':blogs})

def archives(request):
    blogs = get_list_or_404(Blog.objects.order_by('-publish_time'), status='p')
    return render(request, 'archives.html', {'blogs':blogs})

def about(request):
    return render(request, 'about.html',{})
