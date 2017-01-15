from django.db import models
from cinema.catalog.models import Movie
import datetime


class Hall(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Seance(models.Model):
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False, editable=False)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return self.movie.title + " " + self.hall.name

    def save(self, *args, **kwargs):
        self.end_time = self.start_time + datetime.timedelta(minutes = self.movie.duration)
        super(Seance, self).save(*args, **kwargs)
