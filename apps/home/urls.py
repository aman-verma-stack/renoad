from django.urls import path, include
from .views import *

app_name = 'home'

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('contact/', ContactView, name = 'Contact'),
]