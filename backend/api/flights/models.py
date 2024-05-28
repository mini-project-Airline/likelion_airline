from django.db import models

class Continent(models.Model):      # 대륙
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Country(models.Model):      # 국가
    name = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Airport(models.Model):      # 공항
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Airline(models.Model):      # 항공사
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FlightClass(models.Model):    # 좌석 등급
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Flight(models.Model):               # 항공편
    departure_date = models.DateField()
    arrival_date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gate = models.CharField(max_length=50)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    destination_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    flight_class = models.ForeignKey(FlightClass, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.airline} - {self.departure_airport} to {self.destination_airport}"
