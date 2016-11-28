# from django.db import models

# Create your models here.
from django.db import models
from django.utils.crypto import get_random_string
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
import os


class Genre(models.Model):
    description = models.CharField(max_length=140, null=True)

    def __str__(self):
        return self.description


class Movie(models.Model):
    def get_image_path(filename):
        ext = filename.split('.')[-1]
        random_name = get_random_string(length=16)
        filename = "%s.%s" % (random_name, ext)
        return os.path.join('images/', filename)

    title = models.CharField(max_length=50, null=True)
    original_title = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.DateField(null=True)
    director = models.CharField(max_length=140, null=True)
    cast = models.CharField(max_length=500, null=True)
    poster = models.ImageField(upload_to=get_image_path)
    trailer_url = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=1000, null=True)
    genres = models.ManyToManyField(Genre)
    _3D = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Image(models.Model):
    movie = models.ForeignKey(Movie)
    image = models.ImageField(blank=True, verbose_name="image")


@receiver(post_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(post_delete, sender=Movie)
def poster_delete(sender, instance, **kwargs):
    instance.poster.delete(False)
