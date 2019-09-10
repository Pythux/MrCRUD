from django.shortcuts import render
# from django.http import HttpResponse

from .models import Post
from . import forms


def index(request):
    posts = Post.objects.all()
    return render(request, 'myapp/index.html', context={'posts': posts})


def form_name_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = forms.FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("not valide form")
    form = forms.FormName()
    return render(request, 'myapp/form_page.html', {'form': form})
