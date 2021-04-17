from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *
# Register your models here.


class CategoryManager(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'category','slug','priority',)
    search_field = ('category',)
    
    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


class SubCategoryManager(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'category', 'name','slug', 'live')
    search_field = ('category', 'name',)

    def has_add_permission(self, request):
        return True


admin.site.register(Categories,CategoryManager)
admin.site.register(SubCategory, SubCategoryManager)

