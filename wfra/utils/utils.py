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
        "1": ["Thief-Taker", "Silver 1"],
        "2": ["Bounty Hunter", "Silver 3"],
        "3": ["Master Bounty Hunter", "Silver 5"],
        "4": ["Bounty Hunter-General", "Gold 1"],
    },

    "Coachman": {
        "1": ["Postilion", "Silver 1"],
        "2": ["Coachman", "Silver 2"],
        "3": ["Coach Master", "Silver 3"],
        "4": ["Route Master", "Silver 5"],
    },
    "Entertainer": {
        "1": ["Busker", "Brass 3"],
        "2": ["Entertainer", "Brass 5"],
        "3": ["Troubadour", "Silver 3"],
        "4": ["Troupe-Leader", "Gold 1"],
    },
    "Flagellant": {
        "1": ["Zealot", "Brass 0"],
        "2": ["Flagellant", "Brass 0"],
        "3": ["Penitent", "Brass 0"],
        "4": ["Prophet of Doom", "Brass 0"],
    },
    "Messenger": {
        "1": ["Runner", "Brass 3"],
        "2": ["Messenger", "Silver 1"],
        "3": ["Courier", "Silver 3"],
        "4": ["Courier-Captain", "Silver 5"],
    },
    "Pedlar": {
        "1": ["Vagabond", "Brass 1"],
        "2": ["Pedlar", "Brass 4"],
        "3": ["Master Pedlar", "Silver 1"],
        "4": ["Wandering Trader", "Silver 3"],
    },
    "Roadwarden": {
        "1": ["Toll Keeper", "Brass 5"],
        "2": ["Roadwarden", "Silver 2"],
        "3": ["Road Sergeant", "Silver 4"],
        "4": ["Road Captain", "Gold 1"],
    },
    "Witch Hunter": {
        "1": ["Interrogator", "Silver 1"],
        "2": ["Witch Hunter", "Silver 3"],
        "3": ["Inquisitor", "Silver 5"],
        "4": ["Witchfinder General", "Gold 1"],
    },

    # Riverfolk
    "Boatman": {
        "1": ["Boat-hand", "Silver 1"],
        "2": ["Boatman", "Silver 2"],
        "3": ["Bargeswain", "Silver 3"],
        "4": ["Barge Master", "Silver 5"],
    },

    "Huffer": {
        "1": ["Riverguide", "Brass 4"],
        "2": ["Huffer", "Silver 1"],
        "3": ["Pilot", "Silver 3"],
        "4": ["Master Pilot", "Silver 5"],
    },
    "Riverwarden": {
        "1": ["River Recruit", "Silver 1"],
        "2": ["Riverwarden", "Silver 2"],
        "3": ["Shipsword", "Silver 4"],
        "4": ["Shipsword Master", "Gold 1"],
    },
    "Riverwoman": {
        "1": ["Greenfish", "Brass 2"],
        "2": ["Riverwoman", "Brass 3"],
        "3": ["Riverwise", "Brass 5"],
        "4": ["River Elder", "Silver 2"],
    },
    "Seaman": {
        "1": ["Landsman", "Silver 1"],
        "2": ["Seaman", "Silver 3"],
        "3": ["Boatswain", "Silver 5"],
        "4": ["Ship's Master", "Gold 2"],
    },
    "Smuggler": {
        "1": ["River Runner", "Brass 2"],
        "2": ["Smuggler", "Brass 3"],
        "3": ["Master Smuggler", "Brass 5"],
        "4": ["Smuggler King", "Silver 2"],
    },
    "Stevedore": {
        "1": ["Dockhand", "Brass 3"],
        "2": ["Stevedore", "Silver 1"],
        "3": ["Foreman", "Silver 3"],
        "4": ["Dock Master", "Silver 5"],
    },
    "Wrecker": {
        "1": ["Cargo Scavenger", "Brass 2"],
        "2": ["Wrecker", "Brass 3"],
        "3": ["River Pirate", "Brass 5"],
        "4": ["Wrecker Captain", "Silver 2"],
    },

    # Rogues
    "Bawd": {
        "1": ["Hustler", "Brass 1"],
        "2": ["Bawd", "Brass 3"],
        "3": ["Procurer", "Silver 1"],
        "4": ["Ringleader", "Silver 3"],
    },

    "Charlatan": {
        "1": ["Swindler", "Brass 3"],
        "2": ["Charlatan", "Brass 5"],
        "3": ["Con Artist", "Silver 2"],
        "4": ["Scoundrel", "Silver 4"],
    },
    "Fence": {
        "1": ["Broker", "Silver 1"],
        "2": ["Fence", "Silver 2"],
        "3": ["Master Fence", "Silver 3"],
        "4": ["Black Marketeer", "Silver 4"],
    },
    "Grave Robber": {
        "1": ["Body Snatcher", "Brass 2"],
        "2": ["Grave Robber", "Brass 3"],
        "3": ["Tomb Robber", "Silver 1"],
        "4": ["Treasure Hunter", "Silver 5"],
    },
    "Outlaw": {
        "1": ["Brigand", "Brass 1"],
        "2": ["Outlaw", "Brass 2"],
        "3": ["Outlaw Chief", "Brass 4"],
        "4": ["Bandit King", "Silver 2"],
    },
    "Racketeer": {
        "1": ["Thug", "Brass 3"],
        "2": ["Racketeer", "Brass 5"],
        "3": ["Gang Boss", "Silver 3"],
        "4": ["Crime Lord", "Silver 5"],
    },
    "Thief": {
        "1": ["Prowler", "Brass 1"],
        "2": ["Thief", "Brass 3"],
        "3": ["Master Thief", "Brass 5"],
        "4": ["Cat Burglar", "Silver 3"],
    },
    "Witch": {
        "1": ["Hexer", "Brass 1"],
        "2": ["Witch", "Brass 2"],
        "3": ["Wyrd", "Brass 3"],
        "4": ["Warlock", "Brass 5"],
    },

    # Warriors
    "Cavalryman": {
        "1": ["Horseman", "Silver 2"],
        "2": ["Cavalryman", "Silver 4"],
        "3": ["Cavalry Sergeant", "Gold 1"],
        "4": ["Cavalry Officer", "Gold 2"],
    },

    "Guard": {
        "1": ["Sentry", "Silver 1"],
        "2": ["Guard", "Silver 2"],
        "3": ["Honour Guard", "Silver 3"],
        "4": ["Guard Officer", "Silver 5"],
    },
    "Knight": {
        "1": ["Squire", "Silver 3"],
        "2": ["Knight", "Silver 5"],
        "3": ["First Knight", "Gold 2"],
        "4": ["Knight of the Inner Circle", "Gold 4"],
    },
    "Pit Fighter": {
        "1": ["Pugilist", "Brass 4"],
        "2": ["Pit Fighter", "Silver 2"],
        "3": ["Pit Champion", "Silver 5"],
        "4": ["Pit Legend", "Gold 2"],
    },
    "Protagonist": {
        "1": ["Braggart", "Brass 2"],
        "2": ["Protagonist", "Silver 1"],
        "3": ["Hitman", "Silver 4"],
        "4": ["Assassin", "Gold 1"],
    },
    "Soldier": {
        "1": ["Recruit", "Silver 1"],
        "2": ["Soldier", "Silver 3"],
        "3": ["Sergeant", "Silver 5"],
        "4": ["Officer", "Gold 1"],
    },
    "Slayer": {
        "1": ["Troll Slayer", "Brass 2"],
        "2": ["Giant Slayer", "Brass 2"],
        "3": ["Dragon Slayer", "Brass 2"],
        "4": ["Daemon Slayer", "Brass 2"],
    },
    "Warrior Priest": {
        "1": ["Novitiate", "Brass 2"],
        "2": ["Warrior Priest", "Silver 2"],
        "3": ["Priest Sergeant", "Silver 3"],
        "4": ["Priest Captain", "Silver 4"],
    },
}
