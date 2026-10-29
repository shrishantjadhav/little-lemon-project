document.addEventListener("DOMContentLoaded", () => {
    const dateInput = document.getElementById("id_reservation_date");
    const slotSelect = document.getElementById("id_reservation_slot");
    const status = document.getElementById("reservation-status");
    const list = document.getElementById("reservation-list");
    const form = document.getElementById("booking-form");

    if (!dateInput || !slotSelect) return;

    // Default to today's local date if the date field is empty.
    if (!dateInput.value) {
        const now = new Date();
        const localDate = new Date(now.getTime() - now.getTimezoneOffset() * 60000)
            .toISOString().slice(0, 10);
        dateInput.value = localDate;
    }

    async function refreshBookings() {
        const selectedDate = dateInput.value;
        if (!selectedDate) return;

        status.textContent = "Loading reservations…";
        list.replaceChildren();

        try {
            const response = await fetch(`/bookings?date=${encodeURIComponent(selectedDate)}`);
            if (!response.ok) throw new Error("Could not load bookings.");
            const bookings = await response.json();

            // Refresh disabled time slots based on the selected date.
            const slotResponse = await fetch(`/booking-data/?date=${encodeURIComponent(selectedDate)}`);
            if (!slotResponse.ok) throw new Error("Could not load available slots.");
            const slotData = await slotResponse.json();
            const booked = new Set(slotData.booked_slots.map(Number));

            for (const option of slotSelect.options) {
                const isBooked = booked.has(Number(option.value));
                option.disabled = isBooked;
                option.textContent = `${String(option.value).padStart(2, "0")}:00${isBooked ? " — Booked" : ""}`;
            }

            if (bookings.length === 0) {
                status.textContent = "No Booking";
                return;
            }

            status.textContent = `Reservations for ${selectedDate}`;
            for (const booking of bookings) {
                const item = document.createElement("li");
                const hour = String(booking.reservation_slot).padStart(2, "0");
                item.textContent = `${booking.first_name} — ${hour}:00`;
                list.appendChild(item);
            }
        } catch (error) {
            status.textContent = "Unable to load reservations. Please refresh the page.";
        }
    }

    dateInput.addEventListener("change", refreshBookings);
    refreshBookings();

    form.addEventListener("submit", (event) => {
        const chosen = slotSelect.selectedOptions[0];
        if (chosen && chosen.disabled) {
            event.preventDefault();
            status.textContent = "That slot is already booked. Please choose another.";
        }
    });
});
