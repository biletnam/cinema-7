# from django.db import models

# Create your models here.
from django.db import models


class Movies(models.Model):
    movie_id = models.BigIntegerField
    title = models.CharField(max_length=20, null=True)
    original_title = models.CharField(max_length=20, null=True)
    year = models.IntegerField(null=True)
    director = models.CharField(max_length=140, null=True)
    cast = models.SmallIntegerField(null=True)
    poster_url = models.CharField(max_length=50, null=True)
    trailer_url = models.CharField(max_length=50, null=True)
    summary = models.CharField(max_length=140, null=True)
    format = models.SmallIntegerField(null=True)


class MovieGenre(models.Model):
    mg_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    movie = models.BigIntegerField(null=True)
    genre = models.BigIntegerField(null=True)


class Genres(models.Model):
    genre_id = models.ForeignKey(MovieGenre, on_delete=models.CASCADE)
    description = models.CharField(max_length=140, null=True)
