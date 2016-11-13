from django.contrib import admin

from .models import Movies
from .models import MovieGenre
from .models import Genres

# Register your models here.

admin.site.register(Movies)
admin.site.register(MovieGenre)
admin.site.register(Genres)