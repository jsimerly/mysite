from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("players/", views.players, name="players"),
    path("create/", views.create, name="create")
]