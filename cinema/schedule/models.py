from django.db import models
from cinema.catalog.models import Movie


class Hall(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Seance(models.Model):
    time = models.DateTimeField(null=False)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    film = models.OneToOneField(Movie)

    def __str__(self):
        return self.film.title + " " + self.hall.name
