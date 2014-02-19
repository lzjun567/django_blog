from django.shortcuts import render

# Create your views here.

def hello(request):
    return render(request, 'hello.html')

def index(request):
    return render(request, 'index.html')

