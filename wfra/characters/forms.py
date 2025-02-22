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
    """Form with basic information about character."""

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
            "age": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Character Age"}
            ),
            "height": forms.NumberInput(
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
    """Form with fields from characteristics model."""

    # # Alternative way to disable the fields - unsupported, because user should see the value
    # WS_current = forms.IntegerField(disabled=True, required=False)
    # BS_current = forms.IntegerField(disabled=True, required=False)
    # S_current = forms.IntegerField(disabled=True, required=False)
    # T_current = forms.IntegerField(disabled=True, required=False)
    # I_current = forms.IntegerField(disabled=True, required=False)
    # Ag_current = forms.IntegerField(disabled=True, required=False)
    # Dex_current = forms.IntegerField(disabled=True, required=False)
    # Int_current = forms.IntegerField(disabled=True, required=False)
    # WP_current = forms.IntegerField(disabled=True, required=False)
    # Fel_current = forms.IntegerField(disabled=True, required=False)

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
                attrs={
                    "class": "form-control",
                    "placeholder": "Initial Ballistic Skill",
                }
            ),
            "BS_advances": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Advances Ballistic Skill",
                }
            ),
            "BS_current": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Current Ballistic Skill",
                }
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
    """Form with fields from fate model."""

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
    """Form with fields from resilience model."""

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
            "motivation": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Motivation"}
            ),
        }

        labels = {
            "resilience": "Resilience Points",
            "resolve": "Resolve Points",
            "motivation": "Motivation",
        }


class ExperienceForm(forms.ModelForm):
    """Form with fields from experience model."""

    class Meta:
        model = Experience
        fields = ("current", "spent", "total")

        widgets = {
            "current": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Current Experience Points",
                }
            ),
            "spent": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Spent Experience Points",
                }
            ),
            "total": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Total Experience Points",
                }
            ),
        }

        labels = {
            "current": "Current Experience Points",
            "spent": "Spent Experience Points",
            "total": "Total Experience Points",
        }


class MovementForm(forms.ModelForm):
    """Form with fields from movement model."""

    class Meta:
        model = Movement
        fields = ("movement", "walk", "run")

        widgets = {
            "movement": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Movement Speed"}
            ),
            "walk": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Walk Speed"}
            ),
            "run": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Run Speed"}
            ),
        }

        labels = {
            "movement": "Movement Speed",
            "walk": "Walk Speed",
            "run": "Run Speed",
        }


class BasicSkillsForm(forms.ModelForm):
    """Form with fields from basic skills model."""

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

        widgets = {
            field_name: forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": field_name.replace("_", " ").capitalize(),
                }
            )
            for field_name in fields
        }

        labels = {
            "art_characteristics": "Art Characteristics",
            "art_advances": "Art Advances",
            "art_skill": "Art Skill",
            "athletics_characteristics": "Athletics Characteristics",
            "athletics_advances": "Athletics Advances",
            "athletics_skill": "Athletics Skill",
            "bribery_characteristics": "Bribery Characteristics",
            "bribery_advances": "Bribery Advances",
            "bribery_skill": "Bribery Skill",
            "charm_characteristics": "Charm Characteristics",
            "charm_advances": "Charm Advances",
            "charm_skill": "Charm Skill",
            "charm_animal_characteristics": "Charm Animal Characteristics",
            "charm_animal_advances": "Charm Animal Advances",
            "charm_animal_skill": "Charm Animal Skill",
            "climb_characteristics": "Climb Characteristics",
            "climb_advances": "Climb Advances",
            "climb_skill": "Climb Skill",
            "cool_characteristics": "Cool Characteristics",
            "cool_advances": "Cool Advances",
            "cool_skill": "Cool Skill",
            "consume_alcohol_characteristics": "Consume Alcohol Characteristics",
            "consume_alcohol_advances": "Consume Alcohol Advances",
            "consume_alcohol_skill": "Consume Alcohol Skill",
            "dodge_characteristics": "Dodge Characteristics",
            "dodge_advances": "Dodge Advances",
            "dodge_skill": "Dodge Skill",
            "drive_characteristics": "Drive Characteristics",
            "drive_advances": "Drive Advances",
            "drive_skill": "Drive Skill",
            "endurance_characteristics": "Endurance Characteristics",
            "endurance_advances": "Endurance Advances",
            "endurance_skill": "Endurance Skill",
            "entertain_characteristics": "Entertain Characteristics",
            "entertain_advances": "Entertain Advances",
            "entertain_skill": "Entertain Skill",
            "gamble_characteristics": "Gamble Characteristics",
            "gamble_advances": "Gamble Advances",
            "gamble_skill": "Gamble Skill",
            "gossip_characteristics": "Gossip Characteristics",
            "gossip_advances": "Gossip Advances",
            "gossip_skill": "Gossip Skill",
            "haggle_characteristics": "Haggle Characteristics",
            "haggle_advances": "Haggle Advances",
            "haggle_skill": "Haggle Skill",
            "intimidate_characteristics": "Intimidate Characteristics",
            "intimidate_advances": "Intimidate Advances",
            "intimidate_skill": "Intimidate Skill",
            "intuition_characteristics": "Intuition Characteristics",
            "intuition_advances": "Intuition Advances",
            "intuition_skill": "Intuition Skill",
            "leadership_characteristics": "Leadership Characteristics",
            "leadership_advances": "Leadership Advances",
            "leadership_skill": "Leadership Skill",
            "melee_basic_characteristics": "Melee Basic Characteristics",
            "melee_basic_advances": "Melee Basic Advances",
            "melee_basic_skill": "Melee Basic Skill",
            "melee_characteristics": "Melee Characteristics",
            "melee_advances": "Melee Advances",
            "melee_skill": "Melee Skill",
            "navigation_characteristics": "Navigation Characteristics",
            "navigation_advances": "Navigation Advances",
            "navigation_skill": "Navigation Skill",
            "outdoor_survival_characteristics": "Outdoor Survival Characteristics",
            "outdoor_survival_advances": "Outdoor Survival Advances",
            "outdoor_survival_skill": "Outdoor Survival Skill",
            "perception_characteristics": "Perception Characteristics",
            "perception_advances": "Perception Advances",
            "perception_skill": "Perception Skill",
            "ride_characteristics": "Ride Characteristics",
            "ride_advances": "Ride Advances",
            "ride_skill": "Ride Skill",
            "row_characteristics": "Row Characteristics",
            "row_advances": "Row Advances",
            "row_skill": "Row Skill",
            "stealth_characteristics": "Stealth Characteristics",
            "stealth_advances": "Stealth Advances",
            "stealth_skill": "Stealth Skill",
        }


class AdvancedSkillsForm(forms.ModelForm):
    """Form with fields from advanced skills model."""

    class Meta:
        model = AdvancedSkills
        fields = ("name", "attribute_name", "attribute_value", "advances", "total")

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Advanced Skill Name"}
            ),
            "attribute_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Attribute Name"}
            ),
            "attribute_value": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Attribute Value"}
            ),
            "advances": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Advances"}
            ),
            "total": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Total Value"}
            ),
        }

        labels = {
            "name": "Advanced Skill Name",
            "attribute_name": "Attribute Name",
            "attribute_value": "Attribute Value",
            "advances": "Advances",
            "total": "Total Value",
        }


class TalentsForm(forms.ModelForm):
    """Form with fields from talents model."""

    class Meta:
        model = Talents
        fields = ("talent", "times_taken", "description")

        widgets = {
            "talent": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Talent Name"}
            ),
            "times_taken": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Times Taken"}
            ),
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Talent Description"}
            ),
        }

        labels = {
            "talent": "Talent Name",
            "times_taken": "Times Taken",
            "description": "Talent Description",
        }


class AmbitionsForm(forms.ModelForm):
    """Form with fields from ambitions model."""

    class Meta:
        model = Ambitions
        fields = ("short_term", "long_term")

        widgets = {
            "short_term": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Short Term Ambition"}
            ),
            "long_term": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Long Term Ambition"}
            ),
        }

        labels = {
            "short_term": "Short Term Ambition",
            "long_term": "Long Term Ambition",
        }


class PartyForm(forms.ModelForm):
    """Form with fields from ambitions model."""

    class Meta:
        model = Party
        fields = ("party_name", "short_term", "long_term", "members")

        widgets = {
            "party_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Party Name"}
            ),
            "short_term": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Short Term Party Ambition",
                }
            ),
            "long_term": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Long Term Party Ambition",
                }
            ),
            "members": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Party Members"}
            ),
        }

        labels = {
            "party_name": "Party Name",
            "short_term": "Short Term Party Ambition",
            "long_term": "Long Term Party Ambition",
            "members": "Party Members",
        }


class PsychologyForm(forms.ModelForm):
    """Form with field from psychology model."""

    class Meta:
        model = Psychology
        fields = ("effect",)

        widgets = {
            "effect": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Psychology Effects"}
            ),
        }

        labels = {
            "effect": "Psychology Effects",
        }


class CorruptionAndMutationForm(forms.ModelForm):
    """Form with field from corruption and mutation model."""

    class Meta:
        model = CorruptionAndMutation
        fields = ("effect",)

        widgets = {
            "effect": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Corruption And Mutation Effects",
                }
            ),
        }

        labels = {
            "effect": "Corruption And Mutation Effects",
        }


class WoundsForm(forms.ModelForm):
    """Form with fields from wounds model."""

    class Meta:
        model = Wounds
        fields = ("sb", "tb_x2", "wbp", "hardy", "wounds")

        widgets = {
            "sb": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Strength Bonus"}
            ),
            "tb_x2": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Toughness Bonus x2"}
            ),
            "wbp": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Willpower Bonus"}
            ),
            "hardy": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Hardy Skill"}
            ),
            "wounds": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Number Of Wounds (Health)",
                }
            ),
        }

        labels = {
            "sb": "Strength Bonus",
            "tb_x2": "Toughness Bonus x2",
            "wbp": "Willpower Bonus",
            "hardy": "Hardy Skill",
            "wounds": "Number Of Wounds (Health)",
        }


class SinForm(forms.ModelForm):
    """Form with field from sin model."""

    class Meta:
        model = Sin
        fields = ("sin",)

        widgets = {
            "sin": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Sin Points"}
            ),
        }

        labels = {
            "sin": "Sin Points",
        }
