from django.shortcuts import render
# Create your views here.

from .forms import CommentForm


def index(request):
    return render(request, "wedding_index.html", {})


def add_comments(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("helloworld")
    else:
        form = CommentForm()
    return render(request, 'wedding_index.html', {'form': form})

