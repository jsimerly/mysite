from re import match
from typing import Match
from django.db import models
from django.db.models.fields import NullBooleanField
from .static import Static
from main.models import FantasyTeam, Matchup
import numpy as np

class CreateLines():
    allTeams = FantasyTeam.objects.all()
    noFA = allTeams.exclude(sleeperName='FreeAgent')
    static = Static()

    def createSpread(self):
        matchups = Matchup.objects.all()

        for matchup in matchups:
            spread1 = -(matchup.team1.currentProj - matchup.team2.currentProj)
            spread2 = -(matchup.team2.currentProj - matchup.team1.currentProj)

            matchup.spreadT1 = spread1
            matchup.spreadT2 = spread2

            matchup.save()

    def createOU(self):
        matchups = Matchup.objects.all()

        for matchup in matchups:
            ou = abs(matchup.team1.currentProj + matchup.team2.currentProj)
            matchup.overUnder = ou

            matchup.save()

    def createML(self):
        matchups = Matchup.objects.all()
        vig = self.static.vig

        for matchup in matchups:
            print('---------------------------------')
            spread = abs(matchup.spreadT1)
            percentSpread = (1/1.75)*np.log(spread*.0175+1)

            if percentSpread > .33:
                percentSpread = .33

            favOdds = .5+percentSpread
            undOdds = 1-favOdds
            favOdds += vig/2
            undOdds += vig/2

            print(favOdds)
            print(undOdds)

            posML = (-1*favOdds/(1-favOdds)*100)
            if undOdds < .5:
                negML = ((1-undOdds)/undOdds)*100
            else:
                negML = (-1*undOdds/(1-undOdds)*100)

            print(posML)
            print(negML)

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
            print(matchup.team1)
            print(matchup.team1Ml)
            print(matchup.team2)
            print(matchup.team2Ml)






    

    def createLineUp(self):
        teams = self.noFA

        for team in teams:
            qb = []
            rb = []
            wr = []
            te = []
            k = []
            dst = []

            for player in team.player_set.all():
                if player.pos == 'QB':
                    qb.append(player.currentProj)
                elif player.pos == 'RB':
                    rb.append(player.currentProj)
                elif player.pos == 'WR':
                    wr.append(player.currentProj)
                elif player.pos == 'TE':
                    te.append(player.currentProj)
                elif player.pos == 'K':
                    k.append(player.currentProj)
                elif player.pos == 'DEF':
                    dst.append(player.currentProj)
                else:
                    print('position not recognized')

            qb1 = max(qb)
            qb.remove(qb1)

            rb1 = max(rb)
            rb.remove(rb1)
            rb2 = max(rb)
            rb.remove(rb2)

            wr1 = max(wr)
            wr.remove(wr1)
            wr2 = max(wr)
            wr.remove(wr2)

            te1 = max(te)
            te.remove(te1)

            k1 = max(k)

            dst1 = max(dst)

            flex = rb + wr + te
            flex1 = max(flex)
            flex.remove(flex1)

            superFlex = flex + qb
            superFlex1 = max(superFlex)

            total = qb1 + rb1 + rb2 + wr1 + wr2 + te1 + k1 + dst1 + flex1 + superFlex1
            
            team.currentProj = total
            team.save()

