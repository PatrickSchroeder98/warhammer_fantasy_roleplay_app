from django.db import models
from characters.models import Characters


class MeleeWeapons(models.Model):
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
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)
    range = models.CharField(max_length=50)
    damage = models.CharField(max_length=50)
    qualities_and_flaws = models.CharField(max_length=200)
    type = models.CharField(max_length=50)


class Ammunition(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)
    range = models.CharField(max_length=50)
    damage = models.CharField(max_length=50)
    qualities_and_flaws = models.CharField(max_length=200)
    type = models.CharField(max_length=50)


class Armour(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)
    penalty = models.CharField(max_length=50)
    locations = models.CharField(max_length=50)
    aps = models.IntegerField()
    qualities_and_flaws = models.CharField(max_length=200)
    type = models.CharField(max_length=50)


class PacksAndContainers(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    carries = models.IntegerField()
    availability = models.CharField(max_length=50)


class ClothingAndAccessories(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)


class FoodDrinkAndLodging(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)


class ToolsAndKits(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)


class BooksAndDocuments(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)


class TradeToolsAndWorkshops(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)


class AnimalsAndVehicles(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    carries = models.IntegerField()
    availability = models.CharField(max_length=50)


class DrugsAndPoisons(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)


class HerbsAndDraughts(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)


class Prosthetics(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)


class MiscellaneousTrappings(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)


class Hirelings(models.Model):
    name = models.CharField(max_length=50)
    quick_job = models.CharField(max_length=50)
    daily_cost = models.CharField(max_length=50)
    weekly_cost = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)


class CharacterMeleeWeapons(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    melee_weapon = models.ForeignKey(MeleeWeapons, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterRangedWeapons(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    ranged_weapon = models.ForeignKey(RangedWeapons, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterAmmunition(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    ammunition = models.ForeignKey(Ammunition, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterArmour(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    armour = models.ForeignKey(Armour, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterPacksAndContainers(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    packs_and_containers = models.ForeignKey(PacksAndContainers, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterClothingAndAccessories(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    clothing_and_accessories = models.ForeignKey(ClothingAndAccessories, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterFoodDrinkAndLodging(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    food_drink_and_lodging = models.ForeignKey(FoodDrinkAndLodging, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterToolsAndKits(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    tools_and_kits = models.ForeignKey(ToolsAndKits, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterBooksAndDocuments(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    books_and_documents = models.ForeignKey(BooksAndDocuments, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterTradeToolsAndWorkshops(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    trade_tools_and_workshops = models.ForeignKey(TradeToolsAndWorkshops, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterAnimalsAndVehicles(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    animals_and_vehicles = models.ForeignKey(AnimalsAndVehicles, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterDrugsAndPoisons(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    drugs_and_poisons = models.ForeignKey(DrugsAndPoisons, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterHerbsAndDraughts(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    herbs_and_draughts = models.ForeignKey(HerbsAndDraughts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterProsthetics(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    prosthetics = models.ForeignKey(Prosthetics, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterMiscellaneousTrappings(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    miscellaneous_trappings = models.ForeignKey(MiscellaneousTrappings, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


class CharacterHirelings(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    hirelings = models.ForeignKey(Hirelings, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    equipped = models.BooleanField(default=False)


