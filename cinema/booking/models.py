from django.db import models
from cinema.schedule.models import Seance, Row, Hall, Seat, Seat_new
from django.contrib.postgres import fields
from django.conf import settings
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Booking(models.Model):
    price = models.FloatField()
    seance = models.ForeignKey(Seance)
    seats = fields.ArrayField(models.TextField(), max_length=10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

    def str_seats(self):
        return_string = ""
        for seat in self.seats:
            return_string += (str(seat) + ", ")
        return(return_string)

    def __str__(self):
        return("Booking: " + str(self.id) + " " + self.seance.movie.title + " " + self.str_seats())

    def get_id(self):
        return self.id

    def get_movie(self):
        return self.seance.movie


@receiver(pre_delete, sender=Booking)
def booking_delete(sender, instance, **kwargs):
    seance = instance.seance
    hall = seance.hall
    for seat in instance.seats:
        indices = seat.split("_")
        row = Row.objects.filter(hall=hall, number=int(indices[0]))
        number = int(indices[1])
        Seat.objects.filter(seance=seance, hall=hall, row=row, number=number).update(booked=False)


class Booking_new(models.Model):
    price = models.FloatField()
    seance = models.ForeignKey(Seance)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

    def str_seats(self):
        return_string = ""
        for seat in self.seats:
            return_string += (str(seat) + ", ")
        return(return_string)

    def __str__(self):
        return("Booking: " + str(self.id) + " " + self.seance.movie.title + " " + self.str_seats())

    def get_id(self):
        return self.id

    def get_movie(self):
        return self.seance.movie


@receiver(pre_delete, sender=Booking_new)
def booking_new_delete(sender, instance, **kwargs):
    queryset = Seat_new.objects.filter(booking=sender)
    for seat in queryset:
        seat.set_null_booking()