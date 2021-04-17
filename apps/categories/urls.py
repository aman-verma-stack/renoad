from django.urls import path, include
from apps.blog.views import coming_soon_view
from .views import *

app_name = 'categories'

urlpatterns = [
    path('category/', categories_view, name='categories_view'),
    path('category/<slug:slug>/', subCategories, name='subcategory'),
    path('category/details/<slug:slug>/', categories_details, name='categories_details'),
]