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


class Fate(models.Model):

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    fate = models.IntegerField()
    fortune = models.IntegerField()


class Characteristics(models.Model):
    """
    character_id
    INT
    FK
    WS_initial
    INT
    WS_advances
    INT
    WS_current
    INT
    BS_initial
    INT
    BS_advances
    INT
    BS_current
    INT
    S_initial
    INT
    S_advances
    INT
    S_current
    INT
    T_initial
    INT
    T_advances
    INT
    T_current
    INT
    I_initial
    INT
    I_advances
    INT
    I_current
    INT
    Ag_initial
    INT
    Ag_advances
    INT
    Ag_current
    INT
    Dex_initial
    INT
    Dex_advances
    INT
    Dex_current
    INT
    Int_initial
    INT
    Int_advances
    INT
    Int_current
    INT
    WP_initial
    INT
    WP_advances
    INT
    WP_current
    INT
    Fel_initial
    INT
    Fel_advances
    INT
    Fel_current
    INT
    """