from django.urls import path, include
from .views import *

app_name = 'content_pages'

urlpatterns = [
    path('about/', about_view, name = 'about'),
    path('cancellation/', cancellation_view, name = 'Cancellation'),
    path('career/', career_view, name = 'Career'),
    path('e-paper/', e_paper_view, name = 'E_paper'),
    path('feedback/', feedback_view, name = 'Feedback'),
    path('book/', book_view, name = 'Book'),
    path('privacy/', privacy_view, name = 'Privacy'),
    path('terms/', terms_view, name = 'Terms'),
    path('quick/pay/', quick_pay, name = 'quick_payment'),
]