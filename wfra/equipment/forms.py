from django import forms
from .models import (
    MeleeWeapons,
    RangedWeapons,
    Ammunition,
    Armour,
    PacksAndContainers,
    ClothingAndAccessories,
    CharacterMeleeWeapons,
    CharacterRangedWeapons,
    CharacterAmmunition,
    CharacterArmour,
    CharacterPacksAndContainers,
    CharacterClothingAndAccessories,
)


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


class CharacterPacksAndContainersCreateForm(forms.ModelForm):
    """Form for creation of PacksAndContainers row."""

    packs_and_containers = forms.ModelChoiceField(
        queryset=PacksAndContainers.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="PacksAndContainers",
    )

    class Meta:
        model = CharacterPacksAndContainers
        fields = ("packs_and_containers", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen container, raises error if it exists."""
        cleaned_data = super().clean()
        packs_and_containers = cleaned_data.get("packs_and_containers")

        if self.character and packs_and_containers:
            exists = CharacterPacksAndContainers.objects.filter(
                character=self.character, packs_and_containers=packs_and_containers
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this container. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterPacksAndContainersUpdateForm(forms.ModelForm):
    """Form for update of PacksAndContainers row. PacksAndContainersID is not possible to change."""

    class Meta:
        model = CharacterPacksAndContainers
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterClothingAndAccessoriesCreateForm(forms.ModelForm):
    """Form for creation of ClothingAndAccessories row."""

    clothing_and_accessories = forms.ModelChoiceField(
        queryset=ClothingAndAccessories.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="ClothingAndAccessories",
    )

    class Meta:
        model = CharacterClothingAndAccessories
        fields = ("clothing_and_accessories", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen clothing, raises error if it exists."""
        cleaned_data = super().clean()
        clothing_and_accessories = cleaned_data.get("clothing_and_accessories")

        if self.character and clothing_and_accessories:
            exists = CharacterClothingAndAccessories.objects.filter(
                character=self.character, clothing_and_accessories=clothing_and_accessories
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this clothing. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterClothingAndAccessoriesUpdateForm(forms.ModelForm):
    """Form for update of ClothingAndAccessories row. ClothingAndAccessoriesID is not possible to change."""

    class Meta:
        model = CharacterClothingAndAccessories
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
