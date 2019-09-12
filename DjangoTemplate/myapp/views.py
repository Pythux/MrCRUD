from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Post
from . import forms


def index(request):
    posts = Post.objects.all()
    return render(request, 'myapp/index.html', context={'posts': posts})


def detail(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if post is None:
        raise Http404('personalised error message')
    return render(request, 'myapp/detail.html', {'post': post})


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('myapp:index'))


def create_update(request):
    post_id = request.GET.get('id', None)
    post = None
    if post_id is not None:
        try:
            post_id = int(post_id)
        except ValueError:
            raise Http404('the ID is not event an integer')
        post = get_object_or_404(Post, pk=post_id)
        # post = Post.objects.filter(id=post_id).first()
    if request.method == 'POST':
        form = forms.FormPost(request.POST)
        if post:
            form = forms.FormPost(request.POST, instance=post)
        form.full_clean()
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('myapp:index'))
        else:
            print(form.errors.as_data())
            return render(request, 'myapp/create_update.html',
                          {'form': form})
    if request.method == 'GET':
        form = forms.FormPost()
        if post:
            form = forms.FormPost(instance=post)

        return render(request, 'myapp/create_update.html',
                      {'form': form})
    print('error, this request.method not handle: {}'.format(request.method))
