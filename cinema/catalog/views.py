from django.shortcuts import render
from .models import Movie, Genre
from django.http import Http404

def index(request):
    try:
        movie_list = Movie.objects.order_by('-release_date')
    except:
        raise Http404
    else:
        context = {'movie_list': movie_list}
        return render(request, 'catalog/index.html', context)
