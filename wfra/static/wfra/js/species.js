document.addEventListener("DOMContentLoaded", function () {
    const speciesSelect = document.getElementById("id_species");
    const classSelect = document.getElementById("id_character_class");
    const careerSelect = document.getElementById("id_career");

    const careerPath = document.getElementById("id_career_path");
    careerPath.readOnly = true;
    const status = document.getElementById("id_status");
    status.readOnly = true;
    const careerTier = document.getElementById("id_career_tier");

    const classOptions = ["Academics", "Burghers", "Courtiers", "Peasants", "Rangers", "Riverfolk", "Rogues", "Warriors"]

    let careerOptions = {};
    fetch('/api/career-options/')
    .then(response => response.json())
    .then(data => {
        careerOptions = data;

        updateClasses();
        updateCareer();
    });

    let careerPaths = {};
    fetch('/api/career-paths/')
    .then(response => response.json())
    .then(data => {
        careerPaths = data;
        //console.log(careerPaths);
        //careerTier.value = 1

        //updateClasses();
        updatePath();
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

    function updatePath() {
        const selectedClass = careerSelect.value;
        const selectedTier = careerTier.value
        //console.log(careerPaths[selectedClass][selectedTier])
        careerPath.value = careerPaths[selectedClass][selectedTier][0]
        status.value = careerPaths[selectedClass][selectedTier][1]
    }

    speciesSelect.addEventListener("change", updateClasses);
    speciesSelect.addEventListener("change", updateCareer);
    classSelect.addEventListener("change", updateCareer);

    careerTier.addEventListener("change", updatePath);
    careerSelect.addEventListener("change", updatePath);
    classSelect.addEventListener("change", updatePath);
    speciesSelect.addEventListener("change", updatePath);
});