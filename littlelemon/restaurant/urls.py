from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("book/", views.book, name="book"),
    path("reservations/", views.reservations, name="reservations"),
    path("bookings", views.bookings, name="bookings"),
    path("booking-data/", views.booking_page_data, name="booking_page_data"),
]
