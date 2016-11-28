from django.http import HttpResponse
from ..catalog.models import Movie
from django.shortcuts import render

def info(request, m_id):
    try:
        cur_movie = Movie.objects.get(id = m_id)
    except Movie.DoesNotExist:
        return render(request, 'movie404.html', status=404)
    else:
        ret_string = 'Movie info page for movie ' + cur_movie.title
        return HttpResponse(ret_string)