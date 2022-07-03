from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class BlogView(ListView):
    model = BlogModel
    template_name = 'main/blogs.html'
    paginate_by = 1


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'main/blog_detail.html'
