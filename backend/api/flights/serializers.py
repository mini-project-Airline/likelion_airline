from rest_framework import serializers
from .models import Flight, Airline, Airport, FlightClass

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['name']

class AirportSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()

    class Meta:
        model = Airport
        fields = ['name', 'code', 'country']

class FlightClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightClass
        fields = ['name']

class FlightSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer()
    departure_airport = AirportSerializer()
    destination_airport = AirportSerializer()
    flight_class = FlightClassSerializer()

    class Meta:
        model = Flight
        fields = ['id', 'departure_date', 'arrival_date', 'departure_time', 'arrival_time', 'price', 'gate', 'airline', 'departure_airport', 'destination_airport', 'flight_class']
