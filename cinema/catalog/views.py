from django.shortcuts import render
from .models import Movie, Genre
from django.http import Http404

# Create your views here.

def index(request):
    try:
        movie_list = Movie.objects.order_by('-release_date')
        context = {'movie_list': movie_list}
    except:
        raise Http404
    else:
        return render(request, 'catalog/index.html', context)