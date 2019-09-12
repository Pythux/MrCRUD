# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models


class IndexView(TemplateView):
    template_name = 'hello.jinja'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject'] = "yolo"
        return context


class PostListView(ListView):
    model = models.Post


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post_detail.jinja'
