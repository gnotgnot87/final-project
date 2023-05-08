from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from restaurant.api.serializers import (BookingSerializer,
                                        MenuCategorySerializer,
                                        MenuItemSerializer)
from restaurant.models import Booking, MenuCategory, MenuItem


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(
    generics.RetrieveUpdateAPIView, generics.DestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
