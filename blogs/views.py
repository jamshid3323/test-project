from django.shortcuts import render
from .models import *
from django.views.generic import ListView


class BlogView(ListView):
    model = BlogModel
    template_name = 'main/blogs.html'
    paginate_by = 1
    page_kwarg = 'blog'
