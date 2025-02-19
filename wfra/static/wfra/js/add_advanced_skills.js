document.getElementById("add-skill").addEventListener("click", function () {
    const formContainer = document.getElementById("formset-container");
    const totalForms = document.querySelector("#id_form-TOTAL_FORMS");
    const currentFormCount = parseInt(totalForms.value);
    const newFormIndex = currentFormCount;

    // Clone the first form in the formset
    const emptyForm = formContainer.querySelector(".formset-item").cloneNode(true);

    // Update the names and IDs of the cloned form
    emptyForm.querySelectorAll("input, select, textarea").forEach((input) => {
        if (input.name) {
            input.name = input.name.replace(`-0-`, `-${newFormIndex}-`);
        }
        if (input.id) {
            input.id = input.id.replace(`-0-`, `-${newFormIndex}-`);
        }
        input.value = ""; // Clear any existing value
    });

    // Append the new form and update the total forms count
    formContainer.appendChild(emptyForm);
    totalForms.value = currentFormCount + 1;
});

document.addEventListener("click", function (event) {
    const totalForms = document.querySelector("#id_form-TOTAL_FORMS");
    const currentFormCount = parseInt(totalForms.value);


    if (event.target && event.target.matches(".remove-skill")  ) {
        if (currentFormCount <= 1) {
            alert('Error! Cannot remove the only form from this field!');
            return ;
        }
        const formItem = event.target.closest(".formset-item");
        formItem.remove();
        const totalForms = document.querySelector("#id_form-TOTAL_FORMS");
        totalForms.value = parseInt(totalForms.value) - 1; // Decrement total forms count
    }

});