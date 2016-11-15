# from django.db import models

# Create your models here.
from django.db import models


class Genre(models.Model):
    description = models.CharField(max_length=140, null=True)

    def __str__(self):
        return self.description


class Movie(models.Model):
    title = models.CharField(max_length=50, null=True)
    original_title = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.DateField(null=True)
    director = models.CharField(max_length=140, null=True)
    cast = models.CharField(max_length=500, null=True)
    poster_url = models.CharField(max_length=100, null=True)
    trailer_url = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=1000, null=True)
    genres = models.ManyToManyField(Genre)
    _3D = models.BooleanField(default=False)

    def __str__(self):
        return self.title
