from datetime import datetime
from io import open_code
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT

# Create your models here.

class FantasyTeam(models.Model):
    sleeperId = models.CharField(max_length=12, null=True)
    sleeperName = models.CharField(max_length=50)
    rosterId = models.IntegerField(null=True)
    funName = models.CharField(max_length=50)
    currentProj = models.FloatField(default=0)
    matchup = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    tie = models.IntegerField(default=0)
    spreadWin = models.IntegerField(default=0)
    spreadLoss =models.IntegerField(default=0)

   
class Player(models.Model):
    currentTeam = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE, default=11)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    sleeperId = models.CharField(max_length = 6,null=True)
    pos = models.CharField(max_length=4, null=True)
    nflTeam = models.CharField(max_length=4, null=True)

    currentProj = models.FloatField(default=0)

class PlayerHistory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    season = models.IntegerField(null=True)
    week = models.IntegerField(null=True)
    nflTeam = models.CharField(max_length=4)

class TeamHistory(models.Model):
    team = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='mainTeam')
    opponent = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='opponent', default=11)
    season = models.IntegerField(null=True)
    proj = models.FloatField(null=True)
    week = models.IntegerField(null=True)
    score = models.FloatField(null=True)
    ml = models.FloatField(null=True)
    ou = models.FloatField(null=True)

class Matchup(models.Model):
    matchupId = models.IntegerField(default=0)
    team1 = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='team1')
    team2 = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='team2')
    overUnder = models.FloatField(null=True)
    spreadT1 = models.FloatField(null=True)
    spreadT2 = models.FloatField(null=True)
    team1Ml = models.FloatField(null=True)
    team2Ml = models.FloatField(null=True)

    def getMoneyLineT1(self):
        if self.team1Ml > 0:
            return '+' + str(round(self.team1Ml))
        else:
            
            return str(round(self.team1Ml))
            

    def getMoneyLineT2(self):
        if self.team2Ml > 0:
            return '+' + str(round(self.team2Ml))
        else:
            return str(round(self.team2Ml))

    def getOverUnder(self):
        return round(self.overUnder)

    def getSpreadT1(self):
        if self.spreadT1 > 0 :
            return '+' + str(round(self.spreadT1))
        else:
            return round(self.spreadT1)
            

    def getSpreadT2(self):
        if self.spreadT1 < 0:
            return '+' + str(round(self.spreadT2))
        else:
            return round(self.spreadT2)

    

    
    