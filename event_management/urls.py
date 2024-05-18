"""roche URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path
from . import views
from .views import dashboard, login_page, logut_page
from . import settings
from .views import about_us_view

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('login/', login_page, name='login'),
    path('logout/', logut_page, name='logout'),
     path('events/', include('events.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('events/user-mark/contact_us.html', views.contact_us_view, name='contact-us'),
     path('events/about_us.html', about_us_view, name='about-us'),
     
    path('USER/',include('USERS.urls'))
    
     
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)