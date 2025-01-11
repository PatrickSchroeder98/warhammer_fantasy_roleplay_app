from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Characters(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    """
    TODO for later
    character_class =
    career =
    career_tier =
    career_path =
    status =
    age =
    height =
    hair =
    eyes =
    """


class Characteristics(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)

    WS_initial = models.IntegerField()
    WS_advances = models.IntegerField()
    WS_current = models.IntegerField()

    BS_initial = models.IntegerField()
    BS_advances = models.IntegerField()
    BS_current = models.IntegerField()

    S_initial = models.IntegerField()
    S_advances = models.IntegerField()
    S_current = models.IntegerField()

    T_initial = models.IntegerField()
    T_advances = models.IntegerField()
    T_current = models.IntegerField()

    I_initial = models.IntegerField()
    I_advances = models.IntegerField()
    I_current = models.IntegerField()

    Ag_initial = models.IntegerField()
    Ag_advances = models.IntegerField()
    Ag_current = models.IntegerField()

    Dex_initial = models.IntegerField()
    Dex_advances = models.IntegerField()
    Dex_current = models.IntegerField()

    Int_initial = models.IntegerField()
    Int_advances = models.IntegerField()
    Int_current = models.IntegerField()

    WP_initial = models.IntegerField()
    WP_advances = models.IntegerField()
    WP_current = models.IntegerField()

    Fel_initial = models.IntegerField()
    Fel_advances = models.IntegerField()
    Fel_current = models.IntegerField()


class Fate(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    fate = models.IntegerField()
    fortune = models.IntegerField()


class Resilience(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    resilience = models.IntegerField()
    resolve = models.IntegerField()
    motivation = models.CharField(max_length=500)


class Experience(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    current = models.IntegerField()
    spent = models.IntegerField()
    total = models.IntegerField()


class Movement(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    movement = models.IntegerField()
    walk = models.IntegerField()
    run = models.IntegerField()


"""
class BasicSkills
class AdvancedSkills
"""