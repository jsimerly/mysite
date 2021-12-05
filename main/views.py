from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect
from .models import FantasyTeam, Matchup
from . forms import PlaceBet
from dataUpdater.regularUpdates import UsersRosters
from dataUpdater.betting import CreateLines
from datetime import date, datetime, timedelta


# Create your views here.
createLines = CreateLines()
commonUpdates = UsersRosters()
serverStart = datetime.now()
lastUpdate = serverStart

def index(response):
    team = FantasyTeam.objects.get(id=1)
    htmlDict = {"teamName": team}
    return render(response, "main/base.html", htmlDict )



def home(response):
    now = datetime.now()
    global lastUpdate
        
    updateDelta =  now - lastUpdate
    if updateDelta > timedelta(minutes=10):

        commonUpdates.updateRoster()
        commonUpdates.updateAllProject()
        
        createLines.createLineUp()
        createLines.createSpread()
        createLines.createOU()
        createLines.createML()
        

        lastUpdate = datetime.now()

    mathcups = Matchup.objects.all()
    htmlDict = {"fantName":"testname",
                'matchups': mathcups,
                'lastUpdate': lastUpdate.time()}
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