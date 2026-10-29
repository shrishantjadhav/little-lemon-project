from rest_framework import permissions, viewsets
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by("id")
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by("booking_date")
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
