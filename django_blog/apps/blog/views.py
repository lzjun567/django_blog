from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Blog

# Create your views here.

def hello(request):
    return render(request, 'hello.html')

def index(request):

    blogs = Blog.objects.all()
    print blogs
    return render(request, 'index.html', {'blogs':blogs})


def blog_detail(request,blog_id, blog_link):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog-post.html', {'blog':blog})



