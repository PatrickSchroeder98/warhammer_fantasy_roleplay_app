from django import forms
from .models import CharacterMeleeWeapons, MeleeWeapons


class CharacterMeleeWeaponsCreateForm(forms.ModelForm):
    """Form for creation of CharacterMeleeWeapons row."""

    melee_weapon = forms.ModelChoiceField(
        queryset=MeleeWeapons.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Weapon",
    )

    class Meta:
        model = CharacterMeleeWeapons
        fields = ("melee_weapon", "quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

        labels = {
            "equipped": "Equipped",
        }

    def __init__(self, *args, **kwargs):
        """Accepts a character instance to filter during validation"""
        self.character = kwargs.pop("character", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        """Method checks if there is a duplicate of chosen melee weapon, raises error if it exists."""
        cleaned_data = super().clean()
        melee_weapon = cleaned_data.get("melee_weapon")

        if self.character and melee_weapon:
            exists = CharacterMeleeWeapons.objects.filter(
                character=self.character, melee_weapon=melee_weapon
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "This character already has this melee weapon. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterMeleeWeaponsUpdateForm(forms.ModelForm):
    """Form for update of CharacterMeleeWeapons row. MeleeWeaponID is not possible to change."""

    class Meta:
        model = CharacterMeleeWeapons
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
