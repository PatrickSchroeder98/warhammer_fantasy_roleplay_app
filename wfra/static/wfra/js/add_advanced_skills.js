document.getElementById("add-skill").addEventListener("click", function () {
    const formContainer = document.getElementById("formset-container");
    const totalForms = formContainer.querySelector("input[name$='-TOTAL_FORMS']"); // Select correct management form field
    const currentFormCount = parseInt(totalForms.value);
    const newFormIndex = currentFormCount;

    // Clone the last form in the formset (ensures latest structure)
    const emptyForm = formContainer.querySelector(".formset-item").cloneNode(true);

    // Update the names and IDs of the cloned form
    emptyForm.querySelectorAll("input, select, textarea").forEach((input) => {
        if (input.name) {
            input.name = input.name.replace(/\d+/, newFormIndex); // Replace any existing number
        }
        if (input.id) {
            input.id = input.id.replace(/\d+/, newFormIndex);
        }
        input.value = ""; // Clear any existing value
    });

    // Append the new form and update the total forms count
    formContainer.appendChild(emptyForm);
    totalForms.value = currentFormCount + 1; // Increment total form count
});

document.getElementById("add-talent").addEventListener("click", function () {
    const formContainer = document.getElementById("formset-container-2");
    const totalForms = formContainer.querySelector("input[name$='-TOTAL_FORMS']"); // Select correct management form field
    const currentFormCount = parseInt(totalForms.value);
    const newFormIndex = currentFormCount;

    // Clone the last form in the formset
    const emptyForm = formContainer.querySelector(".formset-item").cloneNode(true);

    // Update the names and IDs of the cloned form
    emptyForm.querySelectorAll("input, select, textarea").forEach((input) => {
        if (input.name) {
            input.name = input.name.replace(/\d+/, newFormIndex);
        }
        if (input.id) {
            input.id = input.id.replace(/\d+/, newFormIndex);
        }
        input.value = ""; // Clear any existing value
    });

    // Append the new form and update the total forms count
    formContainer.appendChild(emptyForm);
    totalForms.value = currentFormCount + 1;
});

document.addEventListener("click", function (event) {
    if (event.target && event.target.matches(".remove-skill")) {
        const formContainer = event.target.closest(".formset-item").parentNode;
        const totalForms = formContainer.querySelector("input[name$='-TOTAL_FORMS']");
        const currentFormCount = parseInt(totalForms.value);

        if (currentFormCount <= 1) {
            alert('Error! Cannot remove the only form from this field!');
            return;
        }

        event.target.closest(".formset-item").remove();
        totalForms.value = currentFormCount - 1; // Decrement total form count
    }
});
