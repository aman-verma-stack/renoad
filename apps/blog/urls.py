from django.urls import path, include
from .views import *


app_name = 'blog'

urlpatterns = [
    path('coming/', coming_soon_view, name = 'Coming_soon'),
    path('', blog_main, name = 'blog_main'),
    path('details/<slug:slug>/', blog_details, name = 'blog_details'),
]
