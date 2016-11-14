from django.shortcuts import render
from .models import Movie, Genre


# Create your views here.

def index(request):
    movie_list = Movie.objects.order_by('-release_date')
    context = {'movie_list': movie_list}
    return render(request, 'catalog/index.html', context)