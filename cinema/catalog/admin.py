from django.contrib import admin

from .models import Movie
from .models import Genre
from .models import Image


class InlineImage(admin.TabularInline):
    model = Image


class MovieAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

# Register your models here.

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)