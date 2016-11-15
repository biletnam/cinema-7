from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^(?P<movie_id>[0-9]+)/$', views.info, name='movie info by id'),
    url(r'^(?P<m_id>[0-9]+)/$', views.info, name='detail'),
]