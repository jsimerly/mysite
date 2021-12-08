from django.shortcuts import render, redirect
from datetime import datetime, time, timedelta
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#my imports
from . forms import CreateUserForm, AuthenticationFormWithInActiveUsers
from dataUpdater.regularUpdates import UsersRosters
from dataUpdater.playerUpdates import AllPlayers
from dataUpdater.betting import CreateLines
from .models import FantasyTeam, Matchup, ServerInfo

# Create your views here.
createLines = CreateLines()
commonUpdates = UsersRosters()
weeklyUpdates = AllPlayers()
serverInfo = ServerInfo.objects.get(id=1)

def registerPage(response):
    if response.method == 'POST' :
        form = CreateUserForm(response.POST)
        
        
        if form.is_valid():
            form.save()         
            username = form.cleaned_data.get('username')
            messages.success(response, 'Account was created for ' + username)
            
            return redirect('loginPage')
        
    else:
        form = CreateUserForm()

    context = {'form':form,}
    return render(response, 'main/register.html', context)

def loginPage(response):
    form = AuthenticationFormWithInActiveUsers()

    if response.method == 'POST':
        form = AuthenticationFormWithInActiveUsers(response.POST)

        username = response.POST.get('username')
        password = response.POST.get('password')

        print(username)
        print(password)

        user = authenticate(response, username=username, password=password)

        if user is not None:
            print('user not none')
            login(response, user)
            return redirect('index')
        else:
            messages.info(response, 'Username or password is incorrect')
        
    context = {'form':form}
    return render(response, 'main/login.html', context)

def logoutUser(response):
    logout(response)
    return redirect('index')
    
def teams(response):
    noFa = FantasyTeam.objects.all().exclude(sleeperName='FreeAgent')
    context = {'teams': noFa}
    return render(response, "main/teams.html", context)
    
def index(response):
    now = timezone.now()
    lastLineUpdate = serverInfo.lastLineUpdate
    lastMatchupUpdate = serverInfo.lastMatchupUpdate
    lastProjUpdate = serverInfo.lastProjUpdate
        
    lineUpdateDelta =  now - lastLineUpdate
    matchupUpdateDelta = now - lastMatchupUpdate
    projUpdateDelta = now - lastProjUpdate
    
    if matchupUpdateDelta > timezone.timedelta(hours=3):
        print('---------------Updating Matchups--------------------')
        weeklyUpdates.updateMatchups()
        print('---------------Updating User Info-------------------')
        commonUpdates.updateUserInfo()
        serverInfo.lastMatchupUpdate = timezone.now()
    else:
        print('Time Until Next Matchup Update: ' + str(timezone.timedelta(hours=3) - matchupUpdateDelta))

    
    if projUpdateDelta > timezone.timedelta(minutes=20):
        print('---------------Updating Projections------------------')
        commonUpdates.updateAllProject()
        serverInfo.lastProjUpdate = timezone.now()
    else:
        print('Time Until Next Proj Update: ' + str(timezone.timedelta(minutes=20) - projUpdateDelta))
    
    if lineUpdateDelta > timezone.timedelta(minutes=10):
        print('---------------Updating Rosters----------------------')
        commonUpdates.updateRoster()
        print('---------------Updating Lines------------------------')
        createLines.createLineUp()
        createLines.updateAllLines()
        serverInfo.lastLineUpdate = timezone.now()
    else:
        print('Time Until Next Line Update: ' + str(timezone.timedelta(minutes=10) - lineUpdateDelta))
    
    serverInfo.save()


    mathcups = Matchup.objects.all()
    context = {"fantName":"testname",
                'matchups': mathcups,
                'lastUpdate': lastLineUpdate,}
    return render(response, "main/home.html", context)
        

def players(response):
    team = FantasyTeam.objects.get(id=1)
    context = {"teamName": team}
    return render(response, "main/players.html",context)

def create(response):
    team = FantasyTeam.objects.get(id=1)
    context = {"teamName": team}

    if response.method == "POST":
        form = PlaceBet(response.POST)

        if form.is_valid():
            return render(response, "main/players.html",context)
    else:
        form = PlaceBet

       
    
    return render(response, "main/create.html", {"form": form})