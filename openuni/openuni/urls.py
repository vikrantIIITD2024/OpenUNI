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
    path('courses', courses, name='courses'),
    path('app/courses', courses_app, name='App courses'),
    path('assignments', courses, name='assignments'),
    path('certificate', courses, name='certificate'),
    path('contacts', contacts, name='contacts'),
    path('degree', courses, name='degree'),
    path('diploma', courses, name='diploma'),
    path('events', courses, name='events'),
    path('examnotes', courses, name='examnotes'),
    path('exams', courses, name='exams'),
    path('pgprogram', courses, name='pgprogram'),
    path('profile', profile, name='profile'),
    path('questionpaper', courses, name='questionpaper'),
    path('search', search, name='search'),
    path('worpro', worpro, name='worpro'),
    path('faqs', faqs, name='faqs'),
    path('tnc', tnc, name='tnc'),
    path('privacy-policy', privacypolicy, name='privacy-policy'),
    path('demo/<str:course_id>', demo, name='demo'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('login', login, name='login'),
    path('updateprofile', updateprofile, name='updateprofile'),
    path('buy/<str:product_id>', cart, name='cart'),
    path('callback', callback, name='callback'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'main.views.handler404'