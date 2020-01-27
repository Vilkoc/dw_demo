from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BoardingPasses, Flights, Bookings, Tickets, TicketFlights, Seats


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BoardingPassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardingPasses
        fields = '__all__'


class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'


class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = '__all__'


class TicketFlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketFlights
        fields = '__all__'


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'


# class FlightsViewSerializer(serializers.ModelSerializer):
#     airports = serializers.PrimaryKeyRelatedField(queryset=AirportsData.objects.all())
#     class Meta:
#         model = Flights
#         fields = '__all__'


# class FlightsViewSerializer(serializers.ModelSerializer):
#     flight_id = serializers.IntegerField(read_only=True)
#     flight_no = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     scheduled_departure = serializers.DateTimeField(style={'base_template': 'textarea.html'})
#     scheduled_arrival = serializers.DateTimeField(style={'base_template': 'textarea.html'})
#     departure_airport = serializers.CharField()
#     arrival_airport = serializers.CharField()
#     status = serializers.ChoiceField()
#     aircraft_code = serializers.CharField()
#     actual_departure = serializers.DateTimeField()
#     actual_arrival = serializers.DateTimeField()

