from django.db import models
from cinema.schedule.models import Seance
from django.contrib.postgres import fields
from django.conf import settings


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