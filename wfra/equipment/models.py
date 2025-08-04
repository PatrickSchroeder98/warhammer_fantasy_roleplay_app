from django.db import models
from characters.models import Characters


class MeleeWeapons(models.Model):
    """Model with fields for melee weapons."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)
    reach = models.CharField(max_length=50)
    damage = models.CharField(max_length=50)
    qualities_and_flaws = models.CharField(max_length=200)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (DMG: {self.damage}, ENC: {self.encumbrance})"


class RangedWeapons(models.Model):
    """Model with fields for ranged weapons."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)
    range = models.CharField(max_length=50)
    damage = models.CharField(max_length=50)
    qualities_and_flaws = models.CharField(max_length=200)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (DMG: {self.damage}, ENC: {self.encumbrance})"


class Ammunition(models.Model):
    """Model with fields for ammunition."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)
    range = models.CharField(max_length=50)
    damage = models.CharField(max_length=50)
    qualities_and_flaws = models.CharField(max_length=200)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (DMG: {self.damage}, ENC: {self.encumbrance}, Price {self.price})"


class Armour(models.Model):
    """Model with fields for armour."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)
    penalty = models.CharField(max_length=50)
    locations = models.CharField(max_length=50)
    aps = models.IntegerField()
    qualities_and_flaws = models.CharField(max_length=200)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (APS: {self.aps}, ENC: {self.encumbrance}, Price {self.price})"


class PacksAndContainers(models.Model):
    """Model with fields for packs and containers."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    carries = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (Carries: {self.carries}, ENC: {self.encumbrance}, Price {self.price})"


class ClothingAndAccessories(models.Model):
    """Model with fields for clothing and accessories."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (ENC: {self.encumbrance}, Price {self.price})"


class FoodDrinkAndLodging(models.Model):
    """Model with fields for food, drink and lodging."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (ENC: {self.encumbrance}, Price {self.price})"


class ToolsAndKits(models.Model):
    """Model with fields for tools and kits."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (ENC: {self.encumbrance}, Price {self.price})"


class BooksAndDocuments(models.Model):
    """Model with fields for books and documents."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (ENC: {self.encumbrance}, Price {self.price})"


class TradeToolsAndWorkshops(models.Model):
    """Model with fields for trade tools and workshops."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (ENC: {self.encumbrance}, Price {self.price})"


class AnimalsAndVehicles(models.Model):
    """Model with fields for animals and vehicles."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    carries = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (Carries: {self.carries}, ENC: {self.encumbrance}, Price {self.price})"

class DrugsAndPoisons(models.Model):
    """Model with fields for drugs and poisons."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (ENC: {self.encumbrance}, Price {self.price})"


class HerbsAndDraughts(models.Model):
    """Model with fields for herbs and draughts."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (ENC: {self.encumbrance}, Price {self.price})"


class Prosthetics(models.Model):
    """Model with fields for prosthetics."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (ENC: {self.encumbrance}, Price {self.price})"


class MiscellaneousTrappings(models.Model):
    """Model with fields for miscellaneous trappings."""

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} (ENC: {self.encumbrance}, Price {self.price})"


class Hirelings(models.Model):
    """Model with fields for hirelings."""

    name = models.CharField(max_length=50)
    quick_job = models.CharField(max_length=50)
    daily_cost = models.CharField(max_length=50)
    weekly_cost = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)


class CharacterMeleeWeapons(models.Model):
    """Model with fields for characters' melee weapons."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    melee_weapon = models.ForeignKey(MeleeWeapons, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "melee_weapon"],
                name="unique_melee_weapon_per_character",
            )
        ]


class CharacterRangedWeapons(models.Model):
    """Model with fields for characters' ranged weapons."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    ranged_weapon = models.ForeignKey(RangedWeapons, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "ranged_weapon"],
                name="unique_ranged_weapon_per_character",
            )
        ]


class CharacterAmmunition(models.Model):
    """Model with fields for characters' ammunition."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    ammunition = models.ForeignKey(Ammunition, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "ammunition"],
                name="unique_ammunition_per_character",
            )
        ]


class CharacterArmour(models.Model):
    """Model with fields for characters' armour."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    armour = models.ForeignKey(Armour, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "armour"],
                name="unique_armour_per_character",
            )
        ]


class CharacterPacksAndContainers(models.Model):
    """Model with fields for characters' packs and containers."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    packs_and_containers = models.ForeignKey(
        PacksAndContainers, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "packs_and_containers"],
                name="unique_packs_and_containers_per_character",
            )
        ]


class CharacterClothingAndAccessories(models.Model):
    """Model with fields for characters' clothing and accessories."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    clothing_and_accessories = models.ForeignKey(
        ClothingAndAccessories, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "clothing_and_accessories"],
                name="unique_clothing_and_accessories_per_character",
            )
        ]


class CharacterFoodDrinkAndLodging(models.Model):
    """Model with fields for characters' food, drink and lodging."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    food_drink_and_lodging = models.ForeignKey(
        FoodDrinkAndLodging, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "food_drink_and_lodging"],
                name="unique_food_drink_and_lodging_per_character",
            )
        ]


class CharacterToolsAndKits(models.Model):
    """Model with fields for characters' tools and kits."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    tools_and_kits = models.ForeignKey(ToolsAndKits, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "tools_and_kits"],
                name="unique_tools_and_kits_per_character",
            )
        ]


class CharacterBooksAndDocuments(models.Model):
    """Model with fields for characters' books and documents."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    books_and_documents = models.ForeignKey(BooksAndDocuments, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "books_and_documents"],
                name="unique_books_and_documents_per_character",
            )
        ]


class CharacterTradeToolsAndWorkshops(models.Model):
    """Model with fields for characters' trade tools and workshops."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    trade_tools_and_workshops = models.ForeignKey(
        TradeToolsAndWorkshops, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "trade_tools_and_workshops"],
                name="unique_trade_tools_and_workshops_per_character",
            )
        ]


class CharacterAnimalsAndVehicles(models.Model):
    """Model with fields for characters' animals and vehicles."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    animals_and_vehicles = models.ForeignKey(
        AnimalsAndVehicles, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "animals_and_vehicles"],
                name="unique_animals_and_vehicles_per_character",
            )
        ]


class CharacterDrugsAndPoisons(models.Model):
    """Model with fields for characters' drugs and poisons."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    drugs_and_poisons = models.ForeignKey(DrugsAndPoisons, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "drugs_and_poisons"],
                name="unique_drugs_and_poisons_per_character",
            )
        ]


class CharacterHerbsAndDraughts(models.Model):
    """Model with fields for characters' herbs and draughts."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    herbs_and_draughts = models.ForeignKey(HerbsAndDraughts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "herbs_and_draughts"],
                name="unique_herbs_and_draughts_per_character",
            )
        ]


class CharacterProsthetics(models.Model):
    """Model with fields for characters' prosthetics."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    prosthetics = models.ForeignKey(Prosthetics, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "prosthetics"],
                name="unique_prosthetics_per_character",
            )
        ]


class CharacterMiscellaneousTrappings(models.Model):
    """Model with fields for characters' miscellaneous trappings."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    miscellaneous_trappings = models.ForeignKey(
        MiscellaneousTrappings, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["character", "miscellaneous_trappings"],
                name="unique_miscellaneous_trappings_per_character",
            )
        ]


class CharacterHirelings(models.Model):
    """Model with fields for characters' hirelings."""

    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    hirelings = models.ForeignKey(Hirelings, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)
