from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'departure', 'departure_airport', 'departure_airport_code', 'destination', 'destination_airport', 'destination_airport_code', 'departure_date', 'destination_date', 'departure_time', 'destination_time', 'duration', 'airline', 'flightClass', 'price']
