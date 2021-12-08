from django.utils import timezone
from re import match
from typing import Match
from django.db import models
from django.db.models.fields import NullBooleanField
from .static import Static
from main.models import FantasyTeam, Matchup, ServerInfo
from django.db.models import Q
import numpy as np

class CreateLines():
    allTeams = FantasyTeam.objects.all()
    noFA = allTeams.exclude(sleeperName='FreeAgent')
    serverInfo = ServerInfo.objects.get(id=1)
    static = Static()

    def updateAllLines(self):
        self._createSpread()
        self._createOU()
        self._createML()


    def _createSpread(self):
        matchups = Matchup.objects.all()

        for matchup in matchups:
            spread1 = -(matchup.team1.currentProj - matchup.team2.currentProj)
            spread2 = -(matchup.team2.currentProj - matchup.team1.currentProj)

            matchup.spreadT1 = spread1
            matchup.spreadT2 = spread2

            matchup.save()

    def _createOU(self):
        matchups = Matchup.objects.all()

        for matchup in matchups:
            ou = abs(matchup.team1.currentProj + matchup.team2.currentProj)
            matchup.overUnder = ou

            matchup.save()

    def _createML(self):
        matchups = Matchup.objects.all()
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
            allPlayer = team.player_set.all()
            qb = allPlayer.filter(pos='QB')
            rb = allPlayer.filter(Q(pos='RB') | Q(pos='FB'))
            wr = allPlayer.filter(pos='WR')
            te = allPlayer.filter(pos='TE')
            k = allPlayer.filter(pos='K')
            dst = allPlayer.filter(pos='DEF')

           
            qb1 = qb.order_by('-currentProj')[0]
            qb = qb.exclude(id=qb1.id)
            qb1.starter = True
            # qb1.save()

            rb1 = rb.order_by('-currentProj')[0]
            rb = rb.exclude(id=rb1.id)
            rb1.starter = True
            # rb1.save()
            rb2 = rb.order_by('-currentProj')[0]
            rb = rb.exclude(id=rb2.id)
            rb2.starter = True
            # rb2.save()

            wr1 = wr.order_by('-currentProj')[0]
            wr = wr.exclude(id=wr1.id)
            wr1.starter = True
            # wr1.save()
            wr2 = wr.order_by('-currentProj')[0]
            wr = wr.exclude(id=wr2.id)
            wr2.starter = True
            # wr2.save()

            te1 = te.order_by('-currentProj')[0]
            te = te.exclude(id=te1.id)
            te1.starter = True
            # te1.save()

            k1 = k.order_by('-currentProj')[0]
            k.starter = True
            # k1.save()
            
            dst1 = dst.order_by('-currentProj')[0]
            k.starter = True
            # dst1.save()
            
            flex = rb | wr | te
            flex1 = flex.order_by('-currentProj')[0]
            flex.exclude(id=flex1.id)
            # flex1.save()
            

            superFlex = flex | qb
            superFlex1 = superFlex.order_by('-currentProj')[0]
            # superFlex1.save()

            total = (qb1.currentProj + 
                        rb1.currentProj + 
                        rb2.currentProj + 
                        wr1.currentProj + 
                        wr2.currentProj + 
                        te1.currentProj + 
                        k1.currentProj + 
                        dst1.currentProj + 
                        flex1.currentProj + 
                        superFlex1.currentProj)
            
            team.currentProj = total
            team.save()
            print(team.funName + ": " + str(total))


            
        
            
    
