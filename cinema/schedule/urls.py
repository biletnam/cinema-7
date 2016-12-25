from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d+)-(\d+)/$', views.show_schedule),
    url(r'^$', views.show_schedule)
]