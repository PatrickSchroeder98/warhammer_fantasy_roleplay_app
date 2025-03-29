import json

SPECIES_CHOICES = [
        ("Human", "Human"),
        ("Dwarf", "Dwarf"),
        ("Halfling", "Halfling"),
        ("Wood Elf", "Wood Elf"),
        ("High Elf", "High Elf"),
    ]

CAREER_OPTIONS = {
        "Human": {
                  "Academics": [ "Apothecary", "Engineer", "Lawyer", "Nun", "Physician", "Priest", "Scholar", "Wizard",],
                  "Burghers": [ "Agitator", "Artisan", "Beggar", "Investigator", "Merchant", "Rat Catcher", "Townsman", "Watchman",],
                  "Courtiers": [ "Advisor", "Artist", "Duellist", "Envoy", "Noble", "Servant", "Spy", "Warden",],
                  "Peasants": [ "Bailiff", "Hedge Witch", "Herbalist", "Hunter", "Miner", "Mystic", "Scout", "Villager",],
                  "Rangers": [ "Bounty Hunter", "Coachman", "Entertainer", "Flagellant", "Messenger", "Pedlar", "Roadwarden", "Witch Hunter",],
                  "Riverfolk": [ "Boatman", "Huffer", "Riverwarden", "Riverwoman", "Seaman", "Smuggler", "Stevedore", "Wrecker",],
                  "Rogues": [ "Bawd", "Charlatan", "Fence", "Grave Robber", "Outlaw", "Racketeer", "Thief", "Witch",],
                  "Warriors": [ "Cavalryman", "Guard", "Knight", "Pit Fighter", "Protagonist", "Soldier", "Warrior Priest",],
                  },

        "Dwarf": {
                  "Academics": [ "Apothecary", "Engineer", "Lawyer", "Physician", "Scholar",],
                  "Burghers": [ "Agitator", "Artisan", "Beggar", "Investigator", "Merchant", "Rat Catcher", "Townsman", "Watchman",],
                  "Courtiers": [ "Advisor", "Artist", "Duellist", "Envoy", "Noble", "Servant", "Spy", "Warden",],
                  "Peasants": [ "Bailiff", "Hunter", "Miner", "Scout", "Villager",],
                  "Rangers": [ "Bounty Hunter", "Coachman", "Entertainer", "Messenger", "Pedlar",],
                  "Riverfolk": [ "Boatman", "Huffer", "Riverwoman", "Seaman", "Smuggler", "Stevedore", "Wrecker",],
                  "Rogues": [ "Fence", "Outlaw", "Racketeer", "Thief",],
                  "Warriors": [ "Guard", "Pit Fighter", "Protagonist", "Soldier", "Slayer",],
                  },

        "Halfling": {
                     "Academics": [ "Apothecary", "Engineer", "Lawyer", "Physician", "Scholar",],
                     "Burghers": [ "Agitator", "Artisan", "Beggar", "Investigator", "Merchant", "Rat Catcher", "Townsman", "Watchman",],
                     "Courtiers": [ "Advisor", "Artist", "Envoy", "Servant", "Spy", "Warden",],
                     "Peasants": [ "Bailiff", "Herbalist", "Hunter", "Miner", "Scout", "Villager",],
                     "Rangers": [ "Bounty Hunter", "Coachman", "Entertainer", "Messenger", "Pedlar", "Roadwarden",],
                     "Riverfolk": [ "Boatman", "Huffer", "Riverwarden", "Riverwoman", "Seaman", "Smuggler", "Stevedore",],
                     "Rogues": [ "Bawd", "Charlatan", "Fence", "Grave Robber", "Outlaw", "Racketeer", "Thief",],
                     "Warriors": [ "Guard", "Pit Fighter", "Soldier",],
                     },

        "High Elf": {
                     "Academics": [ "Apothecary", "Lawyer", "Physician", "Scholar", "Wizard",],
                     "Burghers": [ "Artisan", "Investigator", "Merchant", "Townsman", "Watchman",],
                     "Courtiers": [ "Advisor", "Artist", "Duellist", "Envoy", "Noble", "Spy", "Warden",],
                     "Peasants": [ "Herbalist", "Hunter", "Scout",],
                     "Rangers": [ "Bounty Hunter", "Entertainer", "Messenger",],
                     "Riverfolk": [ "Boatman", "Seaman", "Smuggler",],
                     "Rogues": [ "Bawd", "Charlatan", "Outlaw",],
                     "Warriors": [ "Cavalryman", "Guard", "Knight", "Pit Fighter", "Protagonist", "Soldier",],
                     },

        "Wood Elf": {
                     "Academics": [ "Scholar", "Wizard",],
                     "Burghers": [ "Artisan",],
                     "Courtiers": [ "Advisor", "Artist", "Envoy", "Noble", "Spy", "Warden",],
                     "Peasants": [ "Herbalist", "Hunter", "Mystic", "Scout",],
                     "Rangers": [ "Bounty Hunter", "Entertainer", "Messenger",],
                     "Riverfolk": [ "Wrecker",],
                     "Rogues": [ "Outlaw",],
                     "Warriors": [ "Cavalryman", "Guard", "Knight", "Pit Fighter", "Soldier",],
                     },

    }
