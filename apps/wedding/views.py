from django.shortcuts import render
from .forms import CommentForm
from .models import Comment
from django.shortcuts import redirect

def index(request):
    comments = Comment.objects.all()
    return render(request, "wedding_index.html", {"comments": comments})


def add_comments(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()

    return redirect("/wedding/")

