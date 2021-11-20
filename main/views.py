from django.shortcuts import render
from django.http import HttpResponse
from .models import FantasyTeam, ProjPoints

# Create your views here.

def index(response):
    team = FantasyTeam.objects.get(id=1)
    htmlDict = {"fantName": team}
    return render(response, "main/base.html", htmlDict )

def home(response):
    htmlDict = {"fantName":"testname"}
    return render(response, "main/home.html", htmlDict)