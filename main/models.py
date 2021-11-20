from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model

# Create your models here.
class FantasyTeam(models.Model):
    sleeperName = models.CharField(max_length=50)
    funName = models.CharField(max_length=50)

    def __str__(self):
        return self.sleeperName

class ProjPoints(models.Model):
    team = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE)
    projection = models.FloatField

    def __str__(self):
        return self.projection

