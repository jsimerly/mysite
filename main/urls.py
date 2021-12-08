from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("players/", views.players, name="players"),
    path("create/", views.create, name="create"),
    path('register/', views.registerPage, name='registerPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),
    path('teams/', views.teams, name='teams')
]