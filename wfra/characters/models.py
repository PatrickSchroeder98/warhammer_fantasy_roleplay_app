from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Characters(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    character_class = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    career_tier = models.CharField(max_length=200)
    career_path = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.IntegerField()
    hair = models.CharField(max_length=200)
    eyes = models.CharField(max_length=200)


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


class BasicSkills(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)

    art_characteristics = models.IntegerField()
    art_advances = models.IntegerField()
    art_skill = models.IntegerField()

    athletics_characteristics = models.IntegerField()
    athletics_advances = models.IntegerField()
    athletics_skill = models.IntegerField()

    bribery_characteristics = models.IntegerField()
    bribery_advances = models.IntegerField()
    bribery_skill = models.IntegerField()

    charm_characteristics = models.IntegerField()
    charm_advances = models.IntegerField()
    charm_skill = models.IntegerField()

    charm_animal_characteristics = models.IntegerField()
    charm_animal_advances = models.IntegerField()
    charm_animal_skill = models.IntegerField()

    climb_characteristics = models.IntegerField()
    climb_advances = models.IntegerField()
    climb_skill = models.IntegerField()

    cool_characteristics = models.IntegerField()
    cool_advances = models.IntegerField()
    cool_skill = models.IntegerField()

    consume_alcohol_characteristics = models.IntegerField()
    consume_alcohol_advances = models.IntegerField()
    consume_alcohol_skill = models.IntegerField()

    dodge_characteristics = models.IntegerField()
    dodge_advances = models.IntegerField()
    dodge_skill = models.IntegerField()

    drive_characteristics = models.IntegerField()
    drive_advances = models.IntegerField()
    drive_skill = models.IntegerField()

    endurance_characteristics = models.IntegerField()
    endurance_advances = models.IntegerField()
    endurance_skill = models.IntegerField()

    entertain_characteristics = models.IntegerField()
    entertain_advances = models.IntegerField()
    entertain_skill = models.IntegerField()

    gamble_characteristics = models.IntegerField()
    gamble_advances = models.IntegerField()
    gamble_skill = models.IntegerField()

    gossip_characteristics = models.IntegerField()
    gossip_advances = models.IntegerField()
    gossip_skill = models.IntegerField()

    haggle_characteristics = models.IntegerField()
    haggle_advances = models.IntegerField()
    haggle_skill = models.IntegerField()

    intimidate_characteristics = models.IntegerField()
    intimidate_advances = models.IntegerField()
    intimidate_skill = models.IntegerField()

    intuition_characteristics = models.IntegerField()
    intuition_advances = models.IntegerField()
    intuition_skill = models.IntegerField()

    leadership_characteristics = models.IntegerField()
    leadership_advances = models.IntegerField()
    leadership_skill = models.IntegerField()

    melee_basic_characteristics = models.IntegerField()
    melee_basic_advances = models.IntegerField()
    melee_basic_skill = models.IntegerField()

    melee_characteristics = models.IntegerField()
    melee_advances = models.IntegerField()
    melee_skill = models.IntegerField()

    navigation_characteristics = models.IntegerField()
    navigation_advances = models.IntegerField()
    navigation_skill = models.IntegerField()

    outdoor_survival_characteristics = models.IntegerField()
    outdoor_survival_advances = models.IntegerField()
    outdoor_survival_skill = models.IntegerField()

    perception_characteristics = models.IntegerField()
    perception_advances = models.IntegerField()
    perception_skill = models.IntegerField()

    ride_characteristics = models.IntegerField()
    ride_advances = models.IntegerField()
    ride_skill = models.IntegerField()

    row_characteristics = models.IntegerField()
    row_advances = models.IntegerField()
    row_skill = models.IntegerField()

    stealth_characteristics = models.IntegerField()
    stealth_advances = models.IntegerField()
    stealth_skill = models.IntegerField()


class AdvancedSkills(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    attribute_name = models.CharField(max_length=500)
    attribute_value = models.IntegerField()
    advances = models.IntegerField()
    total = models.IntegerField()


class Talents(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    talent = models.CharField(max_length=500)
    times_taken = models.IntegerField()
    description = models.CharField(max_length=1000)


class Ambitions(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    short_term = models.CharField(max_length=1000)
    long_term = models.CharField(max_length=1000)


class Party(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    party_name = models.CharField(max_length=1000)
    short_term = models.CharField(max_length=1000)
    long_term = models.CharField(max_length=1000)
    members = models.CharField(max_length=1000)


class Psychology(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    effect = models.CharField(max_length=1000)


class CorruptionAndMutation(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    effect = models.CharField(max_length=1000)


class Wounds(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    sb = models.IntegerField()
    tb_x2 = models.IntegerField()
    wbp = models.IntegerField()
    hardy = models.IntegerField()
    wounds = models.IntegerField()


class Sin(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    sin = models.IntegerField()
