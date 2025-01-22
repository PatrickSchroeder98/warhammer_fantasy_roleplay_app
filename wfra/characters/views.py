from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from . import models
from .forms import (
    CharactersForm,
    CharacteristicsForm,
    FateForm,
    ResilienceForm,
    BasicSkillsForm,
    AdvancedSkillsForm,
    TalentsForm,
    AmbitionsForm,
    PartyForm,
    PsychologyForm,
    CorruptionAndMutationForm,
    WoundsForm,
    SinForm,
)


class ListCharacters(LoginRequiredMixin, generic.ListView):
    model = models.Characters

    def get_queryset(self):
        return models.Characters.objects.filter(user=self.request.user)


class CreateCharacter(LoginRequiredMixin, View):
    def get(self, request):
        # Create empty forms

        character_form = CharactersForm()
        characteristics_form = CharacteristicsForm()
        fate_form = FateForm()
        resilience_form = ResilienceForm()
        basic_skills_form = BasicSkillsForm()
        advanced_skills_form = AdvancedSkillsForm()
        talents_form = TalentsForm()
        ambitions_form = AmbitionsForm()
        party_form = PartyForm()
        psychology_form = PsychologyForm()
        corruption_and_mutation_form = CorruptionAndMutationForm()
        wounds_form = WoundsForm()
        sin_form = SinForm()

        return render(
            request,
            "characters/characters_form.html",
            {
                "character_form": character_form,
                "characteristics_form": characteristics_form,
                "fate_form": fate_form,
                "resilience_form": resilience_form,
                "basic_skills_form": basic_skills_form,
                "advanced_skills_form": advanced_skills_form,
                "talents_form": talents_form,
                "ambitions_form": ambitions_form,
                "party_form": party_form,
                "psychology_form": psychology_form,
                "corruption_and_mutation_form": corruption_and_mutation_form,
                "wounds_form": wounds_form,
                "sin_form": sin_form,
            },
        )

    def post(self, request):
        """Method binds submitted data to the forms. Then it validates all forms. If they are valid, it saves the data.
        If they are invalid, it re-renders the form with errors."""
        character_form = CharactersForm(request.POST)
        characteristics_form = CharacteristicsForm(request.POST)
        fate_form = FateForm(request.POST)
        resilience_form = ResilienceForm(request.POST)
        basic_skills_form = BasicSkillsForm(request.POST)
        advanced_skills_form = AdvancedSkillsForm(request.POST)
        talents_form = TalentsForm(request.POST)
        ambitions_form = AmbitionsForm(request.POST)
        party_form = PartyForm(request.POST)
        psychology_form = PsychologyForm(request.POST)
        corruption_and_mutation_form = CorruptionAndMutationForm(request.POST)
        wounds_form = WoundsForm(request.POST)
        sin_form = SinForm(request.POST)

        if (
            character_form.is_valid()
            and characteristics_form.is_valid()
            and fate_form.is_valid()
            and resilience_form.is_valid()
            and basic_skills_form.is_valid()
            and advanced_skills_form.is_valid()
            and talents_form.is_valid()
            and ambitions_form.is_valid()
            and party_form.is_valid()
            and psychology_form.is_valid()
            and corruption_and_mutation_form.is_valid()
            and wounds_form.is_valid()
            and sin_form.is_valid()
        ):
            # Save the main character form
            character = character_form.save(commit=False)
            character.user = request.user  # Set the logged-in user
            character.save()

            # Save the related forms with a reference to the character
            characteristics = characteristics_form.save(commit=False)
            characteristics.character_id = character
            characteristics.save()

            fate = fate_form.save(commit=False)
            fate.character_id = character
            fate.save()

            resilience = resilience_form.save(commit=False)
            resilience.character_id = character
            resilience.save()

            basic_skills = basic_skills_form.save(commit=False)
            basic_skills.character_id = character
            basic_skills.save()

            advanced_skills = advanced_skills_form.save(commit=False)
            advanced_skills.character_id = character
            advanced_skills.save()

            talents = talents_form.save(commit=False)
            talents.character_id = character
            talents.save()

            party = party_form.save(commit=False)
            party.character_id = character
            party.save()

            psychology = psychology_form.save(commit=False)
            psychology.character_id = character
            psychology.save()

            corruption_and_mutation = corruption_and_mutation_form.save(commit=False)
            corruption_and_mutation.character_id = character
            corruption_and_mutation.save()

            wounds = wounds_form.save(commit=False)
            wounds.character_id = character
            wounds.save()

            sin = sin_form.save(commit=False)
            sin.character_id = character
            sin.save()

            messages.success(request, "Character created successfully!")
            return redirect("characters:all")

        # If any form is invalid, re-render the form with errors
        return render(
            request,
            "characters/character_form.html",
            {
                "character_form": character_form,
                "characteristics_form": characteristics_form,
                "fate_form": fate_form,
                "resilience_form": resilience_form,
                "basic_skills_form": basic_skills_form,
                "advanced_skills_form": advanced_skills_form,
                "talents_form": talents_form,
                "ambitions_form": ambitions_form,
                "party_form": party_form,
                "psychology_form": psychology_form,
                "corruption_and_mutation_form": corruption_and_mutation_form,
                "wounds_form": wounds_form,
                "sin_form": sin_form,
            },
        )


class DetailViewCharacter(LoginRequiredMixin, generic.DetailView):
    model = models.Characters
    context_object_name = "character"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        character = self.object

        context["characteristics"] = models.Characteristics.objects.filter(
            character_id=character
        )
        context["fate"] = models.Fate.objects.filter(character_id=character)
        context["resilience"] = models.Resilience.objects.filter(character_id=character)
        context["basic_skills"] = models.BasicSkills.objects.filter(
            character_id=character
        )
        context["advanced_skills"] = models.AdvancedSkills.objects.filter(
            character_id=character
        )
        context["talents"] = models.Talents.objects.filter(character_id=character)
        context["ambitions"] = models.Ambitions.objects.filter(character_id=character)
        context["party"] = models.Party.objects.filter(character_id=character)
        context["psychology"] = models.Psychology.objects.filter(character_id=character)
        context["corruption_and_mutation"] = (
            models.CorruptionAndMutation.objects.filter(character_id=character)
        )
        context["wounds"] = models.Wounds.objects.filter(character_id=character)
        context["sin"] = models.Sin.objects.filter(character_id=character)

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
