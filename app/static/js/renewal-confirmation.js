const amountInput = document.getElementById("amount");
const frequencyInput = document.getElementById("billing_frequency");
const renewedOnInput = document.getElementById("renewed_on");

const summaryAmount = document.getElementById("summary-amount");
const summaryFrequency = document.getElementById("summary-frequency");
const summaryRenewedDate = document.getElementById(
    "summary-renewed-date"
);
const summaryNextDate = document.getElementById(
    "summary-next-date"
);

function formatDate(date) {
    return date.toLocaleDateString("en-GB", {
        day: "2-digit",
        month: "short",
        year: "numeric",
    });
}

function calculateNextRenewalDate(
    renewedOn,
    billingFrequency
) {
    const nextDate = new Date(renewedOn);

    if (billingFrequency === "Weekly") {
        nextDate.setDate(nextDate.getDate() + 7);
    } else if (billingFrequency === "Monthly") {
        nextDate.setMonth(nextDate.getMonth() + 1);
    } else if (billingFrequency === "Every 3 Months") {
        nextDate.setMonth(nextDate.getMonth() + 3);
    } else if (billingFrequency === "Every 6 Months") {
        nextDate.setMonth(nextDate.getMonth() + 6);
    } else if (billingFrequency === "Yearly") {
        nextDate.setFullYear(nextDate.getFullYear() + 1);
    } else {
        return null;
    }

    return nextDate;
}

function updateRenewalSummary() {
    const amount = Number.parseFloat(amountInput.value);
    const frequency = frequencyInput.value;
    const renewedOnValue = renewedOnInput.value;

    summaryAmount.textContent = Number.isNaN(amount)
        ? "฿0.00"
        : `฿${amount.toFixed(2)}`;

    summaryFrequency.textContent = frequency;

    if (!renewedOnValue) {
        summaryRenewedDate.textContent = "Select a date";
        summaryNextDate.textContent = "Select a date";
        return;
    }

    const renewedOn = new Date(`${renewedOnValue}T00:00:00`);

    summaryRenewedDate.textContent = formatDate(renewedOn);

    const nextRenewalDate = calculateNextRenewalDate(
        renewedOn,
        frequency
    );

    summaryNextDate.textContent = nextRenewalDate
        ? formatDate(nextRenewalDate)
        : "Unable to calculate";
}

amountInput.addEventListener("input", updateRenewalSummary);
frequencyInput.addEventListener("change", updateRenewalSummary);
renewedOnInput.addEventListener("change", updateRenewalSummary);

updateRenewalSummary();