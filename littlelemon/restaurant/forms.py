from django import forms
from .models import Booking

TIME_SLOTS = [(hour, f"{hour:02d}:00") for hour in range(10, 22)]


class BookingForm(forms.ModelForm):
    reservation_slot = forms.TypedChoiceField(
        choices=TIME_SLOTS,
        coerce=int,
        label="Reservation slot",
    )

    class Meta:
        model = Booking
        fields = ["first_name", "reservation_date", "reservation_slot"]
        widgets = {
            "reservation_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("reservation_date")
        slot = cleaned_data.get("reservation_slot")
        if date and slot is not None:
            existing = Booking.objects.filter(
                reservation_date=date, reservation_slot=slot
            )
            if self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise forms.ValidationError(
                    "That reservation slot is already booked. Please choose another."
                )
        return cleaned_data
