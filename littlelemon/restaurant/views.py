import json
from datetime import date
from django.db import IntegrityError, transaction
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods
from .forms import BookingForm, TIME_SLOTS
from .models import Booking


def home(request):
    return render(request, "restaurant/home.html")


@require_http_methods(["GET", "POST"])
def book(request):
    message = ""
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                return redirect("book")
            except IntegrityError:
                message = "That slot was just booked. Please choose another."
    else:
        form = BookingForm(initial={"reservation_date": date.today()})

    selected_date = request.POST.get("reservation_date") or date.today().isoformat()
    booked_slots = list(
        Booking.objects.filter(reservation_date=selected_date)
        .values_list("reservation_slot", flat=True)
    )
    return render(
        request,
        "restaurant/book.html",
        {
            "form": form,
            "message": message,
            "time_slots": TIME_SLOTS,
            "booked_slots": booked_slots,
            "selected_date": selected_date,
        },
    )


@require_GET
def reservations(request):
    # All reservations are returned as JSON.
    return bookings(request)


@require_GET
def bookings(request):
    selected_date = request.GET.get("date")
    queryset = Booking.objects.all()
    if selected_date:
        try:
            date.fromisoformat(selected_date)
        except ValueError:
            return JsonResponse({"error": "Use date format YYYY-MM-DD."}, status=400)
        queryset = queryset.filter(reservation_date=selected_date)

    data = [
        {
            "id": booking.id,
            "first_name": booking.first_name,
            "reservation_date": booking.reservation_date.isoformat(),
            "reservation_slot": booking.reservation_slot,
        }
        for booking in queryset.order_by("reservation_date", "reservation_slot")
    ]
    return JsonResponse(data, safe=False)


@require_GET
def booking_page_data(request):
    selected_date = request.GET.get("date", date.today().isoformat())
    try:
        date.fromisoformat(selected_date)
    except ValueError:
        return JsonResponse({"error": "Use date format YYYY-MM-DD."}, status=400)
    booked_slots = list(
        Booking.objects.filter(reservation_date=selected_date)
        .values_list("reservation_slot", flat=True)
    )
    return JsonResponse({"date": selected_date, "booked_slots": booked_slots})
