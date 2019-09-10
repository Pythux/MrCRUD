from django.shortcuts import render
# from django.http import HttpResponse

from .models import Post
from . import forms


def index(request):
    posts = Post.objects.all()
    return render(request, 'myapp/index.html', context={'posts': posts})


def detail(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    return render(request, 'myapp/detail.html', {'post': post})


def post_add(request):
    if request.method == 'POST':
        print(request.POST)
        form = forms.FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("not valide form")
    form = forms.FormName()
    return render(request, 'myapp/add.html', {'form': form})
