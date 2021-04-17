"""reno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Add By Aman Verma
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
#Add Include With Path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls', namespace='home')),
    path('', include('apps.content_pages.urls', namespace='content_pages')),
    path('', include('apps.categories.urls', namespace='categories')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('newspaper/', include('apps.newspaper.urls', namespace='newspapers')),
]

#Add By Aman Verma
#set static files DIR
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
