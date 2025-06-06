"""
URL configuration for wfra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='index'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('characters/', include('characters.urls', namespace='characters')),
    path('equipment/', include('equipment.urls', namespace='equipment')),
    path('about/', views.AboutPage.as_view(), name="about"),
    path("api/career-options/", views.career_options_api, name="career-options-api"),
    path("api/career-paths/", views.career_paths_api, name="career-paths-api"),
]
