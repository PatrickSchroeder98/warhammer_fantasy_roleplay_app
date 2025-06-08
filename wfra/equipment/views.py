from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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


class CreateCharacterMeleeWeaponView(LoginRequiredMixin, CreateView):
    model = CharacterMeleeWeapons
    form_class = CharacterMeleeWeaponsCreateForm
    template_name = "equipment/charactermeleeweapons_create.html"

    def form_valid(self, form):
        """Ensure the user can only create for their own characters"""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(Characters, pk=character_id, user=self.request.user)
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("equipment:character_equipment", kwargs={"character_id": self.kwargs["character_id"]})


class UpdateViewCharacterMeleeWeapons(LoginRequiredMixin, UpdateView):
    model = CharacterMeleeWeapons
    form_class = CharacterMeleeWeaponsUpdateForm
    template_name = "equipment/charactermeleeweapons_update.html"

    def get_queryset(self):
        """Filter queryset to only allow access to the user's own characters."""
        return CharacterMeleeWeapons.objects.filter(
            character__user=self.request.user  # adjust if your user FK field has a different name
        )

    def get_success_url(self):
        """Redirect back to character's equipment page."""
        return reverse_lazy("equipment:character_equipment", kwargs={"character_id": self.object.character.id})


class DeleteViewCharacterMeleeWeapon(LoginRequiredMixin, DeleteView):
    """Delete view of a character melee weapon."""

    model = CharacterMeleeWeapons

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy("equipment:character_equipment", kwargs={"character_id": character_id})

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' melee weapon."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen character melee weapon."""
        messages.success(self.request, "Character Melee Weapon Deleted")
        return super().delete(*args, **kwargs)


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
