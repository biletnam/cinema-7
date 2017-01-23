from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d+)/select/$', views.show),
    url(r'^(?P<id>[0-9]+)/$', views.booking_info, name='detail'),
]