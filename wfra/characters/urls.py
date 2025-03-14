from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.ListCharacters.as_view(), name="all"),
    path("create/", views.CreateCharacter.as_view(), name="create"),
    path("<int:pk>/", views.DetailViewCharacter.as_view(), name="detail"),
    path("update/<int:pk>/", views.UpdateViewCharacter.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeleteViewCharacter.as_view(), name="delete"),
]
