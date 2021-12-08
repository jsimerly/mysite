from datetime import datetime
from io import open_code
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User

# Create your models here.

class FantasyTeam(models.Model):
    user = models.ForeignKey(User, verbose_name='User', related_name='fantasyTeam',
                            on_delete=models.PROTECT, null=True)
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

    def getStarters(self):
        allPlayer = self.player_set.all()
        qb = allPlayer.filter(pos='QB')
        rb = allPlayer.filter(models.Q(pos='RB') | models.Q(pos='FB'))
        wr = allPlayer.filter(pos='WR')
        te = allPlayer.filter(pos='TE')
        k = allPlayer.filter(pos='K')
        dst = allPlayer.filter(pos='DEF')

        qb1 = qb.order_by('-currentProj')[0]
        qb = qb.exclude(id=qb1.id)

        rb1 = rb.order_by('-currentProj')[0]
        rb = rb.exclude(id=rb1.id)

        rb2 = rb.order_by('-currentProj')[0]
        rb = rb.exclude(id=rb2.id)

        wr1 = wr.order_by('-currentProj')[0]
        wr = wr.exclude(id=wr1.id)

        wr2 = wr.order_by('-currentProj')[0]
        wr = wr.exclude(id=wr2.id)

        te1 = te.order_by('-currentProj')[0]
        te = te.exclude(id=te1.id)

        k1 = k.order_by('-currentProj')[0]
        k = k.exclude(id=k1.id)
        
        dst1 = dst.order_by('-currentProj')[0]
        dst = dst.exclude(id=dst1.id)
        
        flex = rb | wr | te
        flex1 = flex.order_by('-currentProj')[0]
        flex = flex.exclude(id=flex1.id)
        
        superFlex = flex | qb
        superFlex1 = superFlex.order_by('-currentProj')[0]
        superFlex.exclude(id=superFlex1.id)

        starters = [qb1, rb1, rb2, wr1, wr2, te1,  flex1, superFlex1, k1, dst1]
        bench = qb | rb | wr | te | k | dst

        return (starters,bench)

    def getBestFreeAgent(self,pos):
        freeAgentTeam = self.objects.filter(sleeperName='FreeAgent')
        freeAgents = freeAgentTeam.player.filter(pos=pos)
        best = freeAgents.order_by('-currentProj')[0]
        return best.currentProj

class ServerInfo(models.Model):
    lastLineUpdate = models.DateTimeField(null=True)
    lastProjUpdate = models.DateTimeField(null=True)
    lastMatchupUpdate = models.DateTimeField(null=True)
    

class Proxy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sleeperId = models.IntegerField(default=0)
    weeklyBalance = models.FloatField(default=0)
    balance = models.FloatField(default=0)

class Bets(models.Model):
    user = models.ForeignKey(User, verbose_name='User', related_name='bets',
                                    on_delete=models.PROTECT, null=True)
    wager = models.FloatField(default=0)
    wagerType = models.CharField(null=True, max_length=10)
   
class Player(models.Model):
    currentTeam = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE, default=11)
    starter = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    sleeperId = models.CharField(max_length = 6,null=True)
    pos = models.CharField(max_length=4, null=True)
    nflTeam = models.CharField(max_length=4, null=True)

    currentProj = models.FloatField(default=0)

    def getProj(self):
        return str(round(self.currentProj, 2))

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

    

    
    