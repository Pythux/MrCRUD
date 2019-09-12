# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models


class IndexView(TemplateView):
    template_name = 'myapp/index.jinja'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject'] = "yolo"
        return context


class LoginView(TemplateView):
    template_name = 'myapp/login.jinja'


class PostListView(ListView):
    model = models.Post
    # context_object_name =  # default to <model_name>_list
    # template_name =  # default to '<app_name>/<model_name>_list.html'
    template_name = "myapp/post_list.jinja"


class PostDetailView(DetailView):
    model = models.Post
    # context_object_name =  # default to <model_name>
    template_name = 'myapp/post_detail.jinja'
