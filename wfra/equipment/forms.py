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


class CharacterPacksAndContainersUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of PacksAndContainers row. PacksAndContainersID is not possible to change."""

    class Meta:
        model = CharacterPacksAndContainers
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterClothingAndAccessoriesCreateForm(CharacterEquipmentCreateForm):
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


class CharacterClothingAndAccessoriesUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of ClothingAndAccessories row. ClothingAndAccessoriesID is not possible to change."""

    class Meta:
        model = CharacterClothingAndAccessories
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterFoodDrinkAndLodgingCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of FoodDrinkAndLodging row."""

    food_drink_and_lodging = forms.ModelChoiceField(
        queryset=FoodDrinkAndLodging.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="FoodDrinkAndLodging",
    )

    class Meta:
        model = CharacterFoodDrinkAndLodging
        fields = ("food_drink_and_lodging", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen food, raises error if it exists."""
        cleaned_data = super().clean()
        food_drink_and_lodging = cleaned_data.get("food_drink_and_lodging")

        if self.character and food_drink_and_lodging:
            exists = CharacterFoodDrinkAndLodging.objects.filter(
                character=self.character, food_drink_and_lodging=food_drink_and_lodging
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this food, drink or lodging. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterFoodDrinkAndLodgingUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of FoodDrinkAndLodging row. FoodDrinkAndLodgingID is not possible to change."""

    class Meta:
        model = CharacterFoodDrinkAndLodging
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterToolsAndKitsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of ToolsAndKits row."""

    tools_and_kits = forms.ModelChoiceField(
        queryset=ToolsAndKits.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="ToolsAndKits",
    )

    class Meta:
        model = CharacterToolsAndKits
        fields = ("tools_and_kits", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen tool, raises error if it exists."""
        cleaned_data = super().clean()
        tools_and_kits = cleaned_data.get("tools_and_kits")

        if self.character and tools_and_kits:
            exists = CharacterToolsAndKits.objects.filter(
                character=self.character, tools_and_kits=tools_and_kits
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this tool or kit. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterToolsAndKitsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of ToolsAndKits row. ToolsAndKitsID is not possible to change."""

    class Meta:
        model = CharacterToolsAndKits
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterBooksAndDocumentsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of BooksAndDocuments row."""

    books_and_documents = forms.ModelChoiceField(
        queryset=BooksAndDocuments.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="BooksAndDocuments",
    )

    class Meta:
        model = CharacterBooksAndDocuments
        fields = ("books_and_documents", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen book, raises error if it exists."""
        cleaned_data = super().clean()
        books_and_documents = cleaned_data.get("books_and_documents")

        if self.character and books_and_documents:
            exists = CharacterBooksAndDocuments.objects.filter(
                character=self.character, books_and_documents=books_and_documents
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this book or document. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterBooksAndDocumentsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of BooksAndDocuments row. BooksAndDocumentsID is not possible to change."""

    class Meta:
        model = CharacterBooksAndDocuments
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterTradeToolsAndWorkshopsCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of TradeToolsAndWorkshops row."""

    trade_tools_and_workshops = forms.ModelChoiceField(
        queryset=TradeToolsAndWorkshops.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="TradeToolsAndWorkshops",
    )

    class Meta:
        model = CharacterTradeToolsAndWorkshops
        fields = ("trade_tools_and_workshops", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen tool, raises error if it exists."""
        cleaned_data = super().clean()
        trade_tools_and_workshops = cleaned_data.get("trade_tools_and_workshops")

        if self.character and trade_tools_and_workshops:
            exists = CharacterTradeToolsAndWorkshops.objects.filter(
                character=self.character, trade_tools_and_workshops=trade_tools_and_workshops
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this trade tool or workshop. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterTradeToolsAndWorkshopsUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of TradeToolsAndWorkshops row. TradeToolsAndWorkshopsID is not possible to change."""

    class Meta:
        model = CharacterTradeToolsAndWorkshops
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CharacterAnimalsAndVehiclesCreateForm(CharacterEquipmentCreateForm):
    """Form for creation of AnimalsAndVehicles row."""

    animals_and_vehicles = forms.ModelChoiceField(
        queryset=AnimalsAndVehicles.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="AnimalsAndVehicles",
    )

    class Meta:
        model = CharacterAnimalsAndVehicles
        fields = ("animals_and_vehicles", "quantity", "equipped")

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
        """Method checks if there is a duplicate of chosen animal or vehicle, raises error if it exists."""
        cleaned_data = super().clean()
        animals_and_vehicles = cleaned_data.get("animals_and_vehicles")

        if self.character and animals_and_vehicles:
            exists = CharacterAnimalsAndVehicles.objects.filter(
                character=self.character, animals_and_vehicles=animals_and_vehicles
            ).exists()

            if exists and not self.instance.pk:
                raise forms.ValidationError(
                    "Character already has this animal or vehicle. Increase the quantity in equipment to add another item of this type."
                )

        return cleaned_data


class CharacterAnimalsAndVehiclesUpdateForm(CharacterEquipmentUpdateForm):
    """Form for update of AnimalsAndVehicles row. AnimalsAndVehiclesID is not possible to change."""

    class Meta:
        model = CharacterAnimalsAndVehicles
        fields = ("quantity", "equipped")

        widgets = {
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "equipped": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


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
