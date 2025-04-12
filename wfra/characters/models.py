from django.db import models
from django.contrib.auth import get_user_model
from utils.utils import SPECIES_CHOICES, CAREER_PATHS_MAP

User = get_user_model()


class Characters(models.Model):
    """Model with fields for basic character information."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=100, choices=SPECIES_CHOICES, default="Human")
    character_class = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    career_tier = models.CharField(max_length=2, choices=CAREER_PATHS_MAP, default="1")
    career_path = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.IntegerField()
    hair = models.CharField(max_length=200)
    eyes = models.CharField(max_length=200)
    backstory = models.CharField(max_length=2000)
    other_information = models.CharField(max_length=500)


class Characteristics(models.Model):
    """Model with fields related to characteristics, such as strength or intelligence."""

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

    def save(self, *args, **kwargs):
        """Method save is overwritten to calculate current values of characteristics."""

        self.WS_current = sum([self.WS_initial, self.WS_advances])
        self.BS_current = sum([self.BS_initial, self.BS_advances])
        self.S_current = sum([self.S_initial, self.S_advances])
        self.T_current = sum([self.T_initial, self.T_advances])
        self.I_current = sum([self.I_initial, self.I_advances])
        self.Ag_current = sum([self.Ag_initial, self.Ag_advances])
        self.Dex_current = sum([self.Dex_initial, self.Dex_advances])
        self.Int_current = sum([self.Int_initial, self.Int_advances])
        self.WP_current = sum([self.WP_initial, self.WS_advances])
        self.Fel_current = sum([self.Fel_initial, self.Fel_advances])

        super().save(*args, **kwargs)


class Fate(models.Model):
    """Model containing fate and fortune points of characters."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    fate = models.IntegerField()
    fortune = models.IntegerField()


class Resilience(models.Model):
    """Model containing resilience and resolve points of character, along with motivation CharField."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    resilience = models.IntegerField()
    resolve = models.IntegerField()
    motivation = models.CharField(max_length=500)


class Experience(models.Model):
    """Model with experience points fields."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    current = models.IntegerField()
    spent = models.IntegerField()
    total = models.IntegerField()


class Movement(models.Model):
    """Model containing fields for various movement points values."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    movement = models.IntegerField()
    walk = models.IntegerField()
    run = models.IntegerField()


class BasicSkills(models.Model):
    """Model with characteristic value, advances and total value of every basic skill."""

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

    # def save(self, *args, **kwargs):
    #     """Method save is overwritten to calculate current values of basic skills."""
    #     characteristics = Characteristics.objects.get(character_id=self.character_id)
    #     if characteristics:
    #         self.art_characteristics = characteristics.Dex_current
    #     else:
    #         self.art_characteristics = 0  # Default if no Characteristics found
    #
    #     #self.art_characteristics = sum([characteristics.Dex_current])
    #     self.art_skill = sum([self.art_characteristics, self.art_advances])
    #
    #     self.athletics_characteristics = sum([characteristics.Ag_current])
    #     self.athletics_skill = sum([self.athletics_characteristics, self.athletics_advances])
    #
    #     self.bribery_characteristics = sum([characteristics.Fel_current])
    #     self.bribery_skill = sum([self.bribery_characteristics, self.bribery_advances])
    #
    #     self.charm_characteristics = sum([characteristics.Fel_current])
    #     self.charm_skill = sum([self.charm_characteristics, self.charm_advances])
    #
    #     self.charm_animal_characteristics = sum([characteristics.WP_current])
    #     self.charm_animal_skill = sum([self.charm_animal_characteristics, self.charm_animal_advances])
    #
    #     self.climb_characteristics = sum([characteristics.S_current])
    #     self.climb_skill = sum([self.climb_characteristics, self.climb_advances])
    #
    #     self.cool_characteristics = sum([characteristics.WP_current])
    #     self.cool_skill = sum([self.cool_characteristics, self.cool_advances])
    #
    #     self.consume_alcohol_characteristics = sum([characteristics.T_current])
    #     self.consume_alcohol_skill = sum([self.consume_alcohol_characteristics, self.consume_alcohol_advances])
    #
    #     self.dodge_characteristics = sum([characteristics.Ag_current])
    #     self.dodge_skill = sum([self.dodge_characteristics, self.dodge_advances])
    #
    #     self.drive_characteristics = sum([characteristics.Ag_current])
    #     self.drive_skill = sum([self.drive_characteristics, self.drive_advances])
    #
    #     self.endurance_characteristics = sum([characteristics.T_current])
    #     self.endurance_skill = sum([self.endurance_characteristics, self.endurance_advances])
    #
    #     self.entertain_characteristics = sum([characteristics.Fel_current])
    #     self.entertain_skill = sum([self.entertain_characteristics, self.entertain_advances])
    #
    #     self.gamble_characteristics = sum([characteristics.Int_current])
    #     self.gamble_skill = sum([self.gamble_characteristics, self.gamble_advances])
    #
    #     self.gossip_characteristics = sum([characteristics.Fel_current])
    #     self.gossip_skill = sum([self.gossip_characteristics, self.gossip_advances])
    #
    #     self.haggle_characteristics = sum([characteristics.Fel_current])
    #     self.haggle_skill = sum([self.haggle_characteristics, self.haggle_advances])
    #
    #     self.intimidate_characteristics = sum([characteristics.S_current])
    #     self.intimidate_skill = sum([self.intimidate_characteristics, self.intimidate_advances])
    #
    #     self.intuition_characteristics = sum([characteristics.I_current])
    #     self.intuition_skill = sum([self.intuition_characteristics, self.intuition_advances])
    #
    #     self.leadership_characteristics = sum([characteristics.Fel_current])
    #     self.leadership_skill = sum([self.leadership_characteristics, self.leadership_advances])
    #
    #     self.melee_basic_characteristics = sum([characteristics.WS_current])
    #     self.melee_basic_skill = sum([self.melee_basic_characteristics, self.melee_basic_advances])
    #
    #     self.melee_characteristics = sum([characteristics.WS_current])
    #     self.melee_skill = sum([self.melee_characteristics, self.melee_advances])
    #
    #     self.navigation_characteristics = sum([characteristics.I_current])
    #     self.navigation_skill = sum([self.navigation_characteristics, self.navigation_advances])
    #
    #     self.outdoor_survival_characteristics = sum([characteristics.Int_current])
    #     self.outdoor_survival_skill = sum([self.outdoor_survival_characteristics, self.outdoor_survival_advances])
    #
    #     self.perception_characteristics = sum([characteristics.I_current])
    #     self.perception_skill = sum([self.perception_characteristics, self.perception_advances])
    #
    #     self.ride_characteristics = sum([characteristics.Ag_current])
    #     self.ride_skill = sum([self.ride_characteristics, self.ride_advances])
    #
    #     self.row_characteristics = sum([characteristics.S_current])
    #     self.row_skill = sum([self.row_characteristics, self.row_advances])
    #
    #     self.stealth_characteristics = sum([characteristics.Ag_current])
    #     self.stealth_advances = sum([self.stealth_characteristics, self.stealth_advances])


class AdvancedSkills(models.Model):
    """Model with name, characteristic name and value, advances and total value of advanced skills."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    attribute_name = models.CharField(max_length=500)
    attribute_value = models.IntegerField()
    advances = models.IntegerField()
    total = models.IntegerField()


class Talents(models.Model):
    """Model with fields related to talents."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    talent = models.CharField(max_length=500)
    times_taken = models.IntegerField()
    description = models.CharField(max_length=1000)


class Ambitions(models.Model):
    """Model with fields related to ambitions."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    short_term = models.CharField(max_length=1000)
    long_term = models.CharField(max_length=1000)


class Party(models.Model):
    """Model with fields storing information about party."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    party_name = models.CharField(max_length=1000)
    short_term = models.CharField(max_length=1000)
    long_term = models.CharField(max_length=1000)
    members = models.CharField(max_length=1000)


class Psychology(models.Model):
    """Model with field storing information about psychological effects."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    effect = models.CharField(max_length=1000)


class CorruptionAndMutation(models.Model):
    """Model with field storing information about corruption and mutation effects."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    effect = models.CharField(max_length=1000)


class Wounds(models.Model):
    """Model with fields related to wounds formula."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    sb = models.IntegerField()
    tb_x2 = models.IntegerField()
    wbp = models.IntegerField()
    hardy = models.IntegerField()
    wounds = models.IntegerField()
    current_wounds = models.IntegerField()


class Sin(models.Model):
    """Model with field storing information about sin points."""

    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    sin = models.IntegerField()
