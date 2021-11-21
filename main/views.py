from django.shortcuts import render
from django.http import HttpResponse, response
from .models import FantasyTeam, ProjPoints
from . forms import PlaceBet

# Create your views here.

def index(response):
    team = FantasyTeam.objects.get(id=1)
    htmlDict = {"teamName": team}
    return render(response, "main/base.html", htmlDict )

def home(response):
    htmlDict = {"fantName":"testname"}
    return render(response, "main/home.html", htmlDict)

def players(response):
    team = FantasyTeam.objects.get(id=1)
    htmlDict = {"teamName": team}
    return render(response, "main/players.html",htmlDict)

def create(response):
    if response.method == "POST":
        form = PlaceBet(response.POST)

    else:
        form = PlaceBet
    
    return render(response, "main/create.html", {"form": form})