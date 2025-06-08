from django import forms
from .models import CharacterMeleeWeapons, MeleeWeapons


class CharacterMeleeWeaponsCreateForm(forms.ModelForm):
    """Form for creation of CharacterMeleeWeapons row."""
    melee_weapon = forms.ModelChoiceField(
        queryset=MeleeWeapons.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Weapon"
    )

    class Meta:
        model = CharacterMeleeWeapons
        fields = ("melee_weapon", "quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterMeleeWeaponsUpdateForm(forms.ModelForm):
    """Form for update of CharacterMeleeWeapons row. MeleeWeaponID is not possible to change."""
    class Meta:
        model = CharacterMeleeWeapons
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }