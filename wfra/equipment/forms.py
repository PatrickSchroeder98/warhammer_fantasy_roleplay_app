from django import forms
from .models import CharacterMeleeWeapons


class CharacterMeleeWeaponsForm(forms.ModelForm):
    class Meta:
        model = CharacterMeleeWeapons
        fields = ("quantity", "equipped", "melee_weapon")  # Only editable fields

        widgets = {
            "melee_weapon": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Weapon ID"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Quantity"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

        labels = {
            "quantity": "Quantity",
            "equipped": "Equipped",
            "melee_weapon": "Weapon ID",
        }
