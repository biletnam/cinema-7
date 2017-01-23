from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d+)/select/$', views.show),
    url(r'^(?P<id>[0-9]+)/$', views.show_booking_info),
    url(r'^proceed', views.create_booking),
]