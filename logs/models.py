from django.db import models

# Create your models here.


class Player(models.Model):
    discordName = models.CharField(max_length=32)
    leagueName  = models.CharField(max_length=16)

    registeredKills  = models.IntegerField()
    registeredAssits = models.IntegerField()
    registeredDamage = models.IntegerField()

class Game(models.Model):
    gameMode    = models.CharField(max_length=32)
    result      = models.BooleanField()
    timeElapsed = models.IntegerField()
    date        = models.DateField()