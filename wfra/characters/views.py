from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from . import models
from .forms import CharactersForm, FateForm, ResilienceForm


class ListCharacters(LoginRequiredMixin, generic.ListView):
    model = models.Characters

    def get_queryset(self):
        return models.Characters.objects.filter(user=self.request.user)


# class CreateCharacter(LoginRequiredMixin, generic.CreateView):
#     model = models.Characters
#     form_class = CharactersForm
#     success_url = reverse_lazy('characters:all')
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return super().form_valid(form)

class CreateCharacter(LoginRequiredMixin, View):
    def get(self, request):
        # Create empty forms
        character_form = CharactersForm()
        fate_form = FateForm()
        resilience_form = ResilienceForm()
        return render(request, "characters/characters_form.html", {
            "character_form": character_form,
            "fate_form": fate_form,
            "resilience_form": resilience_form,
        })

    def post(self, request):
        """Method binds submitted data to the forms. Then it validates all forms. If they are valid, it saves the data.
        If they are invalid, it re-renders the form with errors."""
        character_form = CharactersForm(request.POST)
        fate_form = FateForm(request.POST)
        resilience_form = ResilienceForm(request.POST)

        if character_form.is_valid() and fate_form.is_valid() and resilience_form.is_valid():
            # Save the main character form
            character = character_form.save(commit=False)
            character.user = request.user  # Set the logged-in user
            character.save()

            # Save the related forms with a reference to the character
            fate = fate_form.save(commit=False)
            fate.character_id = character
            fate.save()

            resilience = resilience_form.save(commit=False)
            resilience.character_id = character
            resilience.save()

            messages.success(request, "Character created successfully!")
            return redirect("characters:all")

        # If any form is invalid, re-render the form with errors
        return render(request, "characters/character_form.html", {
            "character_form": character_form,
            "fate_form": fate_form,
            "resilience_form": resilience_form,
        })


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
