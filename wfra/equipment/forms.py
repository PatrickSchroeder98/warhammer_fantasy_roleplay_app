from django import forms
from .models import MeleeWeapons, RangedWeapons, Ammunition, Armour, CharacterMeleeWeapons, CharacterRangedWeapons, CharacterAmmunition, CharacterArmour


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
                    "Character already has this melee weapon. Increase the quantity in equipment to add another item of this type."
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


class CharacterRangedWeaponsCreateForm(forms.ModelForm):
    """Form for creation of CharacterRangedWeapons row."""

    ranged_weapon = forms.ModelChoiceField(
        queryset=RangedWeapons.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="RangedWeapon",
    )

    class Meta:
        model = CharacterRangedWeapons
        fields = ("ranged_weapon", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen ranged weapon, raises error if it exists."""
        cleaned_data = super().clean()
        ranged_weapon = cleaned_data.get("ranged_weapon")

        if self.character and ranged_weapon:
            exists = CharacterRangedWeapons.objects.filter(
                character=self.character, ranged_weapon=ranged_weapon
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this ranged weapon. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterRangedWeaponsUpdateForm(forms.ModelForm):
    """Form for update of CharacterRangedWeapons row. RangedWeaponID is not possible to change."""

    class Meta:
        model = CharacterRangedWeapons
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterAmmunitionCreateForm(forms.ModelForm):
    """Form for creation of CharacterAmmunition row."""

    ammunition = forms.ModelChoiceField(
        queryset=Ammunition.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Ammunition",
    )

    class Meta:
        model = CharacterAmmunition
        fields = ("ammunition", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen ammunition, raises error if it exists."""
        cleaned_data = super().clean()
        ammunition = cleaned_data.get("ammunition")

        if self.character and ammunition:
            exists = CharacterAmmunition.objects.filter(
                character=self.character, ammunition=ammunition
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this ammunition. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterAmmunitionUpdateForm(forms.ModelForm):
    """Form for update of CharacterAmmunition row. AmmunitionID is not possible to change."""

    class Meta:
        model = CharacterAmmunition
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterArmourCreateForm(forms.ModelForm):
    """Form for creation of CharacterArmour row."""

    armour = forms.ModelChoiceField(
        queryset=Armour.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Armour",
    )

    class Meta:
        model = CharacterArmour
        fields = ("armour", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen armour, raises error if it exists."""
        cleaned_data = super().clean()
        armour = cleaned_data.get("armour")

        if self.character and armour:
            exists = CharacterArmour.objects.filter(
                character=self.character, armour=armour
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this armour. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterArmourUpdateForm(forms.ModelForm):
    """Form for update of CharacterArmour row. AmmunitionID is not possible to change."""

    class Meta:
        model = CharacterArmour
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
