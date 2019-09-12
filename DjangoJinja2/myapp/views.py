# from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy

from . import models


class IndexView(TemplateView):
    template_name = 'myapp/index.jinja'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject'] = "yolo"
        return context


class CardsView(TemplateView):
    template_name = 'myapp/cards.jinja'


class PostListView(ListView):
    model = models.Post
    # context_object_name =  # default to <model_name>_list
    # template_name =  # default to '<app_name>/<model_name>_list.html'
    template_name = "myapp/post_list.jinja"


class PostDetailView(DetailView):
    model = models.Post
    # context_object_name =  # default to <model_name>
    template_name = 'myapp/post_detail.jinja'


class PostCreateView(CreateView):
    # model need to implement get_absolute_url()
    model = models.Post
    fields = '__all__'  # ('title', 'content')
    template_name = 'myapp/post_form.jinja'


class PostUpdateView(UpdateView):
    model = models.Post
    fields = '__all__'
    template_name = 'myapp/post_form.jinja'


class PostDeleteView(DeleteView):
    model = models.Post
    template_name = 'myapp/post_confirm_delete.jinja'
    success_url = reverse_lazy('myapp:post_list')
