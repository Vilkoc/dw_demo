from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

from rest_framework import viewsets, generics, views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

from .models import BoardingPasses, Flights, Bookings, Tickets, TicketFlights, Seats
from .serializers import UserSerializer, BoardingPassesSerializer, FlightsSerializer, BookingsSerializer, TicketsSerializer, TicketFlightsSerializer, SeatsSerializer#, FlightsViewSerializer
import pdb


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BoardingPassesViews(views.APIView):
    def get_object(self, ticket_no, flight_id):
        try:
            return BoardingPasses.objects.get(ticket_no=ticket_no, flight_id=flight_id)
        except:
            raise Http404

    def get(self, request, ticket_no, flight_id, format=None):
        boarding_pass = self.get_object(ticket_no, flight_id)
        serializer = BoardingPassesSerializer(boarding_pass)
        return Response(serializer.data)

    def put(self, request, ticket_no, flight_id, format=None):
        boarding_pass = self.get_object(ticket_no, flight_id)
        serializer = BoardingPassesSerializer(boarding_pass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ticket_no, flight_id, format=None):
        boarding_pass = self.get_object(ticket_no, flight_id)
        boarding_pass.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlightsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializer


class Bookings(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer


class SeatsDetail(views.APIView):
    def get_object(self, aircraft_code, seat_no):
        try:
            return Seats.objects.get(aircraft_code=aircraft_code, seat_no=seat_no)
        except:
            raise Http404

    def get(self, request, aircraft_code, seat_no, format=None):
        seats = self.get_object(aircraft_code, seat_no)
        serializer = SeatsSerializer(seats)
        return Response(serializer.data)

    def put(self, request, aircraft_code, seat_no, format=None):
        seat = self.get_object(aircraft_code, seat_no)
        serializer = SeatsSerializer(seat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, aircraft_code, seat_no, format=None):
        seat = self.get_object(aircraft_code, seat_no)
        seat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TicketFlights(viewsets.ModelViewSet):
    queryset = TicketFlights.objects.all()
    serializer_class = TicketFlightsSerializer


class Tickets(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


# class FlightsViewView(views.APIView):
#     def get_object(self, pk):
#         try:
#             return Flights.objects.get(pk=pk)
#         except:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         flight = self.get_object(pk)
#         airport
#         serializer = FlightsSerializer(flight)
#         return Response(serializer.data)
#
#     def put(self, request, aircraft_code, seat_no, format=None):
#         seat = self.get_object(aircraft_code, seat_no)
#         serializer = SeatsSerializer(seat, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, aircraft_code, seat_no, format=None):
#         seat = self.get_object(aircraft_code, seat_no)
#         seat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#





