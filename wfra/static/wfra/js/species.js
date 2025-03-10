document.addEventListener("DOMContentLoaded", function () {
    const speciesSelect = document.getElementById("id_species");
    const classSelect = document.getElementById("id_character_class");

    const classOptions = {
        "Human": ["Scholar", "Priest", "Merchant", "Soldier"],
        "Dwarf": ["Scholar", "Slayer", "Merchant", "Engineer"],
        "Halfling": ["Scholar", "Thief", "Cook", "Entertainer"],
        "Wood Elf": ["Scholar", "Waywatcher", "Hunter", "Druid"],
        "High Elf": ["Scholar", "Mage", "Diplomat", "Swordmaster"]
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