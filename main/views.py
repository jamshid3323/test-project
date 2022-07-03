from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, CreateView
from .models import *
from .forms import MessageModelForm


class HomeView(TemplateView):
    template_name = 'main/home.html'


class ContactView(CreateView):
    model = MessageModel
    form_class = MessageModelForm
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse('contact')
