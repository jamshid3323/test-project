from django.contrib import admin
from .models import *


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['created_at']
