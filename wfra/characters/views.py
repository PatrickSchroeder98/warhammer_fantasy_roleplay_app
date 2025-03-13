from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from .models import (
    Characters,
    Characteristics,
    Fate,
    Resilience,
    Experience,
    Movement,
    BasicSkills,
    AdvancedSkills,
    Talents,
    Ambitions,
    Party,
    Psychology,
    CorruptionAndMutation,
    Wounds,
    Sin,
)
from .forms import (
    CharactersForm,
    CharacteristicsForm,
    FateForm,
    ResilienceForm,
    ExperienceForm,
    MovementForm,
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
    """List view of characters."""

    model = Characters

    def get_queryset(self):
        """Returns the query with all characters of logged in user."""
        return Characters.objects.filter(user=self.request.user)


class CreateCharacter(LoginRequiredMixin, View):
    """View for creating new character."""

    def get(self, request):
        """Method creates empty forms for character creation."""

        character_form = CharactersForm()
        characteristics_form = CharacteristicsForm()
        fate_form = FateForm()
        resilience_form = ResilienceForm()
        experience_form = ExperienceForm()
        movement_form = MovementForm()
        basic_skills_form = BasicSkillsForm()

        AdvancedSkillsFormSet = modelformset_factory(
            AdvancedSkills, form=AdvancedSkillsForm, extra=1, can_delete=False
        )
        advanced_skills_formset = AdvancedSkillsFormSet(
            queryset=AdvancedSkills.objects.none()
        )

        TalentsFormSet = modelformset_factory(
            Talents, form=TalentsForm, extra=1, can_delete=False
        )
        talents_formset = TalentsFormSet(
            queryset=Talents.objects.none()
        )

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
                "experience_form": experience_form,
                "movement_form": movement_form,
                "basic_skills_form": basic_skills_form,
                "advanced_skills_form": advanced_skills_formset,
                "talents_form": talents_formset,
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
        experience_form = ExperienceForm(request.POST)
        movement_form = MovementForm(request.POST)
        basic_skills_form = BasicSkillsForm(request.POST)

        AdvancedSkillsFormSet = modelformset_factory(
            AdvancedSkills, form=AdvancedSkillsForm, extra=0, can_delete=False
        )
        advanced_skills_formset = AdvancedSkillsFormSet(request.POST)

        TalentsFormSet = modelformset_factory(
            Talents, form=TalentsForm, extra=0, can_delete=False
        )
        talents_formset = TalentsFormSet(request.POST)

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
            and experience_form.is_valid()
            and movement_form.is_valid()
            and basic_skills_form.is_valid()
            and advanced_skills_formset.is_valid()
            and talents_formset.is_valid()
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

            experience = experience_form.save(commit=False)
            experience.character_id = character
            experience.save()

            movement = movement_form.save(commit=False)
            movement.character_id = character
            movement.save()

            basic_skills = basic_skills_form.save(commit=False)
            basic_skills.character_id = character
            basic_skills.save()

            for form in advanced_skills_formset:
                if form.cleaned_data and not form.cleaned_data.get("DELETE", False):
                    advanced_skill = form.save(commit=False)
                    advanced_skill.character_id = character
                    advanced_skill.save()

            for form in talents_formset:
                if form.cleaned_data and not form.cleaned_data.get("DELETE", False):
                    talents = form.save(commit=False)
                    talents.character_id = character
                    talents.save()

            ambitions = ambitions_form.save(commit=False)
            ambitions.character_id = character
            ambitions.save()

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
            "characters/characters_form.html",
            {
                "character_form": character_form,
                "characteristics_form": characteristics_form,
                "fate_form": fate_form,
                "resilience_form": resilience_form,
                "experience_form": experience_form,
                "movement_form": movement_form,
                "basic_skills_form": basic_skills_form,
                "advanced_skills_form": advanced_skills_formset,
                "talents_form": talents_formset,
                "ambitions_form": ambitions_form,
                "party_form": party_form,
                "psychology_form": psychology_form,
                "corruption_and_mutation_form": corruption_and_mutation_form,
                "wounds_form": wounds_form,
                "sin_form": sin_form,
            },
        )


class DetailViewCharacter(LoginRequiredMixin, generic.DetailView):
    """Detail view of a character."""

    model = Characters
    context_object_name = "character"

    def get_context_data(self, **kwargs):
        """Method builds and returns a context with all character details."""
        context = super().get_context_data(**kwargs)
        character = self.object

        context["characteristics"] = Characteristics.objects.filter(
            character_id=character
        )
        context["fate"] = Fate.objects.filter(character_id=character)
        context["resilience"] = Resilience.objects.filter(character_id=character)
        context["experience"] = Experience.objects.filter(character_id=character)
        context["movement"] = Movement.objects.filter(character_id=character)
        context["basic_skills"] = BasicSkills.objects.filter(character_id=character)
        context["advanced_skills"] = AdvancedSkills.objects.filter(
            character_id=character
        )
        context["talents"] = Talents.objects.filter(character_id=character)
        context["ambitions"] = Ambitions.objects.filter(character_id=character)
        context["party"] = Party.objects.filter(character_id=character)
        context["psychology"] = Psychology.objects.filter(character_id=character)
        context["corruption_and_mutation"] = CorruptionAndMutation.objects.filter(
            character_id=character
        )
        context["wounds"] = Wounds.objects.filter(character_id=character)
        context["sin"] = Sin.objects.filter(character_id=character)

        return context


class UpdateViewCharacter(LoginRequiredMixin, generic.UpdateView):
    """Update view of a character."""
    model = Characters
    form_class = CharactersForm
    template_name = "characters/characters_update.html"
    success_url = reverse_lazy("characters:all")

    def get_context_data(self, **kwargs):
        """Extend context to include related models."""
        context = super().get_context_data(**kwargs)
        character = self.object  # Current character object

        context["characteristics"] = CharacteristicsForm(
            instance=get_object_or_404(Characteristics, character_id=character)
        )
        context["fate"] = FateForm(
            instance=get_object_or_404(Fate, character_id=character)
        )
        context["resilience"] = ResilienceForm(
            instance=get_object_or_404(Resilience, character_id=character)
        )
        context["experience"] = ExperienceForm(
            instance=get_object_or_404(Experience, character_id=character)
        )
        context["movement"] = MovementForm(
            instance=get_object_or_404(Movement, character_id=character)
        )
        context["basic_skills"] = BasicSkillsForm(
            instance=get_object_or_404(BasicSkills, character_id=character)
        )
        AdvancedSkillsFormSet = modelformset_factory(
            AdvancedSkills, form=AdvancedSkillsForm, extra=1, can_delete=True
        )
        context["advanced_skills_formset"] = AdvancedSkillsFormSet(
            queryset=AdvancedSkills.objects.filter(character_id=character)
        )

        TalentsFormSet = modelformset_factory(
            Talents, form=TalentsForm, extra=1, can_delete=True
        )
        context["talents_formset"] = TalentsFormSet(
            queryset=Talents.objects.filter(character_id=character)
        )

        context["ambitions"] = AmbitionsForm(
            instance=get_object_or_404(Ambitions, character_id=character)
        )
        context["party"] = PartyForm(
            instance=get_object_or_404(Party, character_id=character)
        )
        context["psychology"] = PsychologyForm(
            instance=get_object_or_404(Psychology, character_id=character)
        )
        context["corruption_and_mutation"] = CorruptionAndMutationForm(
            instance=get_object_or_404(CorruptionAndMutation, character_id=character)
        )
        context["wounds"] = WoundsForm(
            instance=get_object_or_404(Wounds, character_id=character)
        )
        context["sin"] = SinForm(
            instance=get_object_or_404(Sin, character_id=character)
        )

        return context

    def form_valid(self, form):
        """Save related models after character form is valid."""
        response = super().form_valid(form)

        character = self.object

        characteristics = get_object_or_404(Characteristics, character_id=character)
        fate = get_object_or_404(Fate, character_id=character)
        resilience = get_object_or_404(Resilience, character_id=character)
        experience = get_object_or_404(Experience, character_id=character)
        movement = get_object_or_404(Movement, character_id=character)
        basic_skills = get_object_or_404(BasicSkills, character_id=character)
        # advanced_skills = get_object_or_404(AdvancedSkills, character_id=character)
        # talents = get_object_or_404(Talents, character_id=character)
        ambitions = get_object_or_404(Ambitions, character_id=character)
        party = get_object_or_404(Party, character_id=character)
        psychology = get_object_or_404(Psychology, character_id=character)
        corruption_and_mutation = get_object_or_404(CorruptionAndMutation, character_id=character)
        wounds = get_object_or_404(Wounds, character_id=character)
        sin = get_object_or_404(Sin, character_id=character)

        characteristics_form = CharacteristicsForm(self.request.POST, instance=characteristics)
        if characteristics_form.is_valid():
            characteristics_form.save()

        fate_form = FateForm(self.request.POST, instance=fate)
        if fate_form.is_valid():
            fate_form.save()

        resilience_form = ResilienceForm(self.request.POST, instance=resilience)
        if resilience_form.is_valid():
            resilience_form.save()

        experience_form = ExperienceForm(self.request.POST, instance=experience)
        if experience_form.is_valid():
            experience_form.save()

        movement_form = MovementForm(self.request.POST, instance=movement)
        if movement_form.is_valid():
            movement_form.save()

        basic_skills_form = BasicSkillsForm(self.request.POST, instance=basic_skills)
        if basic_skills_form.is_valid():
            basic_skills_form.save()

        AdvancedSkillsFormSet = modelformset_factory(
            AdvancedSkills, form=AdvancedSkillsForm, extra=0, can_delete=True
        )
        advanced_skills_formset = AdvancedSkillsFormSet(self.request.POST)

        if advanced_skills_formset.is_valid():
            for form in advanced_skills_formset:
                if form.cleaned_data:
                    if form.cleaned_data.get("DELETE", False):
                        # Delete the skill if marked for deletion
                        form.instance.delete()
                    else:
                        # Assign character_id and save
                        advanced_skill = form.save(commit=False)
                        advanced_skill.character_id = character
                        advanced_skill.save()

        TalentsFormSet = modelformset_factory(
            Talents, form=TalentsForm, extra=0, can_delete=True
        )
        talents_formset = TalentsFormSet(self.request.POST)

        if talents_formset.is_valid():
            for form in talents_formset:
                if form.cleaned_data:
                    if form.cleaned_data.get("DELETE", False):
                        # Delete the skill if marked for deletion
                        form.instance.delete()
                    else:
                        # Assign character_id and save
                        talent = form.save(commit=False)
                        talent.character_id = character
                        talent.save()

        ambitions_form = AmbitionsForm(self.request.POST, instance=ambitions)
        if ambitions_form.is_valid():
            ambitions_form.save()

        party_form = PartyForm(self.request.POST, instance=party)
        if party_form.is_valid():
            party_form.save()

        psychology_form = PsychologyForm(self.request.POST, instance=psychology)
        if psychology_form.is_valid():
            psychology_form.save()

        corruption_and_mutation_form = CorruptionAndMutationForm(self.request.POST, instance=corruption_and_mutation)
        if corruption_and_mutation_form.is_valid():
            corruption_and_mutation_form.save()

        wounds_form = WoundsForm(self.request.POST, instance=wounds)
        if wounds_form.is_valid():
            wounds_form.save()

        sin_form = SinForm(self.request.POST, instance=sin)
        if sin_form.is_valid():
            sin_form.save()

        return response


class DeleteViewCharacter(LoginRequiredMixin, generic.DeleteView):
    """Delete view of a character."""

    model = Characters
    success_url = reverse_lazy("characters:all")

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters."""
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen character."""
        messages.success(self.request, "Character Deleted")
        return super().delete(*args, **kwargs)
