from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from .models import Blog, Tag

# Create your views here.

def hello(request):
    return render(request, 'hello.html')

def index(request):

    blogs = get_list_or_404(Blog)
    return render(request, 'index.html', {'blogs':blogs})


def blog_detail(request,blog_id, blog_link):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog-post.html', {'blog':blog})

def author_blogs(request, username):
    blogs = get_list_or_404(Blog, author__username=username)
    return render(request, 'index.html',{'blogs':blogs})

def archives(request):
    blogs = get_list_or_404(Blog)
    return render(request, 'archives.html', {'blogs':blogs})





