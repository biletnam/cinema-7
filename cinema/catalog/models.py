# from django.db import models

# Create your models here.
from django.db import models
from django.utils.crypto import get_random_string
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.contrib.contenttypes.fields import GenericRelation
from bs4 import BeautifulSoup
from star_ratings.models import Rating
import urllib.request
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

    def get_kinopoisk_id(self):
        request_string = "https://www.kinopoisk.ru/index.php?first=no&kp_query=%s" % urllib.parse.quote(self.title)
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9.1.8) Gecko/20100214 Linux Mint/8 (Helena) Firefox/'
                      '3.5.8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'ru,en-us;q=0.7,en;q=0.3',
        'Accept-Encoding': 'deflate',
        'Accept-Charset': 'windows-1251,utf-8;q=0.7,*;q=0.7',
        'Keep-Alive': '300',
        'Connection': 'keep-alive',
        'Referer': 'http://www.kinopoisk.ru/',
        'Cookie': 'users_info[check_sh_bool]=none; search_last_date=2010-02-19; search_last_month=2010-02;'
                  '                                        PHPSESSID=b6df76a958983da150476d9cfa0aab18',
        }
        req = urllib.request.Request(request_string, data = None, headers = headers)
        res = urllib.request.urlopen(req)
        soup = BeautifulSoup(res, "html.parser")
        movie_list = soup.findAll("div", {"class": "element"})
        for element in movie_list:
            year = element.find('div', {'class': 'info'}).find('p', {'class': 'name'}).find('span', {'class': 'year'}).string
            if int(year) == self.release_date.year:
                id = element.find('div', {'class': 'info'}).find('p', {'class': 'name'}).find('a').get('data-id')
                return id
        return None


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
    kinopoisk_id = models.IntegerField(editable=False, null=True)
    rating = GenericRelation(Rating, related_query_name='rating')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.kinopoisk_id is None:
            self.kinopoisk_id = self.get_kinopoisk_id()
            super(Movie, self).save(*args, **kwargs)


class Image(models.Model):
    movie = models.ForeignKey(Movie)
    image = models.ImageField(blank=True, verbose_name="image")


@receiver(post_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(post_delete, sender=Movie)
def poster_delete(sender, instance, **kwargs):
    instance.poster.delete(False)
