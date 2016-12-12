from django.shortcuts import render
from ..catalog.models import Movie, Genre

def info(request, m_id):
    try:
        cur_movie = Movie.objects.get(id=m_id)
    except Movie.DoesNotExist:
        return render(request, 'cinema/movie_info/templates/movie_info/movie404.html', status=404)
    else:
        cur_movie.trailer_url = cur_movie.trailer_url.split("=", 1)[1]
        context = {'cur_movie': cur_movie}
        return render(request, 'movie_info/movie_info.html', context)
