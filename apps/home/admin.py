from django.contrib import admin
from .models import *

# Register your models here.

class HomeManager(admin.ModelAdmin):
    list_display = ('id', 'description',  'updated_on')
    
    def has_add_permission(self, request):
        return True
    def has_delete_permission(self, request, obj=None):
        return False


class ReviewManager(admin.ModelAdmin):
    list_display = ('id', 'title','rating', 'live')
    search_field = ('title'),


class PartnersManager(admin.ModelAdmin):
    list_display = ('id', 'slug','alt')
    search_field = ('alt'),

    

admin.site.register(Reviews, ReviewManager)
admin.site.register(HomeContent, HomeManager)
admin.site.register(Partners, PartnersManager)
