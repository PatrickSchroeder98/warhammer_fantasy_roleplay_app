document.addEventListener("DOMContentLoaded", function () {
    const speciesSelect = document.getElementById("id_species");
    const classSelect = document.getElementById("id_character_class");

    const classOptions = {
        "Human": ["Apothecary", "Engineer", "Lawyer", "Nun", "Physician", "Priest", "Scholar", "Wizard",
                  "Agitator", "Artisan", "Beggar", "Investigator", "Merchant", "Rat Catcher", "Townsman", "Watchman",
                  "Advisor", "Artist", "Duellist", "Envoy", "Noble", "Servant", "Spy", "Warden",
                  "Bailiff", "Hedge Witch", "Herbalist", "Hunter", "Miner", "Mystic", "Scout", "Villager"],

        "Dwarf": ["Apothecary", "Engineer", "Lawyer", "Physician", "Scholar",
                  "Agitator", "Artisan", "Beggar", "Investigator", "Merchant", "Rat Catcher", "Townsman", "Watchman",
                  "Advisor", "Artist", "Duellist", "Envoy", "Noble", "Servant", "Spy", "Warden",
                  "Bailiff", "Hunter", "Miner", "Scout", "Villager"],

        "Halfling": ["Apothecary", "Engineer", "Lawyer", "Physician", "Scholar",
                     "Agitator", "Artisan", "Beggar", "Investigator", "Merchant", "Rat Catcher", "Townsman", "Watchman",
                     "Advisor", "Artist", "Envoy", "Servant", "Spy", "Warden",
                     "Bailiff", "Herbalist", "Hunter", "Miner", "Scout", "Villager"],

        "High Elf": ["Apothecary", "Lawyer", "Physician", "Scholar", "Wizard",
                     "Artisan", "Investigator", "Merchant", "Townsman", "Watchman",
                     "Advisor", "Artist", "Duellist", "Envoy", "Noble", "Spy", "Warden",
                     "Herbalist", "Hunter", "Scout"],

        "Wood Elf": ["Scholar", "Wizard",
                     "Artisan",
                     "Advisor", "Artist", "Envoy", "Noble", "Spy", "Warden",
                     "Herbalist", "Hunter", "Mystic", "Scout"]

    };

    function updateClasses() {
        const selectedSpecies = speciesSelect.value;
        const availableClasses = classOptions[selectedSpecies] || ["Scholar"];

        classSelect.innerHTML = "";
        availableClasses.forEach(cls => {
            const option = document.createElement("option");
            option.value = cls;
            option.textContent = cls;
            classSelect.appendChild(option);
        });
    }

    speciesSelect.addEventListener("change", updateClasses);
    updateClasses();  // Run on page load to set the initial values
});