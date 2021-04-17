from django.urls import path, include
from apps.blog.views import coming_soon_view
from apps.newspaper.views import newspaper_details

app_name = 'newspaper'

urlpatterns = [
    path('', coming_soon_view, name = 'Coming_soon'),
    path('aaj/', newspaper_details, name = 'newspaper_details'),
]