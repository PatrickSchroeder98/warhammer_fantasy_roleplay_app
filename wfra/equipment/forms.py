from django import forms
from .models import CharacterMeleeWeapons


class CharacterMeleeWeaponsForm(forms.ModelForm):
    class Meta:
        model = CharacterMeleeWeapons
        fields = ("quantity", "equipped")  # Only editable fields

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Quantity"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

        labels = {
            "quantity": "Quantity",
            "equipped": "Equipped",
        }