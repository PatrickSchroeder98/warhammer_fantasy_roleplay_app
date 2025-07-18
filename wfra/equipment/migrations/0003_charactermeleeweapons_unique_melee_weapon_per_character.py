# Generated by Django 5.2.1 on 2025-06-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_alter_characters_career_tier_and_more'),
        ('equipment', '0002_characterammunition_characteranimalsandvehicles_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='charactermeleeweapons',
            constraint=models.UniqueConstraint(fields=('character', 'melee_weapon'), name='unique_melee_weapon_per_character'),
        ),
    ]
