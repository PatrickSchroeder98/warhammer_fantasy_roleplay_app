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

CAREER_PATHS = {
    # Academics
    "Apothecary": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    "Engineer": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Lawyer": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Nun": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Physician": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Priest": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Scholar": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Wizard": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    # Burghers
    "Agitator": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    "Artisan": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Beggar": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Investigator": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Merchant": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Rat Catcher": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Townsman": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Watchman": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    # Courtiers
    "Advisor": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    "Artist": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Duellist": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Envoy": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Noble": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Servant": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Spy": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Warden": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    # Peasants
    "Bailiff": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    "Hedge Witch": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Herbalist": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Hunter": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Miner": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Mystic": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Scout": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Villager": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
}