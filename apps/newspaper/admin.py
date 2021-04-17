from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

class NewspaperManager(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'newspaper',)
    search_field = ('newspaper')

admin.site.register(Newspaper, NewspaperManager)
