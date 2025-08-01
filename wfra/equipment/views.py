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
    """Create view for characters' melee weapon."""

    model = CharacterMeleeWeapons
    form_class = CharacterMeleeWeaponsCreateForm
    template_name = "equipment/charactermeleeweapons_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create weapon for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateCharacterRangedWeaponView(LoginRequiredMixin, CreateView):
    """Create view for characters' ranged weapon."""

    model = CharacterRangedWeapons
    form_class = CharacterRangedWeaponsCreateForm
    template_name = "equipment/characterrangedweapons_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create weapon for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterAmmunition(LoginRequiredMixin, CreateView):
    """Create view for characters' ammunition."""

    model = CharacterAmmunition
    form_class = CharacterAmmunitionCreateForm
    template_name = "equipment/characterammunition_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create ammunition for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterArmour(LoginRequiredMixin, CreateView):
    """Create view for characters' armour."""

    model = CharacterArmour
    form_class = CharacterArmourCreateForm
    template_name = "equipment/characterarmour_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create armour for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterPacksAndContainers(LoginRequiredMixin, CreateView):
    """Create view for characters' packs and containers."""

    model = CharacterPacksAndContainers
    form_class = CharacterPacksAndContainersCreateForm
    template_name = "equipment/characterpacksandcontainers_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create containers for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterClothingAndAccessories(LoginRequiredMixin, CreateView):
    """Create view for characters' clothing and accessories."""

    model = CharacterClothingAndAccessories
    form_class = CharacterClothingAndAccessoriesCreateForm
    template_name = "equipment/characterclothingandaccessories_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create clothing for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterFoodDrinkAndLodging(LoginRequiredMixin, CreateView):
    """Create view for characters' food, drink and lodging."""

    model = CharacterFoodDrinkAndLodging
    form_class = CharacterFoodDrinkAndLodgingCreateForm
    template_name = "equipment/characterfooddrinkandlodging_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create food for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterToolsAndKits(LoginRequiredMixin, CreateView):
    """Create view for characters' tools and kits."""

    model = CharacterToolsAndKits
    form_class = CharacterToolsAndKitsCreateForm
    template_name = "equipment/charactertoolsandkits_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create tools for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterBooksAndDocuments(LoginRequiredMixin, CreateView):
    """Create view for characters' tools and kits."""

    model = CharacterBooksAndDocuments
    form_class = CharacterBooksAndDocumentsCreateForm
    template_name = "equipment/characterbooksanddocuments_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create books for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterTradeToolsAndWorkshops(LoginRequiredMixin, CreateView):
    """Create view for characters' tools and workshops."""

    model = CharacterTradeToolsAndWorkshops
    form_class = CharacterTradeToolsAndWorkshopsCreateForm
    template_name = "equipment/charactertradetoolsandworkshops_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create tools for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterAnimalsAndVehicles(LoginRequiredMixin, CreateView):
    """Create view for characters' animals and vehicles."""

    model = CharacterAnimalsAndVehicles
    form_class = CharacterAnimalsAndVehiclesCreateForm
    template_name = "equipment/characteranimalsandvehicles_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create animals or vehicles for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterDrugsAndPoisons(LoginRequiredMixin, CreateView):
    """Create view for characters' drugs and poisons."""

    model = CharacterDrugsAndPoisons
    form_class = CharacterDrugsAndPoisonsCreateForm
    template_name = "equipment/characterdrugsandpoisons_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create drugs or poisons for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterHerbsAndDraughts(LoginRequiredMixin, CreateView):
    """Create view for characters' herbs and draughts."""

    model = CharacterHerbsAndDraughts
    form_class = CharacterHerbsAndDraughtsCreateForm
    template_name = "equipment/characterherbsanddraughts_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create herbs or draughts for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class CreateViewCharacterProsthetics(LoginRequiredMixin, CreateView):
    """Create view for characters' prosthetics."""

    model = CharacterProsthetics
    form_class = CharacterProstheticsCreateForm
    template_name = "equipment/characterprosthetics_create.html"

    def get_form_kwargs(self):
        """Method returns kwargs with saved character."""
        kwargs = super().get_form_kwargs()
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        kwargs["character"] = character
        return kwargs

    def form_valid(self, form):
        """Method ensures the user can only create prosthetics for their own characters."""
        character_id = self.kwargs.get("character_id")
        character = get_object_or_404(
            Characters, pk=character_id, user=self.request.user
        )
        form.instance.character = character
        return super().form_valid(form)

    def get_success_url(self):
        """Method prepares redirection link with character id in argument."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.kwargs["character_id"]},
        )


class UpdateViewCharacterMeleeWeapons(LoginRequiredMixin, UpdateView):
    """Update view for characters' melee weapon."""

    model = CharacterMeleeWeapons
    form_class = CharacterMeleeWeaponsUpdateForm
    template_name = "equipment/charactermeleeweapons_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterMeleeWeapons.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterRangedWeapons(LoginRequiredMixin, UpdateView):
    """Update view for characters' ranged weapon."""

    model = CharacterRangedWeapons
    form_class = CharacterRangedWeaponsUpdateForm
    template_name = "equipment/characterrangedweapons_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterRangedWeapons.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterAmmunition(LoginRequiredMixin, UpdateView):
    """Update view for characters' ammunition."""

    model = CharacterAmmunition
    form_class = CharacterAmmunitionUpdateForm
    template_name = "equipment/characterammunition_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterAmmunition.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterArmour(LoginRequiredMixin, UpdateView):
    """Update view for characters' armour."""

    model = CharacterArmour
    form_class = CharacterArmourUpdateForm
    template_name = "equipment/characterarmour_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterArmour.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterPacksAndContainers(LoginRequiredMixin, UpdateView):
    """Update view for characters' packs and containers."""

    model = CharacterPacksAndContainers
    form_class = CharacterPacksAndContainersUpdateForm
    template_name = "equipment/characterpacksandcontainers_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterPacksAndContainers.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterClothingAndAccessories(LoginRequiredMixin, UpdateView):
    """Update view for characters' clothing and accessories."""

    model = CharacterClothingAndAccessories
    form_class = CharacterClothingAndAccessoriesUpdateForm
    template_name = "equipment/characterclothingandaccessories_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterClothingAndAccessories.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterFoodDrinkAndLodging(LoginRequiredMixin, UpdateView):
    """Update view for characters' food, drink and lodging."""

    model = CharacterFoodDrinkAndLodging
    form_class = CharacterFoodDrinkAndLodgingUpdateForm
    template_name = "equipment/characterfooddrinkandlodging_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterFoodDrinkAndLodging.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterToolsAndKits(LoginRequiredMixin, UpdateView):
    """Update view for characters' tools and kits."""

    model = CharacterToolsAndKits
    form_class = CharacterToolsAndKitsUpdateForm
    template_name = "equipment/charactertoolsandkits_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterToolsAndKits.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterBooksAndDocuments(LoginRequiredMixin, UpdateView):
    """Update view for characters' tools and kits."""

    model = CharacterBooksAndDocuments
    form_class = CharacterBooksAndDocumentsUpdateForm
    template_name = "equipment/characterbooksanddocuments_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterBooksAndDocuments.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterTradeToolsAndWorkshops(LoginRequiredMixin, UpdateView):
    """Update view for characters' tools and workshops."""

    model = CharacterTradeToolsAndWorkshops
    form_class = CharacterTradeToolsAndWorkshopsUpdateForm
    template_name = "equipment/charactertradetoolsandworkshops_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterTradeToolsAndWorkshops.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterAnimalsAndVehicles(LoginRequiredMixin, UpdateView):
    """Update view for characters' animals and vehicles."""

    model = CharacterAnimalsAndVehicles
    form_class = CharacterAnimalsAndVehiclesUpdateForm
    template_name = "equipment/characteranimalsandvehicles_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterAnimalsAndVehicles.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterDrugsAndPoisons(LoginRequiredMixin, UpdateView):
    """Update view for characters' drugs and poisons."""

    model = CharacterDrugsAndPoisons
    form_class = CharacterDrugsAndPoisonsUpdateForm
    template_name = "equipment/characterdrugsandpoisons_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterDrugsAndPoisons.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterHerbsAndDraughts(LoginRequiredMixin, UpdateView):
    """Update view for characters' herbs and draughts."""

    model = CharacterHerbsAndDraughts
    form_class = CharacterHerbsAndDraughtsUpdateForm
    template_name = "equipment/characterherbsanddraughts_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterHerbsAndDraughts.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class UpdateViewCharacterProsthetics(LoginRequiredMixin, UpdateView):
    """Update view for characters' prosthetics."""

    model = CharacterProsthetics
    form_class = CharacterProstheticsUpdateForm
    template_name = "equipment/characterprosthetics_update.html"

    def get_queryset(self):
        """Method filters queryset to only allow access to the user's own characters."""
        return CharacterProsthetics.objects.filter(character__user=self.request.user)

    def get_success_url(self):
        """Method redirects back to character's equipment page."""
        return reverse_lazy(
            "equipment:character_equipment",
            kwargs={"character_id": self.object.character.id},
        )


class DeleteViewCharacterMeleeWeapon(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' melee weapon."""

    model = CharacterMeleeWeapons

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' melee weapon."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' melee weapon."""
        messages.success(self.request, "Characters' Melee Weapon Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterRangedWeapon(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' ranged weapon."""

    model = CharacterRangedWeapons

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' ranged weapon."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' ranged weapon."""
        messages.success(self.request, "Characters' Ranged Weapon Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterAmmunition(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' ammunition."""

    model = CharacterAmmunition

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' ammunition."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' ammunition."""
        messages.success(self.request, "Characters' Ammunition Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterArmour(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' armour."""

    model = CharacterArmour

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' armour."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' armour."""
        messages.success(self.request, "Characters' Armour Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterPacksAndContainers(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' packs and containers."""

    model = CharacterPacksAndContainers

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' containers."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' container."""
        messages.success(self.request, "Characters' Container Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterClothingAndAccessories(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' clothing and accessories."""

    model = CharacterClothingAndAccessories

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' clothing."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' clothing."""
        messages.success(self.request, "Characters' Clothing Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterFoodDrinkAndLodging(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' food, drink and lodging."""

    model = CharacterFoodDrinkAndLodging

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' food, drink and lodging."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' melee weapon."""
        messages.success(self.request, "Characters' Food, Drink Or Lodging Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterToolsAndKits(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' tools and kits."""

    model = CharacterToolsAndKits

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' tools and kits."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' tool or kit."""
        messages.success(self.request, "Characters' Tool Or Kit Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterBooksAndDocuments(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' books and documents."""

    model = CharacterBooksAndDocuments

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' books and documents."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' book or document."""
        messages.success(self.request, "Characters' Book Or Document Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterTradeToolsAndWorkshops(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' trade tools and workshops."""

    model = CharacterTradeToolsAndWorkshops

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' trade tools and workshops."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' trade tools or workshop."""
        messages.success(self.request, "Characters' Trade Tools Or Workshop Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterAnimalsAndVehicles(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' animals and vehicles."""

    model = CharacterAnimalsAndVehicles

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' animals and vehicles."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' animal or vehicle."""
        messages.success(self.request, "Characters' Animal Or Vehicle Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterDrugsAndPoisons(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' drugs and poisons."""

    model = CharacterDrugsAndPoisons

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' drugs and poisons."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' drug or poison."""
        messages.success(self.request, "Characters' Drug Or Poison Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterHerbsAndDraughts(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' herbs and draughts."""

    model = CharacterHerbsAndDraughts

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' herbs and draughts."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' herb or draught."""
        messages.success(self.request, "Characters' Herb Or Draught Deleted")
        return super().delete(*args, **kwargs)


class DeleteViewCharacterProsthetics(LoginRequiredMixin, DeleteView):
    """Delete view of a characters' prosthetics."""

    model = CharacterProsthetics

    def get_success_url(self):
        """Method to redirect user after successful deletion."""
        character_id = self.object.character.id
        return reverse_lazy(
            "equipment:character_equipment", kwargs={"character_id": character_id}
        )

    def get_queryset(self):
        """Method to ensure that only the owner can delete their characters' prosthetics."""
        return super().get_queryset().filter(character__user=self.request.user)

    def delete(self, *args, **kwargs):
        """Method deletes chosen characters' prosthetics."""
        messages.success(self.request, "Characters' Prosthetics Deleted")
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
