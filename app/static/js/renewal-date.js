const startDateInput = document.getElementById("start_date");
const billingFrequencySelect = document.getElementById("billing_frequency");
const nextRenewalDateInput = document.getElementById("next_renewal_date");

function calculateNextRenewalDate() {
    if (
        !startDateInput ||
        !billingFrequencySelect ||
        !nextRenewalDateInput ||
        !startDateInput.value ||
        !billingFrequencySelect.value
    ) {
        return;
    }

    const [year, month, day] = startDateInput.value
        .split("-")
        .map(Number);

    const nextDate = new Date(year, month - 1, day);

    switch (billingFrequencySelect.value) {
        case "Weekly":
            nextDate.setDate(nextDate.getDate() + 7);
            break;

        case "Monthly":
            nextDate.setMonth(nextDate.getMonth() + 1);
            break;

        case "Every 3 Months":
            nextDate.setMonth(nextDate.getMonth() + 3);
            break;

        case "Every 6 Months":
            nextDate.setMonth(nextDate.getMonth() + 6);
            break;

        case "Yearly":
            nextDate.setFullYear(nextDate.getFullYear() + 1);
            break;

        default:
            return;
    }

    const formattedYear = nextDate.getFullYear();
    const formattedMonth = String(nextDate.getMonth() + 1).padStart(2, "0");
    const formattedDay = String(nextDate.getDate()).padStart(2, "0");

    nextRenewalDateInput.value =
        `${formattedYear}-${formattedMonth}-${formattedDay}`;

    nextRenewalDateInput.dispatchEvent(new Event("change"));
}

if (
    startDateInput &&
    billingFrequencySelect &&
    nextRenewalDateInput
) {
    startDateInput.addEventListener(
        "change",
        calculateNextRenewalDate
    );

    billingFrequencySelect.addEventListener(
        "change",
        calculateNextRenewalDate
    );
}