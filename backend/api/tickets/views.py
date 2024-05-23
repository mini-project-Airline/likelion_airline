from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Ticket
from .serializers import TicketSerializer
from api.flights.models import Flight
from django.core.paginator import Paginator

class TicketListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        page = request.query_params.get('page', 1)
        limit = request.query_params.get('limit', 10)
        tickets = Ticket.objects.filter(user=request.user).order_by('-id')
        paginator = Paginator(tickets, limit)
        serialized_tickets = TicketSerializer(paginator.page(page), many=True)

        response_data = {
            "totalItems": paginator.count,
            "totalPages": paginator.num_pages,
            "currentPage": page,
            "tickets": serialized_tickets.data
        }

        return Response(response_data)
    
    
class PurchaseTicketView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, ticket):
        try:
            flight_id = request.data['flightId']
            flight = Flight.objects.get(id=flight_id)
            ticket = Ticket.objects.create(user=request.user, flight=flight)
            serialized_ticket = TicketSerializer(ticket)
            response_data = {
                "message": "구매 완료",
                "ticket": serialized_ticket.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Flight.DoesNotExist:
            return Response({"message": "항공편이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        
class RefundTicketView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, ticketId):
        try:
            ticket = Ticket.objects.get(id=ticketId, user=request.user)
            ticket.delete()
            return Response({"message": "티켓이 환불되었습니다."}, status=status.HTTP_200_OK)
        except Ticket.DoesNotExist:
            return Response({"message": "티켓이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)