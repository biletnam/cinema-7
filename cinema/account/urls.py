from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login_view),
    url(r'^signup/$', views.signup_view),
    url(r'^login/attempt$', views.auth_user),
    url(r'^signup/attempt$', views.create_user),
    url(r'^(?P<id>[0-9]+)/', views.account_info),
]