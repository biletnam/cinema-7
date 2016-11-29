from django.shortcuts import render
from ..catalog.models import Movie, Genre

def info(request, m_id):
    cur_movie = Movie.objects.get(id = m_id)
    context = {'cur_movie': cur_movie}
    return render(request, 'movie_info/movie_info.html', context)