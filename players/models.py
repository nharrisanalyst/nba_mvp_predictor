from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=300)
    wins = models.IntegerField()
    losses = models.IntegerField()



class Player(models.Model):
    name = models.CharField(max_length=300)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    games = models.IntegerField()
    mpg = models.FloatField()
    win_share = models.FloatField()
    ppg = models.FloatField()
    ws_48 = models.FloatField()
    fg = models.FloatField()
    fga = models.FloatField()
    efg = models.FloatField()
    ast = models.FloatField()
    rbd = models.FloatField()
    fta = models.FloatField()
    ft = models.FloatField()
    ws_rank = models.IntegerField(null=True)
    losses_rank = models.IntegerField(null=True)
    ppg_rank = models.IntegerField(null=True)
    ast_rank = models.IntegerField(null=True)
    trb_rank = models.IntegerField(null=True)

    
