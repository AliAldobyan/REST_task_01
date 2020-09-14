from rest_framework.generics import ListAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightListSerializer, BookingListSerializer


class FlightList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingList(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer
