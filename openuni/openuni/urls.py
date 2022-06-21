"""openuni URL Configuration

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
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index', index, name='index'),
    path('account', account, name='account'),
    path('assignments', assignments, name='assignments'),
    path('certificate', certificate, name='certificate'),
    path('contacts', contacts, name='contacts'),
    path('degree', degree, name='degree'),
    path('diploma', diploma, name='diploma'),
    path('events', events, name='events'),
    path('examnotes', examnotes, name='examnotes'),
    path('exams', exams, name='exams'),
    path('pgprogram', pgprogram, name='pgprogram'),
    path('profile', profile, name='profile'),
    path('questionpaper', questionpaper, name='questionpaper'),
    path('search', search, name='search'),
    path('worpro', worpro, name='worpro'),
    path('faqs', faqs, name='faqs'),
    path('tnc', tnc, name='tnc'),
    path('privacy-policy', privacypolicy, name='privacy-policy'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
