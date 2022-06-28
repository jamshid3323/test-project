from django.contrib import admin
from .models import BlogModel, CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['title', 'created_at']
    list_filter = ['created_at']
