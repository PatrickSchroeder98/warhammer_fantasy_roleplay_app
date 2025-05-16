from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
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
