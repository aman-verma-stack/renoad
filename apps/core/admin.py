from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

class CityManager(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'city', 'slug',)
    list_filter  = ('city',)


class LanguageManager(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'language', 'slug')
    list_filter = ('language',)


class AdTypeManager(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'adtype', 'slug')
    list_filter = ('adtype',)


admin.site.register(City, CityManager)
admin.site.register(Language, LanguageManager)
admin.site.register(AdType, AdTypeManager)