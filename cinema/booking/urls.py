from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d+)/select/$', views.show),
    # url(r'^(\d+)/$', views.show),
]