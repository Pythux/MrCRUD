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


def create_update(request):
    post_id = request.GET.get('id', None)
    post = None
    if post_id is not None:
        try:
            post_id = int(post_id)
        except ValueError:
            return index(request)
        post = Post.objects.filter(id=post_id).first()
    if request.method == 'POST':
        form = forms.FormPost(request.POST)
        if post:
            form = forms.FormPost(request.POST, instance=post)
        form.full_clean()
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            # print(form.errors.as_data())
            return render(request, 'myapp/create_update.html',
                          {'form': form, 'post': post})
    if request.method == 'GET':
        form = forms.FormPost()
        if post:
            form = forms.FormPost(instance=post)

        return render(request, 'myapp/create_update.html',
                      {'form': form, 'post': post})
    print('error, this request.method not handle: {}'.format(request.method))
