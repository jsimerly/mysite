from django.utils import timezone
from re import match
from typing import Match
from django.db import models
from django.db.models.fields import NullBooleanField
from .static import Static
from main.models import FantasyTeam, Matchup, Player
from django.db.models import Q
import numpy as np

class CreateLines():
    allTeams = FantasyTeam.objects.all()
    noFA = allTeams.exclude(sleeperName='FreeAgent')
    static = Static()

    def updateAllLines(self):
        self._createSpread()
        self._createOU()
        self._createML()


    def _createSpread(self):
        matchups = Matchup.objects.all().exclude(team1_id=None)

        for matchup in matchups:
            spread1 = -(matchup.team1.currentProj - matchup.team2.currentProj)
            spread2 = -(matchup.team2.currentProj - matchup.team1.currentProj)

            matchup.spreadT1 = spread1
            matchup.spreadT2 = spread2

            matchup.save()

    def _createOU(self):
        matchups = Matchup.objects.all().exclude(team1_id=None)

        for matchup in matchups:
            ou = abs(matchup.team1.currentProj + matchup.team2.currentProj)
            matchup.overUnder = ou

            matchup.save()

    def _createML(self):
        matchups = Matchup.objects.all().exclude(team1_id=None)
        vig = self.static.vig

        for matchup in matchups:
            spread = abs(matchup.spreadT1)
            percentSpread = (1/1.75)*np.log(spread*.0175+1)

            if percentSpread > .33:
                percentSpread = .33

            favOdds = .5+percentSpread
            undOdds = 1-favOdds
            favOdds += vig/2
            undOdds += vig/2

            
            posML = (-1*favOdds/(1-favOdds)*100)
            if undOdds < .5:
                negML = ((1-undOdds)/undOdds)*100
            else:
                negML = (-1*undOdds/(1-undOdds)*100)

            
            if matchup.team1.currentProj > matchup.team2.currentProj:
                matchup.team1Ml = posML
                matchup.team2Ml = negML
            elif matchup.team2.currentProj > matchup.team1.currentProj:
                matchup.team1Ml = negML
                matchup.team2Ml = posML
            else:
                matchup.team1Ml = -110
                matchup.team2Ml = -110

            matchup.save()
            
    def createLineUp(self):
        teams = self.noFA

        for team in teams:
            total = 0
            starters = team.getStarters()
            for player in starters[0]:
                if player.currentProj <= 0:
                    freeAgents = Player.objects.filter(Q(pos=player.pos) & Q(currentTeam_id=11))         
                    best = freeAgents.order_by('-currentProj')[0]
                    total += best.currentProj
                else:                    
                    total += player.currentProj

            team.currentProj = total
            team.save()
            print(team.funName + ": " + str(total))


            
        
            
    
