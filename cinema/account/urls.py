from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d+)/login', views.auth_user()),
]