from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect
from .models import FantasyTeam, Matchup
from . forms import PlaceBet

# Create your views here.

def index(response):
    team = FantasyTeam.objects.get(id=1)
    htmlDict = {"teamName": team}
    return render(response, "main/base.html", htmlDict )

def home(response):
    mathcups = Matchup.objects.all()
    htmlDict = {"fantName":"testname",
                'matchups': mathcups}
    return render(response, "main/home.html", htmlDict)

def players(response):
    team = FantasyTeam.objects.get(id=1)
    htmlDict = {"teamName": team}
    return render(response, "main/players.html",htmlDict)

def create(response):
    team = FantasyTeam.objects.get(id=1)
    htmlDict = {"teamName": team}

    if response.method == "POST":
        form = PlaceBet(response.POST)

        if form.is_valid():
            return render(response, "main/players.html",htmlDict)
    else:
        form = PlaceBet

       
    
    return render(response, "main/create.html", {"form": form})