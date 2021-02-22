"""
IS2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)


urlpatterns = [
    # Uncomment the next line to enable the admin: 
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    #path('dashboard', views.dashboard, name='dashboard'),
    #path('dashboard/', include('accounts.urls')),
    path('admin/', admin.site.urls),
] #+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
