from django.db import models


class MeleeWeapons(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)
    reach = models.CharField(max_length=50)
    damage = models.CharField(max_length=50)
    qualities_and_flaws = models.CharField(max_length=200)
    type = models.CharField(max_length=50)


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
