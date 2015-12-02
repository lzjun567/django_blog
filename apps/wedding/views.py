from django.shortcuts import render

from .forms import CommentForm


def index(request):
    return render(request, "wedding_index.html", {})


def add_comments(request):
    success = False
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = CommentForm()
    return render(request, 'wedding_index.html', {'form': form, "success": success})

