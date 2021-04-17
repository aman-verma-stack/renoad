from django.contrib import admin
from .models import *


class AboutManager(admin.ModelAdmin):
    list_display = ('id', 'updated_on',)

    # def has_add_permission(self, request):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False


class CancellationManager(admin.ModelAdmin):
    list_display = ('id', 'updated_on',)

    # def has_add_permission(self, request):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False


class CareerManager(admin.ModelAdmin):
    list_display = ('id','updated_on',)

    # def has_add_permission(self, request):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False


class BookManager(admin.ModelAdmin):
    list_display = ('id','updated_on',)

    def has_delete_permission(self, request, obj=None):
        return False


class PrivacyManager(admin.ModelAdmin):
    list_display = ('id','updated_on',)

    def has_delete_permission(self, request, obj=None):
        return False


class TermsManager(admin.ModelAdmin):
    list_display = ('id','updated_on',)

    def has_delete_permission(self, request,  obj=None):
        return False


class EpaperManager(admin.ModelAdmin):
        list_display = ('id', 'title', 'link',)


class FeedbackManager(admin.ModelAdmin):
    list_display = ('id','updated_on',)

    def has_delete_permission(self, request,  obj=None):
        return False


admin.site.register(About, AboutManager)
admin.site.register(Cancellation, CancellationManager)
admin.site.register(Career, CareerManager)
admin.site.register(Book, BookManager)
admin.site.register(Privacy, PrivacyManager)
admin.site.register(Terms, TermsManager)
admin.site.register(Epapers, EpaperManager)
admin.site.register(Feedback, FeedbackManager)
