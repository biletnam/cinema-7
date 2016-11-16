from django.http import HttpResponse
from ..catalog.models import Movie

def info(request, m_id):
    cur_movie = Movie.objects.get(id = m_id)
    ret_string = 'Movie info page for movie ' + cur_movie.title
    return HttpResponse(ret_string)