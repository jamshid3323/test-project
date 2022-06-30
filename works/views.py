from django.shortcuts import render
from .models import *
from django.views.generic import ListView


class WorksView(ListView):
    model = WorksModel
    template_name = 'main/works.html'
