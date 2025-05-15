from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path("meleeweapons/<int:pk>/", views.DetailViewMeleeWeapons.as_view(), name="detail_melee_weapon"),
]
