from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.ListCharacters.as_view(), name="all"),
]