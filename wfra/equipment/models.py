from django.db import models


class MeleeWeapon(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    encumbrance = models.IntegerField()
    availability = models.CharField(max_length=50)
    reach = models.CharField(max_length=50)
    damage = models.CharField(max_length=50)
    qualities_and_flaws = models.CharField(max_length=200)
    type = models.CharField(max_length=50)


class RangedWeapon(models.Model):
    name = models.CharField(max_length=50)


class Ammunition(models.Model):
    name = models.CharField(max_length=50)


class Armour(models.Model):
    name = models.CharField(max_length=50)


class Packs(models.Model):
    name = models.CharField(max_length=50)


class Clothing(models.Model):
    name = models.CharField(max_length=50)


class Food(models.Model):
    name = models.CharField(max_length=50)


class Tools(models.Model):
    name = models.CharField(max_length=50)


class Books(models.Model):
    name = models.CharField(max_length=50)


class Workshop(models.Model):
    name = models.CharField(max_length=50)


class Animals(models.Model):
    name = models.CharField(max_length=50)


class Drugs(models.Model):
    name = models.CharField(max_length=50)


class Herbs(models.Model):
    name = models.CharField(max_length=50)


class Prosthetics(models.Model):
    name = models.CharField(max_length=50)


class Trappings(models.Model):
    name = models.CharField(max_length=50)


class Hirelings(models.Model):
    name = models.CharField(max_length=50)
