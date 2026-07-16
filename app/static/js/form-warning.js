// Find the form on the page
const form = document.querySelector("form");

// Only run on pages that contain a form
if (form) {

    let isDirty = false;

    // Watch every input and select inside the form
    const fields = form.querySelectorAll("input, select, textarea");

    fields.forEach(field => {
        field.addEventListener("change", () => {
            isDirty = true;
        });
    });

    // User is saving, so don't warn
    form.addEventListener("submit", () => {
        isDirty = false;
    });

    // Warn before leaving the page
    window.addEventListener("beforeunload", (event) => {
        if (isDirty) {
            event.preventDefault();
            event.returnValue = "";
        }
    });
}