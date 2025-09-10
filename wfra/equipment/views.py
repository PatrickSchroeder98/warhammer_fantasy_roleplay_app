from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from characters.models import Characters
from .models import (
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
    CharacterHirelings,
)
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
    MiscellaneousTrappings,
    Hirelings,
)
from .forms import (
    CharacterMeleeWeaponsCreateForm,
    CharacterMeleeWeaponsUpdateForm,
    CharacterRangedWeaponsCreateForm,
    CharacterRangedWeaponsUpdateForm,
    CharacterAmmunitionCreateForm,
    CharacterAmmunitionUpdateForm,
    CharacterArmourCreateForm,
    CharacterArmourUpdateForm,
    CharacterPacksAndContainersCreateForm,
    CharacterPacksAndContainersUpdateForm,
    CharacterClothingAndAccessoriesCreateForm,
    CharacterClothingAndAccessoriesUpdateForm,
    CharacterFoodDrinkAndLodgingCreateForm,
    CharacterFoodDrinkAndLodgingUpdateForm,
    CharacterToolsAndKitsCreateForm,
    CharacterToolsAndKitsUpdateForm,
    CharacterBooksAndDocumentsCreateForm,
    CharacterBooksAndDocumentsUpdateForm,
    CharacterTradeToolsAndWorkshopsCreateForm,
    CharacterTradeToolsAndWorkshopsUpdateForm,
    CharacterAnimalsAndVehiclesCreateForm,
    CharacterAnimalsAndVehiclesUpdateForm,
    CharacterDrugsAndPoisonsCreateForm,
    CharacterDrugsAndPoisonsUpdateForm,
    CharacterHerbsAndDraughtsCreateForm,
    CharacterHerbsAndDraughtsUpdateForm,
    CharacterProstheticsCreateForm,
    CharacterProstheticsUpdateForm,
    CharacterMiscellaneousTrappingsCreateForm,
    CharacterMiscellaneousTrappingsUpdateForm,
    CharacterHirelingsCreateForm,
    CharacterHirelingsUpdateForm
)


class CharacterEquipmentView(View):
    """View for equipment of given character."""

    def get(self, request, character_id):
        """Method creates contexts of all equipment types for a given character, then returns the template."""
        character = get_object_or_404(Characters, pk=character_id)

        melee_weapons = CharacterMeleeWeapons.objects.filter(character=character)
        ranged_weapons = CharacterRangedWeapons.objects.filter(character=character)
        ammunition = CharacterAmmunition.objects.filter(character=character)
        armour = CharacterArmour.objects.filter(character=character)
        packs_and_containers = CharacterPacksAndContainers.objects.filter(
            character=character
        )
        clothing_and_accessories = CharacterClothingAndAccessories.objects.filter(
            character=character
        )
        food_drink_and_lodging = CharacterFoodDrinkAndLodging.objects.filter(
            character=character
        )
        tools_and_kits = CharacterToolsAndKits.objects.filter(character=character)
        books_and_documents = CharacterBooksAndDocuments.objects.filter(
            character=character
        )
        trade_tools_and_workshops = CharacterTradeToolsAndWorkshops.objects.filter(
            character=character
        )
        animals_and_vehicles = CharacterAnimalsAndVehicles.objects.filter(
            character=character
        )
        drugs_and_poisons = CharacterDrugsAndPoisons.objects.filter(character=character)
        herbs_and_draughts = CharacterHerbsAndDraughts.objects.filter(
            character=character
        )
        prosthetics = CharacterProsthetics.objects.filter(character=character)
        miscellaneous_trappings = CharacterMiscellaneousTrappings.objects.filter(
            character=character
        )
        hirelings = CharacterHirelings.objects.filter(character=character)

        context = {
            "character": character,
            "melee_weapons": melee_weapons,
            "ranged_weapons": ranged_weapons,
            "ammunition": ammunition,
            "armour": armour,
            "packs_and_containers": packs_and_containers,
            "clothing_and_accessories": clothing_and_accessories,
            "food_drink_and_lodging": food_drink_and_lodging,
            "tools_and_kits": tools_and_kits,
            "books_and_documents": books_and_documents,
            "trade_tools_and_workshops": trade_tools_and_workshops,
            "animals_and_vehicles": animals_and_vehicles,
            "drugs_and_poisons": drugs_and_poisons,
            "herbs_and_draughts": herbs_and_draughts,
            "prosthetics": prosthetics,
            "miscellaneous_trappings": miscellaneous_trappings,
            "hirelings": hirelings,
        }
        return render(request, "equipment/character_equipment.html", context)


class CharacterEquipmentCreateView(LoginRequiredMixin, CreateView):
    """Generic create view for character equipment."""

    template_name = "equipment/character_equipment_form.html"

    category_title = None
    field_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_title"] = self.category_title
        context["field_name"] = self.field_name
        context["character_id"] = self.kwargs.get("character_id")

        if self.field_name and "form" in context:
            context["main_field"] = context["form"][self.field_name]

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(Characters, pk=character_id, user=self.request.user)
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(Characters, pk=character_id, user=self.request.user)
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CharacterEquipmentUpdateView(LoginRequiredMixin, UpdateView):
    """Generic update view for character equipment."""

    def get_queryset(self):
        return self.model.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class CharacterEquipmentDeleteView(LoginRequiredMixin, DeleteView):
    """Generic delete view for character equipment."""

    template_name = "equipment/character_equipment_confirm_delete.html"

    def get_queryset(self):
        return super().get_queryset().filter(character__user=self.request.user)

    def get_context_data(self, **kwargs):
        """Gives access to _meta fields through context."""

        context = super().get_context_data(**kwargs)
        obj = self.object

        context["category_title"] = obj._meta.verbose_name.title()

        context["cancel_url"] = reverse(
            "equipment:character_equipment",
            kwargs={"character_id": obj.character_id},
        )
        return context

    def get_success_url(self):
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )

    def delete(self, *args, **kwargs):
        messages.success(self.request, f"{self.model._meta.verbose_name.title()} deleted.")
        return super().delete(*args, **kwargs)


class CreateViewCharacterMeleeWeapons(CharacterEquipmentCreateView):
    """Create view for characters' melee weapon."""
    model = CharacterMeleeWeapons
    form_class = CharacterMeleeWeaponsCreateForm
    category_title = "Melee Weapon"
    field_name = "melee_weapon"
    #template_name = "equipment/charactermeleeweapons_create.html"


class UpdateViewCharacterMeleeWeapons(CharacterEquipmentUpdateView):
    """Update view for characters' melee weapon."""
    model = CharacterMeleeWeapons
    form_class = CharacterMeleeWeaponsUpdateForm
    template_name = "equipment/charactermeleeweapons_update.html"


class DeleteViewCharacterMeleeWeapon(CharacterEquipmentDeleteView):
    """Delete view of a characters' melee weapon."""
    model = CharacterMeleeWeapons


class CreateViewCharacterRangedWeapons(CharacterEquipmentCreateView):
    """Create view for characters' ranged weapon."""
    model = CharacterRangedWeapons
    form_class = CharacterRangedWeaponsCreateForm
    category_title = "Ranged Weapon"
    field_name = "ranged_weapon"
    #template_name = "equipment/characterrangedweapons_create.html"


class UpdateViewCharacterRangedWeapons(CharacterEquipmentUpdateView):
    """Update view for characters' ranged weapon."""
    model = CharacterRangedWeapons
    form_class = CharacterRangedWeaponsUpdateForm
    template_name = "equipment/characterrangedweapons_update.html"


class DeleteViewCharacterRangedWeapon(CharacterEquipmentDeleteView):
    """Delete view of a characters' ranged weapon."""
    model = CharacterRangedWeapons


class CreateViewCharacterAmmunition(CharacterEquipmentCreateView):
    """Create view for characters' ammunition."""
    model = CharacterAmmunition
    form_class = CharacterAmmunitionCreateForm
    category_title = "Ammunition"
    field_name = "ammunition"
    #template_name = "equipment/characterammunition_create.html"


class UpdateViewCharacterAmmunition(CharacterEquipmentUpdateView):
    """Update view for characters' ammunition."""
    model = CharacterAmmunition
    form_class = CharacterAmmunitionUpdateForm
    template_name = "equipment/characterammunition_update.html"


class DeleteViewCharacterAmmunition(CharacterEquipmentDeleteView):
    """Delete view of a characters' ammunition."""
    model = CharacterAmmunition


class CreateViewCharacterArmour(CharacterEquipmentCreateView):
    """Create view for characters' armour."""
    model = CharacterArmour
    form_class = CharacterArmourCreateForm
    category_title = "Armour"
    field_name = "armour"
    #template_name = "equipment/characterarmour_create.html"


class UpdateViewCharacterArmour(CharacterEquipmentUpdateView):
    """Update view for characters' armour."""
    model = CharacterArmour
    form_class = CharacterArmourUpdateForm
    template_name = "equipment/characterarmour_update.html"


class DeleteViewCharacterArmour(CharacterEquipmentDeleteView):
    """Delete view of a characters' armour."""
    model = CharacterArmour


class CreateViewCharacterPacksAndContainers(CharacterEquipmentCreateView):
    """Create view for characters' packs and containers."""
    model = CharacterPacksAndContainers
    form_class = CharacterPacksAndContainersCreateForm
    template_name = "equipment/characterpacksandcontainers_create.html"


class UpdateViewCharacterPacksAndContainers(CharacterEquipmentUpdateView):
    """Update view for characters' packs and containers."""
    model = CharacterPacksAndContainers
    form_class = CharacterPacksAndContainersUpdateForm
    template_name = "equipment/characterpacksandcontainers_update.html"


class DeleteViewCharacterPacksAndContainers(CharacterEquipmentDeleteView):
    """Delete view of a characters' packs and containers."""
    model = CharacterPacksAndContainers


class CreateViewCharacterClothingAndAccessories(CharacterEquipmentCreateView):
    """Create view for characters' clothing and accessories."""
    model = CharacterClothingAndAccessories
    form_class = CharacterClothingAndAccessoriesCreateForm
    template_name = "equipment/characterclothingandaccessories_create.html"


class UpdateViewCharacterClothingAndAccessories(CharacterEquipmentUpdateView):
    """Update view for characters' clothing and accessories."""
    model = CharacterClothingAndAccessories
    form_class = CharacterClothingAndAccessoriesUpdateForm
    template_name = "equipment/characterclothingandaccessories_update.html"


class DeleteViewCharacterClothingAndAccessories(CharacterEquipmentDeleteView):
    """Delete view of a characters' clothing and accessories."""
    model = CharacterClothingAndAccessories


class CreateViewCharacterFoodDrinkAndLodging(CharacterEquipmentCreateView):
    """Create view for characters' food, drink and lodging."""
    model = CharacterFoodDrinkAndLodging
    form_class = CharacterFoodDrinkAndLodgingCreateForm
    template_name = "equipment/characterfooddrinkandlodging_create.html"


class UpdateViewCharacterFoodDrinkAndLodging(CharacterEquipmentUpdateView):
    """Update view for characters' food, drink and lodging."""
    model = CharacterFoodDrinkAndLodging
    form_class = CharacterFoodDrinkAndLodgingUpdateForm
    template_name = "equipment/characterfooddrinkandlodging_update.html"


class DeleteViewCharacterFoodDrinkAndLodging(CharacterEquipmentDeleteView):
    """Delete view of a characters' food, drink and lodging."""
    model = CharacterFoodDrinkAndLodging


class CreateViewCharacterToolsAndKits(CharacterEquipmentCreateView):
    """Create view for characters' tools and kits."""
    model = CharacterToolsAndKits
    form_class = CharacterToolsAndKitsCreateForm
    template_name = "equipment/charactertoolsandkits_create.html"


class UpdateViewCharacterToolsAndKits(CharacterEquipmentUpdateView):
    """Update view for characters' tools and kits."""
    model = CharacterToolsAndKits
    form_class = CharacterToolsAndKitsUpdateForm
    template_name = "equipment/charactertoolsandkits_update.html"


class DeleteViewCharacterToolsAndKits(CharacterEquipmentDeleteView):
    """Delete view of a characters' tools and kits."""
    model = CharacterToolsAndKits


class CreateViewCharacterBooksAndDocuments(CharacterEquipmentCreateView):
    """Create view for characters' tools and kits."""
    model = CharacterBooksAndDocuments
    form_class = CharacterBooksAndDocumentsCreateForm
    template_name = "equipment/characterbooksanddocuments_create.html"


class UpdateViewCharacterBooksAndDocuments(CharacterEquipmentUpdateView):
    """Update view for characters' tools and kits."""
    model = CharacterBooksAndDocuments
    form_class = CharacterBooksAndDocumentsUpdateForm
    template_name = "equipment/characterbooksanddocuments_update.html"


class DeleteViewCharacterBooksAndDocuments(CharacterEquipmentDeleteView):
    """Delete view of a characters' books and documents."""
    model = CharacterBooksAndDocuments


class CreateViewCharacterTradeToolsAndWorkshops(CharacterEquipmentCreateView):
    """Create view for characters' tools and workshops."""
    model = CharacterTradeToolsAndWorkshops
    form_class = CharacterTradeToolsAndWorkshopsCreateForm
    template_name = "equipment/charactertradetoolsandworkshops_create.html"


class UpdateViewCharacterTradeToolsAndWorkshops(CharacterEquipmentUpdateView):
    """Update view for characters' tools and workshops."""
    model = CharacterTradeToolsAndWorkshops
    form_class = CharacterTradeToolsAndWorkshopsUpdateForm
    template_name = "equipment/charactertradetoolsandworkshops_update.html"


class DeleteViewCharacterTradeToolsAndWorkshops(CharacterEquipmentDeleteView):
    """Delete view of a characters' trade tools and workshops."""
    model = CharacterTradeToolsAndWorkshops


class CreateViewCharacterAnimalsAndVehicles(CharacterEquipmentCreateView):
    """Create view for characters' animals and vehicles."""
    model = CharacterAnimalsAndVehicles
    form_class = CharacterAnimalsAndVehiclesCreateForm
    template_name = "equipment/characteranimalsandvehicles_create.html"


class UpdateViewCharacterAnimalsAndVehicles(CharacterEquipmentUpdateView):
    """Update view for characters' animals and vehicles."""
    model = CharacterAnimalsAndVehicles
    form_class = CharacterAnimalsAndVehiclesUpdateForm
    template_name = "equipment/characteranimalsandvehicles_update.html"


class DeleteViewCharacterAnimalsAndVehicles(CharacterEquipmentDeleteView):
    """Delete view of a characters' animals and vehicles."""
    model = CharacterAnimalsAndVehicles


class CreateViewCharacterDrugsAndPoisons(CharacterEquipmentCreateView):
    """Create view for characters' drugs and poisons."""
    model = CharacterDrugsAndPoisons
    form_class = CharacterDrugsAndPoisonsCreateForm
    template_name = "equipment/characterdrugsandpoisons_create.html"


class UpdateViewCharacterDrugsAndPoisons(CharacterEquipmentUpdateView):
    """Update view for characters' drugs and poisons."""
    model = CharacterDrugsAndPoisons
    form_class = CharacterDrugsAndPoisonsUpdateForm
    template_name = "equipment/characterdrugsandpoisons_update.html"


class DeleteViewCharacterDrugsAndPoisons(CharacterEquipmentDeleteView):
    """Delete view of a characters' drugs and poisons."""
    model = CharacterDrugsAndPoisons


class CreateViewCharacterHerbsAndDraughts(CharacterEquipmentCreateView):
    """Create view for characters' herbs and draughts."""
    model = CharacterHerbsAndDraughts
    form_class = CharacterHerbsAndDraughtsCreateForm
    template_name = "equipment/characterherbsanddraughts_create.html"


class UpdateViewCharacterHerbsAndDraughts(CharacterEquipmentUpdateView):
    """Update view for characters' herbs and draughts."""
    model = CharacterHerbsAndDraughts
    form_class = CharacterHerbsAndDraughtsUpdateForm
    template_name = "equipment/characterherbsanddraughts_update.html"


class DeleteViewCharacterHerbsAndDraughts(CharacterEquipmentDeleteView):
    """Delete view of a characters' herbs and draughts."""
    model = CharacterHerbsAndDraughts


class CreateViewCharacterProsthetics(CharacterEquipmentCreateView):
    """Create view for characters' prosthetics."""
    model = CharacterProsthetics
    form_class = CharacterProstheticsCreateForm
    template_name = "equipment/characterprosthetics_create.html"


class UpdateViewCharacterProsthetics(CharacterEquipmentUpdateView):
    """Update view for characters' prosthetics."""
    model = CharacterProsthetics
    form_class = CharacterProstheticsUpdateForm
    template_name = "equipment/characterprosthetics_update.html"


class DeleteViewCharacterProsthetics(CharacterEquipmentDeleteView):
    """Delete view of a characters' prosthetics."""
    model = CharacterProsthetics


class CreateViewCharacterMiscellaneousTrappings(CharacterEquipmentCreateView):
    """Create view for characters' miscellaneous trappings."""
    model = CharacterMiscellaneousTrappings
    form_class = CharacterMiscellaneousTrappingsCreateForm
    template_name = "equipment/charactermiscellaneoustrappings_create.html"


class UpdateViewCharacterMiscellaneousTrappings(CharacterEquipmentUpdateView):
    """Update view for characters' miscellaneous trappings."""
    model = CharacterMiscellaneousTrappings
    form_class = CharacterMiscellaneousTrappingsUpdateForm
    template_name = "equipment/charactermiscellaneoustrappings_update.html"


class DeleteViewCharacterMiscellaneousTrappings(CharacterEquipmentDeleteView):
    """Delete view of a characters' miscellaneous trappings."""
    model = CharacterMiscellaneousTrappings


class CreateViewCharacterHirelings(CharacterEquipmentCreateView):
    """Create view for characters' hirelings."""
    model = CharacterHirelings
    form_class = CharacterHirelingsCreateForm
    template_name = "equipment/characterhirelings_create.html"


class UpdateViewCharacterHirelings(CharacterEquipmentUpdateView):
    """Update view for characters' hirelings."""
    model = CharacterHirelings
    form_class = CharacterHirelingsUpdateForm
    template_name = "equipment/characterhirelings_update.html"


class DeleteViewCharacterHirelings(CharacterEquipmentDeleteView):
    """Delete view of a characters' hirelings."""
    model = CharacterHirelings


class DetailViewMeleeWeapons(LoginRequiredMixin, DetailView):
    """Detail view of melee weapons."""

    model = MeleeWeapons
    context_object_name = "melee_weapon"


class DetailViewRangedWeapons(LoginRequiredMixin, DetailView):
    """Detail view of ranged weapons."""

    model = RangedWeapons
    context_object_name = "ranged_weapon"


class DetailViewAmmunition(LoginRequiredMixin, DetailView):
    """Detail view of ammunition."""

    model = Ammunition
    context_object_name = "ammunition"


class DetailViewArmour(LoginRequiredMixin, DetailView):
    """Detail view of an armour."""

    model = Armour
    context_object_name = "armour"


class DetailViewPacksAndContainers(LoginRequiredMixin, DetailView):
    """Detail view of packs and containers."""

    model = PacksAndContainers
    context_object_name = "packs_and_containers"


class DetailViewClothingAndAccessories(LoginRequiredMixin, DetailView):
    """Detail view of clothing and accessories."""

    model = ClothingAndAccessories
    context_object_name = "clothing_and_accessories"


class DetailViewFoodDrinkAndLodging(LoginRequiredMixin, DetailView):
    """Detail view of food drink and lodging."""

    model = FoodDrinkAndLodging
    context_object_name = "food_drink_and_lodging"


class DetailViewToolsAndKits(LoginRequiredMixin, DetailView):
    """Detail view of tools and kits."""

    model = ToolsAndKits
    context_object_name = "tools_and_kits"


class DetailViewBooksAndDocuments(LoginRequiredMixin, DetailView):
    """Detail view of books and documents."""

    model = BooksAndDocuments
    context_object_name = "books_and_documents"


class DetailViewTradeToolsAndWorkshops(LoginRequiredMixin, DetailView):
    """Detail view of trade tools and workshops."""

    model = TradeToolsAndWorkshops
    context_object_name = "trade_tools_and_workshops"


class DetailViewAnimalsAndVehicles(LoginRequiredMixin, DetailView):
    """Detail view of animals and vehicles."""

    model = AnimalsAndVehicles
    context_object_name = "animals_and_vehicles"


class DetailViewDrugsAndPoisons(LoginRequiredMixin, DetailView):
    """Detail view of drugs and poisons."""

    model = DrugsAndPoisons
    context_object_name = "drugs_and_poisons"


class DetailViewHerbsAndDraughts(LoginRequiredMixin, DetailView):
    """Detail view of herbs and draughts."""

    model = HerbsAndDraughts
    context_object_name = "herbs_and_draughts"


class DetailViewProsthetics(LoginRequiredMixin, DetailView):
    """Detail view of prosthetics."""

    model = Prosthetics
    context_object_name = "prosthetics"


class DetailViewMiscellaneousTrappings(LoginRequiredMixin, DetailView):
    """Detail view of miscellaneous trappings."""

    model = MiscellaneousTrappings
    context_object_name = "miscellaneous_trappings"


class DetailViewHirelings(LoginRequiredMixin, DetailView):
    """Detail view of hirelings."""

    model = Hirelings
    context_object_name = "hirelings"
