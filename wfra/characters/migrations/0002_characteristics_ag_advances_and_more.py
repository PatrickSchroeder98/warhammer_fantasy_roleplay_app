# Generated by Django 5.1.2 on 2025-01-14 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristics',
            name='Ag_advances',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Ag_current',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Ag_initial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='BS_advances',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='BS_current',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='BS_initial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Dex_advances',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Dex_current',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Dex_initial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Fel_advances',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Fel_current',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Fel_initial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='I_advances',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='I_current',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='I_initial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Int_advances',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Int_current',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='Int_initial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='S_advances',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='S_current',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='S_initial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='T_advances',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='T_current',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='T_initial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='WP_advances',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='WP_current',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='WP_initial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='WS_advances',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='WS_current',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='WS_initial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristics',
            name='character_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='characters.characters'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characters',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characters',
            name='career',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characters',
            name='career_path',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characters',
            name='career_tier',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characters',
            name='character_class',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characters',
            name='eyes',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characters',
            name='hair',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characters',
            name='height',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characters',
            name='status',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AdvancedSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('attribute_name', models.CharField(max_length=500)),
                ('attribute_value', models.IntegerField()),
                ('advances', models.IntegerField()),
                ('sum', models.IntegerField()),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='Ambitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_term', models.CharField(max_length=1000)),
                ('long_term', models.CharField(max_length=1000)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='BasicSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_characteristics', models.IntegerField()),
                ('art_advances', models.IntegerField()),
                ('art_skill', models.IntegerField()),
                ('athletics_characteristics', models.IntegerField()),
                ('athletics_advances', models.IntegerField()),
                ('athletics_skill', models.IntegerField()),
                ('bribery_characteristics', models.IntegerField()),
                ('bribery_advances', models.IntegerField()),
                ('bribery_skill', models.IntegerField()),
                ('charm_characteristics', models.IntegerField()),
                ('charm_advances', models.IntegerField()),
                ('charm_skill', models.IntegerField()),
                ('charm_animal_characteristics', models.IntegerField()),
                ('charm_animal_advances', models.IntegerField()),
                ('charm_animal_skill', models.IntegerField()),
                ('climb_characteristics', models.IntegerField()),
                ('climb_advances', models.IntegerField()),
                ('climb_skill', models.IntegerField()),
                ('cool_characteristics', models.IntegerField()),
                ('cool_advances', models.IntegerField()),
                ('cool_skill', models.IntegerField()),
                ('consume_alcohol_characteristics', models.IntegerField()),
                ('consume_alcohol_advances', models.IntegerField()),
                ('consume_alcohol_skill', models.IntegerField()),
                ('dodge_characteristics', models.IntegerField()),
                ('dodge_advances', models.IntegerField()),
                ('dodge_skill', models.IntegerField()),
                ('drive_characteristics', models.IntegerField()),
                ('drive_advances', models.IntegerField()),
                ('drive_skill', models.IntegerField()),
                ('endurance_characteristics', models.IntegerField()),
                ('endurance_advances', models.IntegerField()),
                ('endurance_skill', models.IntegerField()),
                ('entertain_characteristics', models.IntegerField()),
                ('entertain_advances', models.IntegerField()),
                ('entertain_skill', models.IntegerField()),
                ('gamble_characteristics', models.IntegerField()),
                ('gamble_advances', models.IntegerField()),
                ('gamble_skill', models.IntegerField()),
                ('gossip_characteristics', models.IntegerField()),
                ('gossip_advances', models.IntegerField()),
                ('gossip_skill', models.IntegerField()),
                ('haggle_characteristics', models.IntegerField()),
                ('haggle_advances', models.IntegerField()),
                ('haggle_skill', models.IntegerField()),
                ('intimidate_characteristics', models.IntegerField()),
                ('intimidate_advances', models.IntegerField()),
                ('intimidate_skill', models.IntegerField()),
                ('intuition_characteristics', models.IntegerField()),
                ('intuition_advances', models.IntegerField()),
                ('intuition_skill', models.IntegerField()),
                ('leadership_characteristics', models.IntegerField()),
                ('leadership_advances', models.IntegerField()),
                ('leadership_skill', models.IntegerField()),
                ('melee_basic_characteristics', models.IntegerField()),
                ('melee_basic_advances', models.IntegerField()),
                ('melee_basic_skill', models.IntegerField()),
                ('melee_characteristics', models.IntegerField()),
                ('melee_advances', models.IntegerField()),
                ('melee_skill', models.IntegerField()),
                ('navigation_characteristics', models.IntegerField()),
                ('navigation_advances', models.IntegerField()),
                ('navigation_skill', models.IntegerField()),
                ('outdoor_survival_characteristics', models.IntegerField()),
                ('outdoor_survival_advances', models.IntegerField()),
                ('outdoor_survival_skill', models.IntegerField()),
                ('perception_characteristics', models.IntegerField()),
                ('perception_advances', models.IntegerField()),
                ('perception_skill', models.IntegerField()),
                ('ride_characteristics', models.IntegerField()),
                ('ride_advances', models.IntegerField()),
                ('ride_skill', models.IntegerField()),
                ('row_characteristics', models.IntegerField()),
                ('row_advances', models.IntegerField()),
                ('row_skill', models.IntegerField()),
                ('stealth_characteristics', models.IntegerField()),
                ('stealth_advances', models.IntegerField()),
                ('stealth_skill', models.IntegerField()),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='CorruptionAndMutation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect', models.CharField(max_length=1000)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.IntegerField()),
                ('spent', models.IntegerField()),
                ('total', models.IntegerField()),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement', models.IntegerField()),
                ('walk', models.IntegerField()),
                ('run', models.IntegerField()),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=1000)),
                ('short_term', models.CharField(max_length=1000)),
                ('long_term', models.CharField(max_length=1000)),
                ('members', models.CharField(max_length=1000)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='Psychology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect', models.CharField(max_length=1000)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='Resilience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resilience', models.IntegerField()),
                ('resolve', models.IntegerField()),
                ('motivation', models.CharField(max_length=500)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='Sin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sin', models.IntegerField()),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='Talents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talent', models.CharField(max_length=500)),
                ('times_taken', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
        migrations.CreateModel(
            name='Wounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sb', models.IntegerField()),
                ('tb_x2', models.IntegerField()),
                ('wbp', models.IntegerField()),
                ('hardy', models.IntegerField()),
                ('wounds', models.IntegerField()),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.characters')),
            ],
        ),
    ]
