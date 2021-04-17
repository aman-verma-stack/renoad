from django.contrib import admin
from .models import *
# Register your models here.

class BlogManager(admin.ModelAdmin):
    list_display = ('id', 'title','slug', 'live')
    search_field = ('title'),


admin.site.register(Blog, BlogManager)