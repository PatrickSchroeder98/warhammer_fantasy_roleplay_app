from django import forms
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
            "character_class": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Character Class"}
            ),
            "career": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Career"}
            ),
            "career_tier": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Career Tier"}
            ),
            "career_path": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Career Path"}
            ),
            "status": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Status"}
            ),
            "age": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Character Age"}
            ),
            "height": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Character Height"}
            ),
            "hair": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Character Hair"}
            ),
            "eyes": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Character Eyes"}
            ),
        }
        labels = {
            "name": "Character Name",
            "species": "Species",
            "character_class": "Character Class",
            "career": "Career",
            "career_tier": "Career Tier",
            "career_path": "Career Path",
            "status": "Status",
            "age": "Character Age",
            "height": "Character Height",
            "hair": "Character Hair",
            "eyes": "Character Eyes",
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

        widgets = {
            "WS_initial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Initial Weapon Skill"}
            ),
            "WS_advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances Weapon Skill"}
            ),
            "WS_current": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Current Weapon Skill"}
            ),
            "BS_initial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Initial Ballistic Skill"}
            ),
            "BS_advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances Ballistic Skill"}
            ),
            "BS_current": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Current Ballistic Skill"}
            ),
            "S_initial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Initial Strength"}
            ),
            "S_advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances Strength"}
            ),
            "S_current": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Current Strength"}
            ),
            "T_initial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Initial Toughness"}
            ),
            "T_advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances Toughness"}
            ),
            "T_current": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Current Toughness"}
            ),
            "I_initial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Initial Initiative"}
            ),
            "I_advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances Initiative"}
            ),
            "I_current": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Current Initiative"}
            ),
            "Ag_initial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Initial Agility"}
            ),
            "Ag_advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances Agility"}
            ),
            "Ag_current": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Current Agility"}
            ),
            "Dex_initial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Initial Dexterity"}
            ),
            "Dex_advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances Dexterity"}
            ),
            "Dex_current": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Current Dexterity"}
            ),
            "Int_initial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Initial Intelligence"}
            ),
            "Int_advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances Intelligence"}
            ),
            "Int_current": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Current Intelligence"}
            ),
            "WP_initial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Initial Willpower"}
            ),
            "WP_advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances Willpower"}
            ),
            "WP_current": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Current Willpower"}
            ),
            "Fel_initial": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Initial Fellowship"}
            ),
            "Fel_advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances Fellowship"}
            ),
            "Fel_current": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Current Fellowship"}
            ),
        }

        labels = {
            "WS_initial": "Initial Weapon Skill",
            "WS_advances": "Advances Weapon Skill",
            "WS_current": "Current Weapon Skill",
            "BS_initial": "Initial Ballistic Skill",
            "BS_advances": "Advances Ballistic Skill",
            "BS_current": "Current Ballistic Skill",
            "S_initial": "Initial Strength",
            "S_advances": "Advances Strength",
            "S_current": "Current Strength",
            "T_initial": "Initial Toughness",
            "T_advances": "Advances Toughness",
            "T_current": "Current Toughness",
            "I_initial": "Initial Initiative",
            "I_advances": "Advances Initiative",
            "I_current": "Current Initiative",
            "Ag_initial": "Initial Agility",
            "Ag_advances": "Advances Agility",
            "Ag_current": "Current Agility",
            "Dex_initial": "Initial Dexterity",
            "Dex_advances": "Advances Dexterity",
            "Dex_current": "Current Dexterity",
            "Int_initial": "Initial Intelligence",
            "Int_advances": "Advances Intelligence",
            "Int_current": "Current Intelligence",
            "WP_initial": "Initial Willpower",
            "WP_advances": "Advances Willpower",
            "WP_current": "Current Willpower",
            "Fel_initial": "Initial Fellowship",
            "Fel_advances": "Advances Fellowship",
            "Fel_current": "Current Fellowship",
        }


class FateForm(forms.ModelForm):
    class Meta:
        model = Fate
        fields = ("fate", "fortune")

        widgets = {
            "fate": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Fate Points"}
            ),
            "fortune": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Fortune Points"}
            ),
        }

        labels = {
            "fate": "Fate Points",
            "fortune": "Fortune Points",
        }


class ResilienceForm(forms.ModelForm):
    class Meta:
        model = Resilience
        fields = ("resilience", "resolve", "motivation")

        widgets = {
            "resilience": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Resilience Points"}
            ),
            "resolve": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Resolve Points"}
            ),
            "motivation": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Motivation"}
            ),
        }

        labels = {
            "resilience": "Resilience Points",
            "resolve": "Resolve Points",
            "motivation": "Motivation",
        }


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


class AdvancedSkillsForm(forms.ModelForm):
    class Meta:
        model = AdvancedSkills
        fields = ('name_0', 'attribute_name_0', 'attribute_value_0', 'advances_0', 'total_0',
                  'name_1', 'attribute_name_1', 'attribute_value_1', 'advances_1', 'total_1',
                  'name_2', 'attribute_name_2', 'attribute_value_2', 'advances_2', 'total_2',)


class TalentsForm(forms.ModelForm):
    class Meta:
        model = Talents
        fields = ('talent', 'times_taken', 'description')


class AmbitionsForm(forms.ModelForm):
    class Meta:
        model = Ambitions
        fields = ('short_term', 'long_term')


class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ('party_name', 'short_term', 'long_term', 'members')


class PsychologyForm(forms.ModelForm):
    class Meta:
        model = Psychology
        fields = ('effect',)


class CorruptionAndMutationForm(forms.ModelForm):
    class Meta:
        model = CorruptionAndMutation
        fields = ('effect',)


class WoundsForm(forms.ModelForm):
    class Meta:
        model = Wounds
        fields = ('sb', 'tb_x2', 'wbp', 'hardy', 'wounds')


class SinForm(forms.ModelForm):
    class Meta:
        model = Sin
        fields = ('sin',)
