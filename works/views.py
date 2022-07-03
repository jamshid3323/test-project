from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DeleteView


class WorksView(ListView):
    model = WorksModel
    template_name = 'main/works.html'
    paginate_by = 1


class WorksDetailView(DeleteView):
    model = WorksModel
    template_name = 'main/work_detail.html'
