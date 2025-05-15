from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import (
    MeleeWeapons,

)


class DetailViewMeleeWeapons(LoginRequiredMixin, DetailView):
    """Detail view of a melee weapon."""
    model = MeleeWeapons
    context_object_name = "meleeweapon"

