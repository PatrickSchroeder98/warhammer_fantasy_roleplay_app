from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from . import models
from .forms import CharactersForm


class ListCharacters(LoginRequiredMixin, generic.ListView):
    model = models.Characters

    def get_queryset(self):
        return models.Characters.objects.filter(user=self.request.user)


class CreateCharacter(LoginRequiredMixin, generic.CreateView):
    model = models.Characters
    form_class = CharactersForm
    success_url = reverse_lazy('characters:all')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DetailViewCharacter(LoginRequiredMixin, generic.DetailView):
    model = models.Characters
    context_object_name = 'character'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        character = self.object

        context['experience'] = models.Experience.objects.filter(character_id=character)
        context['basic_skills'] = models.BasicSkills.objects.filter(character_id=character)
        context['advanced_skills'] = models.AdvancedSkills.objects.filter(character_id=character)

        return context


class DeleteViewCharacter(LoginRequiredMixin, generic.DeleteView):
    model = models.Characters
    success_url = reverse_lazy("characters:all")

    def get_queryset(self):
        # Ensure only the owner can delete their characters
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Character Deleted")
        return super().delete(*args, **kwargs)
