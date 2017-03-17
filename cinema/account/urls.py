from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.auth_user),
    url(r'^signup/$', views.create_user),
    url(r'^(?P<id>[0-9]+)/', views.account_info),
]