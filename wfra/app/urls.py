from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path(r'^register/$', views.register, name='register')
]