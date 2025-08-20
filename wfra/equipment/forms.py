from django import forms
from .models import (
    MeleeWeapons,
    RangedWeapons,
    Ammunition,
    Armour,
    PacksAndContainers,
    ClothingAndAccessories,
    FoodDrinkAndLodging,
    ToolsAndKits,
    BooksAndDocuments,
    TradeToolsAndWorkshops,
    AnimalsAndVehicles,
    DrugsAndPoisons,
    HerbsAndDraughts,
    Prosthetics,
    Hirelings,
    MiscellaneousTrappings,
    CharacterMeleeWeapons,
    CharacterRangedWeapons,
    CharacterAmmunition,
    CharacterArmour,
    CharacterPacksAndContainers,
    CharacterClothingAndAccessories,
    CharacterFoodDrinkAndLodging,
    CharacterToolsAndKits,
    CharacterBooksAndDocuments,
    CharacterTradeToolsAndWorkshops,
    CharacterAnimalsAndVehicles,
    CharacterDrugsAndPoisons,
    CharacterHerbsAndDraughts,
    CharacterProsthetics,
    CharacterMiscellaneousTrappings,
    CharacterHirelings
)


class CharacterEquipmentCreateForm(forms.ModelForm):
    """Base form for creating character equipment."""

    fk_field = None  # e.g., "melee_weapon"
    fk_model = None  # e.g., MeleeWeapons

    def __init__(self, *args, **kwargs):
        self.character = kwargs.pop("character", None)
        super().__init__(*args, **kwargs)

        # Dynamically add the FK choice field
        if self.fk_field and self.fk_model:
            self.fields[self.fk_field] = forms.ModelChoiceField(
                queryset=self.fk_model.objects.all(),
                widget=forms.Select(attrs={"class": "form-control"}),
                label=self.fk_field.replace("_", " ").title(),
            )

    def clean(self):
        cleaned_data = super().clean()
        fk_value = cleaned_data.get(self.fk_field)

        if self.character and fk_value:
            exists = self._meta.model.objects.filter(
                character=self.character,
                **{self.fk_field: fk_value}
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    f"Character already has this {self.fk_field.replace('_', ' ')}. "
                    f"Increase the quantity instead."
                )

        return cleaned_data

    class Meta:
        fields = ("quantity", "equipped")
        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "equipped": "Equipped",
        }


class CharacterEquipmentUpdateForm(forms.ModelForm):
    """Base form for updating character equipment (FK field not editable)."""

    class Meta:
        fields = ("quantity", "equipped")
        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterMeleeWeaponsCreateForm(CharacterEquipmentCreateForm):
    fk_field = "melee_weapon"
    fk_model = MeleeWeapons

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterMeleeWeapons
        fields = CharacterEquipmentCreateForm.Meta.fields + ("melee_weapon",)


class CharacterMeleeWeaponsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of CharacterMeleeWeapons row. CharacterMeleeWeaponsID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterMeleeWeapons


class CharacterRangedWeaponsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of CharacterRangedWeapons row."""

    fk_field = "ranged_weapon"
    fk_model = RangedWeapons

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterRangedWeapons
        fields = CharacterEquipmentCreateForm.Meta.fields + ("ranged_weapon",)


class CharacterRangedWeaponsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of CharacterRangedWeapons row. CharacterRangedWeaponsID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterRangedWeapons


class CharacterAmmunitionCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of CharacterAmmunition row."""
    fk_field = "ammunition"
    fk_model = Ammunition

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterAmmunition
        fields = CharacterEquipmentCreateForm.Meta.fields + ("ammunition",)


class CharacterAmmunitionUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of CharacterAmmunition row. AmmunitionID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterAmmunition


class CharacterArmourCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of CharacterArmour row."""

    fk_field = "armour"
    fk_model = Armour

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterArmour
        fields = CharacterEquipmentCreateForm.Meta.fields + ("armour",)


class CharacterArmourUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of CharacterArmour row. AmmunitionID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterArmour


class CharacterPacksAndContainersCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of PacksAndContainers row."""

    fk_field = "packs_and_containers"
    fk_model = PacksAndContainers

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterPacksAndContainers
        fields = CharacterEquipmentCreateForm.Meta.fields + ("packs_and_containers",)


class CharacterPacksAndContainersUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of PacksAndContainers row. PacksAndContainersID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterPacksAndContainers


class CharacterClothingAndAccessoriesCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of ClothingAndAccessories row."""

    fk_field = "clothing_and_accessories"
    fk_model = ClothingAndAccessories

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterClothingAndAccessories
        fields = CharacterEquipmentCreateForm.Meta.fields + ("clothing_and_accessories",)


class CharacterClothingAndAccessoriesUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of ClothingAndAccessories row. ClothingAndAccessoriesID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterClothingAndAccessories


class CharacterFoodDrinkAndLodgingCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of FoodDrinkAndLodging row."""

    fk_field = "food_drink_and_lodging"
    fk_model = FoodDrinkAndLodging

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterFoodDrinkAndLodging
        fields = CharacterEquipmentCreateForm.Meta.fields + ("food_drink_and_lodging",)


class CharacterFoodDrinkAndLodgingUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of FoodDrinkAndLodging row. FoodDrinkAndLodgingID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterFoodDrinkAndLodging


class CharacterToolsAndKitsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of ToolsAndKits row."""

    fk_field = "tools_and_kits"
    fk_model = ToolsAndKits

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterToolsAndKits
        fields = CharacterEquipmentCreateForm.Meta.fields + ("tools_and_kits",)


class CharacterToolsAndKitsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of ToolsAndKits row. ToolsAndKitsID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterToolsAndKits


class CharacterBooksAndDocumentsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of BooksAndDocuments row."""

    fk_field = "books_and_documents"
    fk_model = BooksAndDocuments

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterBooksAndDocuments
        fields = CharacterEquipmentCreateForm.Meta.fields + ("books_and_documents",)


class CharacterBooksAndDocumentsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of BooksAndDocuments row. BooksAndDocumentsID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterBooksAndDocuments


class CharacterTradeToolsAndWorkshopsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of TradeToolsAndWorkshops row."""

    fk_field = "trade_tools_and_workshops"
    fk_model = TradeToolsAndWorkshops

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterTradeToolsAndWorkshops
        fields = CharacterEquipmentCreateForm.Meta.fields + ("trade_tools_and_workshops",)


class CharacterTradeToolsAndWorkshopsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of TradeToolsAndWorkshops row. TradeToolsAndWorkshopsID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterTradeToolsAndWorkshops


class CharacterAnimalsAndVehiclesCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of AnimalsAndVehicles row."""

    fk_field = "animal_and_vehicles"
    fk_model = AnimalsAndVehicles

    class Meta(CharacterEquipmentCreateForm.Meta):
        model = CharacterAnimalsAndVehicles
        fields = CharacterEquipmentCreateForm.Meta.fields + ("animal_and_vehicles",)


class CharacterAnimalsAndVehiclesUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of AnimalsAndVehicles row. AnimalsAndVehiclesID is not possible to change."""

    class Meta(CharacterEquipmentUpdateForm.Meta):
        model = CharacterAnimalsAndVehicles


class CharacterDrugsAndPoisonsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of DrugsAndPoisons row."""

    drugs_and_poisons = forms.ModelChoiceField(
        queryset=DrugsAndPoisons.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="DrugsAndPoisons",
    )

    class Meta:
        model = CharacterDrugsAndPoisons
        fields = ("drugs_and_poisons", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen drug or poison, raises error if it exists."""
        cleaned_data = super().clean()
        drugs_and_poisons = cleaned_data.get("drugs_and_poisons")

        if self.character and drugs_and_poisons:
            exists = CharacterDrugsAndPoisons.objects.filter(
                character=self.character, drugs_and_poisons=drugs_and_poisons
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this drug or poison. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterDrugsAndPoisonsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of DrugsAndPoisons row. DrugsAndPoisonsID is not possible to change."""

    class Meta:
        model = CharacterDrugsAndPoisons
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterHerbsAndDraughtsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of HerbsAndDraughts row."""

    herbs_and_draughts = forms.ModelChoiceField(
        queryset=HerbsAndDraughts.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="HerbsAndDraughts",
    )

    class Meta:
        model = CharacterHerbsAndDraughts
        fields = ("herbs_and_draughts", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen herb or draught, raises error if it exists."""
        cleaned_data = super().clean()
        herbs_and_draughts = cleaned_data.get("herbs_and_draughts")

        if self.character and herbs_and_draughts:
            exists = CharacterHerbsAndDraughts.objects.filter(
                character=self.character, herbs_and_draughts=herbs_and_draughts
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this herb or draught. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterHerbsAndDraughtsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of HerbsAndDraughts row. HerbsAndDraughtsID is not possible to change."""

    class Meta:
        model = CharacterHerbsAndDraughts
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterProstheticsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of Prosthetics row."""

    prosthetics = forms.ModelChoiceField(
        queryset=Prosthetics.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Prosthetics",
    )

    class Meta:
        model = CharacterProsthetics
        fields = ("prosthetics", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen prosthetics, raises error if it exists."""
        cleaned_data = super().clean()
        prosthetics = cleaned_data.get("prosthetics")

        if self.character and prosthetics:
            exists = CharacterProsthetics.objects.filter(
                character=self.character, prosthetics=prosthetics
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this prosthetics. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterProstheticsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of Prosthetics row. ProstheticsID is not possible to change."""

    class Meta:
        model = CharacterProsthetics
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterMiscellaneousTrappingsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of MiscellaneousTrappings row."""

    miscellaneous_trappings = forms.ModelChoiceField(
        queryset=MiscellaneousTrappings.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="MiscellaneousTrappings",
    )

    class Meta:
        model = CharacterMiscellaneousTrappings
        fields = ("miscellaneous_trappings", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen miscellaneous trapping, raises error if it exists."""
        cleaned_data = super().clean()
        miscellaneous_trappings = cleaned_data.get("miscellaneous_trappings")

        if self.character and miscellaneous_trappings:
            exists = CharacterMiscellaneousTrappings.objects.filter(
                character=self.character, miscellaneous_trappings=miscellaneous_trappings
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this miscellaneous trapping. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterMiscellaneousTrappingsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of MiscellaneousTrappings row. MiscellaneousTrappingsID is not possible to change."""

    class Meta:
        model = CharacterMiscellaneousTrappings
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterHirelingsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of Hirelings row."""

    hirelings = forms.ModelChoiceField(
        queryset=Hirelings.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Hirelings",
    )

    class Meta:
        model = CharacterHirelings
        fields = ("hirelings", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen hireling, raises error if it exists."""
        cleaned_data = super().clean()
        hirelings = cleaned_data.get("hirelings")

        if self.character and hirelings:
            exists = CharacterHirelings.objects.filter(
                character=self.character, hirelings=hirelings
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this hireling. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterHirelingsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of Hirelings row. HirelingsID is not possible to change."""

    class Meta:
        model = CharacterHirelings
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
