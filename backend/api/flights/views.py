from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Flight
from .serializers import FlightSerializer
from django.core.paginator import Paginator
from django.db.models import Q

class FlightListView(APIView):
    def get(self, request):
        departures = request.GET.get('departures')
        arrivals = request.GET.get('arrivals')
        departure_date = request.GET.get('departure_date')
        arrival_date = request.GET.get('arrival_date')
        flight_class = request.GET.get('flightClass')
        airline = request.GET.get('airline')
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 5)

        flights = Flight.objects.all()

        if departures:
            flights = flights.filter(departure_airport__name__icontains=departures)
        if arrivals:
            flights = flights.filter(destination_airport__name__icontains=arrivals)
        if departure_date:
            flights = flights.filter(departure_date=departure_date)
        if arrival_date:
            flights = flights.filter(arrival_date=arrival_date)
        if flight_class:
            flights = flights.filter(flight_class__name__icontains=flight_class)
        if airline:
            flights = flights.filter(airline__name__icontains=airline)

        paginator = Paginator(flights, limit)
        serialized_flights = FlightSerializer(paginator.page(page), many=True)

        response_data = {
            "totalItems": paginator.count,
            "totalPages": paginator.num_pages,
            "currentPage": int(page),
            "flights": serialized_flights.data
        }

        return Response(response_data)
