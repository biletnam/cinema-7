from django.db import models
from cinema.schedule.models import Seance
from django.contrib.postgres import fields

class Booking(models.Model):
    price = models.FloatField()
    seance = models.OneToOneField(Seance)
    seats = fields.ArrayField(models.IntegerField(), max_length=10)

    def get_id(self):
        return self.id

    def get_movie(self):
        return self.seance.movie