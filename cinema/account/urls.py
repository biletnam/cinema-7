from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.auth_user),
    url(r'^signup/$', views.create_user),
]