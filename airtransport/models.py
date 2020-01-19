from django.db import models
from django.contrib.gis.db.models import PointField
from django.core.validators import RegexValidator, MinValueValidator
from django.contrib.postgres.fields import JSONField


class AircraftsData(models.Model):
    aircraft_code = models.CharField(primary_key=True, max_length=3,
                                     validators=[RegexValidator(regex='^.[3]$')])
    model = JSONField()
    range = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        managed = False
        db_table = 'aircrafts_data'


class AirportsData(models.Model):
    airport_code = models.CharField(primary_key=True, max_length=3,
                                    validators=[RegexValidator(regex='^.(3)$',
                                                               message='fixed length - 3 char')])
    airport_name = JSONField()
    city = JSONField()
    coordinates = PointField()
    timezone = models.TextField()

    class Meta:
        managed = False
        db_table = 'airports_data'


class BoardingPasses(models.Model):
    ticket_no = models.OneToOneField('TicketFlights', models.DO_NOTHING,
                                     db_column='ticket_no', primary_key=True)
    flight_id = models.ForeignKey('TicketFlights', models.DO_NOTHING,
                                  db_index=True, related_name='flight_id')
    boarding_no = models.IntegerField()
    seat_no = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'boarding_passes'
        unique_together = (('flight_id', 'boarding_no'),
                           ('flight_id', 'seat_no'),
                           ('ticket_no', 'flight_id'),)


class Bookings(models.Model):
    book_ref = models.CharField(primary_key=True, max_length=6)
    book_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'bookings'


class Flights(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_no = models.CharField(max_length=6)
    scheduled_departure = models.DateTimeField()
    scheduled_arrival = models.DateTimeField()
    departure_airport = models.ForeignKey(AirportsData, models.DO_NOTHING,
                                          db_column='departure_airport',
                                          related_name='departure_airport')
    arrival_airport = models.ForeignKey(AirportsData, models.DO_NOTHING,
                                        db_column='arrival_airport',
                                        related_name='arrival_airport')
    STATUS = (
        ('Scheduled', 'Scheduled'),
        ('On Time', 'On Time'),
        ('Delayed', 'Delayed'),
        ('Departed', 'Departed'),
        ('Arrived', 'Arrived'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=20, choices=STATUS)
    aircraft_code = models.ForeignKey(AircraftsData, models.DO_NOTHING, db_column='aircraft_code')
    actual_departure = models.DateTimeField(blank=True, null=True)
    actual_arrival = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flights'
        unique_together = (('flight_no', 'scheduled_departure'),)


class Seats(models.Model):
    aircraft_code = models.OneToOneField(AircraftsData, models.CASCADE,
                                         db_column='aircraft_code', primary_key=True)
    seat_no = models.CharField(max_length=4)
    CONDITION = (
        ('Economy', 'Economy'),
        ('Comfort', 'Comfort'),
        ('Business', 'Business'),
    )
    fare_conditions = models.CharField(max_length=10, choices=CONDITION)

    class Meta:
        managed = False
        db_table = 'seats'
        unique_together = (('aircraft_code', 'seat_no'),)


class TicketFlights(models.Model):
    ticket_no = models.OneToOneField('Tickets', models.DO_NOTHING,
                                     db_column='ticket_no', primary_key=True)
    flight = models.ForeignKey(Flights, models.DO_NOTHING, db_index=True)
    fare_conditions = models.CharField(max_length=10, choices=Seats.CONDITION)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        managed = False
        db_table = 'ticket_flights'
        unique_together = (('ticket_no', 'flight'),)


class Tickets(models.Model):
    ticket_no = models.CharField(primary_key=True, max_length=13)
    book_ref = models.ForeignKey(Bookings, models.DO_NOTHING, db_column='book_ref')
    passenger_id = models.CharField(max_length=20)
    passenger_name = models.TextField()
    contact_data = JSONField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'tickets'
