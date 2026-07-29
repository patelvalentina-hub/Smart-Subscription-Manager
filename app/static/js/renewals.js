const filterButtons = document.querySelectorAll(".renewal-filter");

const renewalSections = {
    overdue: document.getElementById("overdue-section"),
    "due-today": document.getElementById("due-today-section"),
    upcoming: document.getElementById("upcoming-section"),
};

filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const selectedFilter = button.dataset.renewalFilter;

        // Hide all sections
        Object.values(renewalSections).forEach((section) => {
            section.style.display = "none";
        });

        // Show selected section
        renewalSections[selectedFilter].style.display = "block";

        // Remove active style from all filters
        filterButtons.forEach((filterButton) => {
            filterButton.classList.remove("renewal-filter--active");
        });

        // Add active style to the clicked filter
        button.classList.add("renewal-filter--active");
    });
});