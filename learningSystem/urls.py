"""learningSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path, include
from learningapp.views import index, aboutUs, contact, yourCourse, IntroductionToC, Operators, Conditions, Loops, Arrays, Functions, Classes, Enum
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('aboutUs/', aboutUs, name='aboutUs'),
    path('contact/', contact, name='contact'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('yourCourse/', yourCourse, name='yourCourse'),
    path('introductionToC/', IntroductionToC, name='IntroductionToC'),
    path('operators/', Operators, name='operators'),
    path('conditions/', Conditions, name='conditions'),
    path('loops/', Loops, name='loops'),
    path('arrays/', Arrays, name='arrays'),
    path('functions/', Functions, name='functions'),
    path('classes/', Classes, name='classes'),
    path('enum/', Enum, name='enum'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
