from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


class ListCharacters(LoginRequiredMixin, generic.ListView):
    model = models.Characters

    def get_queryset(self):
        return models.Characters.objects.filter(user=self.request.user)
