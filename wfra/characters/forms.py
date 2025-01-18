from django import forms
from .models import (
    Characters,
    Characteristics,
    Fate,
    Resilience,
    Experience,
    Movement,
    BasicSkills,
)


class CharactersForm(forms.ModelForm):
    class Meta:
        model = Characters
        fields = (
            "name",
            "species",
            "character_class",
            "career",
            "career_tier",
            "career_path",
            "status",
            "age",
            "height",
            "hair",
            "eyes",
        )  # Fields to include in the form

        # Customization of widgets and labels
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Character Name"}
            ),
            "species": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Character Species"}
            ),
        }
        labels = {
            "name": "Character Name",
            "species": "Species",
        }


class CharacteristicsForm(forms.ModelForm):
    class Meta:
        model = Characteristics
        fields = (
            "WS_initial",
            "WS_advances",
            "WS_current",
            "BS_initial",
            "BS_advances",
            "BS_current",
            "S_initial",
            "S_advances",
            "S_current",
            "T_initial",
            "T_advances",
            "T_current",
            "I_initial",
            "I_advances",
            "I_current",
            "Ag_initial",
            "Ag_advances",
            "Ag_current",
            "Dex_initial",
            "Dex_advances",
            "Dex_current",
            "Int_initial",
            "Int_advances",
            "Int_current",
            "WP_initial",
            "WP_advances",
            "WP_current",
            "Fel_initial",
            "Fel_advances",
            "Fel_current",
        )


class FateForm(forms.ModelForm):
    class Meta:
        model = Fate
        fields = ("fate", "fortune")


class ResilienceForm(forms.ModelForm):
    class Meta:
        model = Resilience
        fields = ("resilience", "resolve", "motivation")


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ("current", "spent", "total")


class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ("movement", "walk", "run")


class BasicSkillsForm(forms.ModelForm):
    class Meta:
        model = BasicSkills
        fields = (
            "art_characteristics",
            "art_advances",
            "art_skill",
            "athletics_characteristics",
            "athletics_advances",
            "athletics_skill",
            "bribery_characteristics",
            "bribery_advances",
            "bribery_skill",
            "charm_characteristics",
            "charm_advances",
            "charm_skill",
            "charm_animal_characteristics",
            "charm_animal_advances",
            "charm_animal_skill",
            "climb_characteristics",
            "climb_advances",
            "climb_skill",
            "cool_characteristics",
            "cool_advances",
            "cool_skill",
            "consume_alcohol_characteristics",
            "consume_alcohol_advances",
            "consume_alcohol_skill",
            "dodge_characteristics",
            "dodge_advances",
            "dodge_skill",
            "drive_characteristics",
            "drive_advances",
            "drive_skill",
            "endurance_characteristics",
            "endurance_advances",
            "endurance_skill",
            "entertain_characteristics",
            "entertain_advances",
            "entertain_skill",
            "gamble_characteristics",
            "gamble_advances",
            "gamble_skill",
            "gossip_characteristics",
            "gossip_advances",
            "gossip_skill",
            "haggle_characteristics",
            "haggle_advances",
            "haggle_skill",
            "intimidate_characteristics",
            "intimidate_advances",
            "intimidate_skill",
            "intuition_characteristics",
            "intuition_advances",
            "intuition_skill",
            "leadership_characteristics",
            "leadership_advances",
            "leadership_skill",
            "melee_basic_characteristics",
            "melee_basic_advances",
            "melee_basic_skill",
            "melee_characteristics",
            "melee_advances",
            "melee_skill",
            "navigation_characteristics",
            "navigation_advances",
            "navigation_skill",
            "outdoor_survival_characteristics",
            "outdoor_survival_advances",
            "outdoor_survival_skill",
            "perception_characteristics",
            "perception_advances",
            "perception_skill",
            "ride_characteristics",
            "ride_advances",
            "ride_skill",
            "row_characteristics",
            "row_advances",
            "row_skill",
            "stealth_characteristics",
            "stealth_advances",
            "stealth_skill",
        )

