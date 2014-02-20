from django.shortcuts import render

from .models import Blog

# Create your views here.

def hello(request):
    return render(request, 'hello.html')

def index(request):

    blogs = Blog.objects.all()
    print blogs
    return render(request, 'index.html', {'blogs':blogs})

