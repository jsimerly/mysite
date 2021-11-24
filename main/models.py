from datetime import datetime
from io import open_code
from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

class FantasyTeam(models.Model):
    sleeperId = models.CharField(max_length=12, null=True)
    sleeperName = models.CharField(max_length=50)
    funName = models.CharField(max_length=50)
    currentProj = models.FloatField(default=0)
    matchup = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    tie = models.IntegerField(default=0)
    spreadWin = models.IntegerField(default=0)
    spreadLoss =models.IntegerField(default=0)
    
            

class Player(models.Model):
    currentTeam = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sleeperId = models.IntegerField(null=True)

    qb = models.BooleanField(default=False)
    rb = models.BooleanField(default=False)
    wr = models.BooleanField(default=False)
    te = models.BooleanField(default=False)
    k = models.BooleanField(default=False)
    dst = models.BooleanField(default=False)

    currentProj = models.FloatField(default=0)

    def __str__(self):
        return self.name

class PlayerHistory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    season = models.IntegerField
    week = models.IntegerField
    nflTeam = models.CharField(max_length=4)

class TeamHistory(models.Model):
    team = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT)
    #opponent = models.ManyToManyField(FantasyTeam, open_code=PROTECT)
    season = models.IntegerField
    week = models.IntegerField
    score = models.FloatField
    ml = models.FloatField
    ou = models.FloatField
    
    