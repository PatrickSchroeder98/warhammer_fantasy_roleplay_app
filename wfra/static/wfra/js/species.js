document.addEventListener("DOMContentLoaded", function () {
    const speciesSelect = document.getElementById("id_species");
    const classSelect = document.getElementById("id_character_class");
    const careerSelect = document.getElementById("id_career");

    const classOptions = ["Academics", "Burghers", "Courtiers", "Peasants", "Rangers", "Riverfolk", "Rogues", "Warriors"]

    let careerOptions = {};
    fetch('/api/career-options/')
    .then(response => response.json())
    .then(data => {
        careerOptions = data;
        console.log(careerOptions);

        updateClasses();
        updateCareer();
    });

    function updateClasses() {
        //const selectedSpecies = speciesSelect.value;
        const availableClasses = classOptions || ["Rogues"];

        classSelect.innerHTML = "";
        availableClasses.forEach(cls => {
            const option = document.createElement("option");
            option.value = cls;
            option.textContent = cls;
            classSelect.appendChild(option);
        });
    }

    function updateCareer() {
        const selectedSpecies = speciesSelect.value;
        const selectedClass = classSelect.value;

        if (!careerOptions[selectedSpecies]) {
            console.warn("Career options not loaded yet.");
            return;
        }

        const availableCareers = careerOptions[selectedSpecies][selectedClass] || ["Outlaw"];

        careerSelect.innerHTML = "";
        availableCareers.forEach(cls => {
            const option = document.createElement("option");
            option.value = cls;
            option.textContent = cls;
            careerSelect.appendChild(option);
        });
    }

    speciesSelect.addEventListener("change", updateClasses);
    speciesSelect.addEventListener("change", updateCareer);
    classSelect.addEventListener("change", updateCareer);

});