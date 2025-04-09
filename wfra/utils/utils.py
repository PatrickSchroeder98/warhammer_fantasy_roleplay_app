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
        "1": ["Student Engineer", "Brass 4"],
        "2": ["Engineer", "Silver 2"],
        "3": ["Master Engineer", "Silver 4"],
        "4": ["Chartered Engineer", "Gold 2"],
    },
    "Lawyer": {
        "1": ["Student Lawyer", "Brass 4"],
        "2": ["Lawyer", "Silver 3"],
        "3": ["Barrister", "Gold 1"],
        "4": ["Judge", "Gold 2"],
    },
    "Nun": {
        "1": ["Novitiate", "Brass 1"],
        "2": ["Nun", "Brass 4"],
        "3": ["Abbess", "Silver 2"],
        "4": ["Prioress General", "Silver 5"],
    },
    "Physician": {
        "1": ["Physician's Apprentice", "Brass 4"],
        "2": ["Physician", "Silver 3"],
        "3": ["Doktor", "Silver 5"],
        "4": ["Court Physician", "Gold 1"],
    },
    "Priest": {
        "1": ["Initiate", "Brass 2"],
        "2": ["Priest", "Silver 1"],
        "3": ["High Priest", "Gold 1"],
        "4": ["Lector", "Gold 2"],
    },
    "Scholar": {
        "1": ["Student", "Brass 3"],
        "2": ["Scholar", "Silver 2"],
        "3": ["Fellow", "Silver 5"],
        "4": ["Professor", "Gold 1"],
    },
    "Wizard": {
        "1": ["Wizard's Apprentice", "Brass 3"],
        "2": ["Wizard", "Silver 3"],
        "3": ["Master Wizard", "Gold 1"],
        "4": ["Wizard Lord", "Gold 2"],
    },

    # Burghers
    "Agitator": {
        "1": ["Pamphleteer", "Brass 1"],
        "2": ["Agitator", "Brass 2"],
        "3": ["Rabble Rouser", "Brass 3"],
        "4": ["Demagogue", "Brass 5"],
    },

    "Artisan": {
        "1": ["Apprentice Artisan", "Brass 2"],
        "2": ["Artisan", "Silver 1"],
        "3": ["Master Artisan", "Silver 3"],
        "4": ["Guildmaster", "Gold 1"],
    },
    "Beggar": {
        "1": ["Pauper", "Brass 0"],
        "2": ["Beggar", "Brass 2"],
        "3": ["Master Beggar", "Brass 4"],
        "4": ["Beggar King", "Silver 2"],
    },
    "Investigator": {
        "1": ["Sleuth", "Silver 1"],
        "2": ["Investigator", "Silver 2"],
        "3": ["Master Investigator", "Silver 3"],
        "4": ["Detective", "Silver 5"],
    },
    "Merchant": {
        "1": ["Trader", "Silver 2"],
        "2": ["Merchant", "Silver 5"],
        "3": ["Master Merchant", "Gold 1"],
        "4": ["Merchant Prince", "Gold 3"],
    },
    "Rat Catcher": {
        "1": ["Rat Hunter", "Brass 3"],
        "2": ["Rat Catcher", "Silver 1"],
        "3": ["Sewer Jack", "Silver 2"],
        "4": ["Exterminator", "Silver 3"],
    },
    "Townsman": {
        "1": ["Clerk", "Silver 1"],
        "2": ["Townsman", "Silver 2"],
        "3": ["Town Councillor", "Silver 5"],
        "4": ["Burgomeister", "Gold 1"],
    },
    "Watchman": {
        "1": ["Watch Recruit", "Brass 3"],
        "2": ["Watchman", "Silver 1"],
        "3": ["Watch Sergeant", "Silver 3"],
        "4": ["Watch Captain", "Gold 1"],
    },

    # Courtiers
    "Advisor": {
        "1": ["Aide", "Silver 2"],
        "2": ["Advisor", "Silver 4"],
        "3": ["Counsellor", "Gold 1"],
        "4": ["Chancellor", "Gold 3"],
    },

    "Artist": {
        "1": ["Apprentice Artist", "Silver 1"],
        "2": ["Artist", "Silver 3"],
        "3": ["Master Artist", "Silver 5"],
        "4": ["Maestro", "Gold 2"],
    },
    "Duellist": {
        "1": ["Fencer", "Silver 3"],
        "2": ["Duellist", "Silver 5"],
        "3": ["Duelmaster", "Gold 1"],
        "4": ["Judicial Champion", "Gold 3"],
    },
    "Envoy": {
        "1": ["Herald", "Silver 2"],
        "2": ["Envoy", "Silver 4"],
        "3": ["Diplomat", "Gold 2"],
        "4": ["Ambassador", "Gold 5"],
    },
    "Noble": {
        "1": ["Scion", "Gold 1"],
        "2": ["Noble", "Gold 3"],
        "3": ["Magnate", "Gold 5"],
        "4": ["Noble Lord", "Gold 7"],
    },
    "Servant": {
        "1": ["Menial", "Silver 1"],
        "2": ["Servant", "Silver 3"],
        "3": ["Attendant", "Silver 5"],
        "4": ["Steward", "Gold 1"],
    },
    "Spy": {
        "1": ["Informer", "Brass 3"],
        "2": ["Spy", "Silver 3"],
        "3": ["Agent", "Gold 1"],
        "4": ["Spymaster", "Gold 4"],
    },
    "Warden": {
        "1": ["Custodian", "Silver 1"],
        "2": ["Warden", "Silver 3"],
        "3": ["Seneschal", "Gold 1"],
        "4": ["Governor", "Gold 3"],
    },

    # Peasants
    "Bailiff": {
        "1": ["Tax Collector", "Silver 1"],
        "2": ["Bailiff", "Silver 5"],
        "3": ["Reeve", "Gold 1"],
        "4": ["Magistrate", "Gold 3"],
    },

    "Hedge Witch": {
        "1": ["Hedge Apprentice", "Brass 1"],
        "2": ["Hedge Witch", "Brass 2"],
        "3": ["Hedge Master", "Brass 3"],
        "4": ["Hedgewise", "Brass 5"],
    },
    "Herbalist": {
        "1": ["Herb Gatherer", "Brass 2"],
        "2": ["Herbalist", "Brass 4"],
        "3": ["Herb Master", "Silver 1"],
        "4": ["Herbwise", "Silver 3"],
    },
    "Hunter": {
        "1": ["Trapper", "Brass 2"],
        "2": ["Hunter", "Brass 4"],
        "3": ["Tracker", "Silver 1"],
        "4": ["Huntsmaster", "Silver 3"],
    },
    "Miner": {
        "1": ["Prospector", "Brass 2"],
        "2": ["Miner", "Brass 4"],
        "3": ["Master Miner", "Brass 5"],
        "4": ["Mine Foreman", "Silver 4"],
    },
    "Mystic": {
        "1": ["Fortune Teller", "Brass 1"],
        "2": ["Mystic", "Brass 2"],
        "3": ["Sage", "Brass 3"],
        "4": ["Seer", "Brass 4"],
    },
    "Scout": {
        "1": ["Guide", "Brass 3"],
        "2": ["Scout", "Brass 5"],
        "3": ["Pathfinder", "Silver 1"],
        "4": ["Explorer", "Silver 5"],
    },
    "Villager": {
        "1": ["Peasant", "Brass 2"],
        "2": ["Villager", "Brass 3"],
        "3": ["Councillor", "Brass 4"],
        "4": ["Village Elder", "Silver 2"],
    },

    # Rangers
    "Bounty Hunter": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    "Coachman": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Entertainer": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Flagellant": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Messenger": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Pedlar": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Roadwarden": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Witch Hunter": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    # Riverfolk
    "Boatman": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    "Huffer": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Riverwarden": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Riverwoman": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Seaman": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Smuggler": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Stevedore": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Wrecker": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    # Rogues
    "Bawd": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    "Charlatan": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Fence": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Grave Robber": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Outlaw": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Racketeer": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Thief": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Witch": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    # Warriors
    "Cavalryman": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },

    "Guard": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Knight": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Pit Fighter": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Protagonist": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Soldier": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Slayer": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
    "Warrior Priest": {
        "1": ["Apothecary's Apprentice", "Brass 3"],
        "2": ["Apothecary", "Silver 1"],
        "3": ["Master Apothecary", "Silver 3"],
        "4": ["Apothecary-General", "Gold 1"],
    },
}
