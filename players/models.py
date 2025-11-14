from django.db import models

class Team(models.Model):
    team_id = models.IntegerField(unique=True)
    team_name = models.CharField(max_length=300)
    wins = models.IntegerField()
    losses = models.IntegerField()
    team_abr = models.CharField(max_length=5, unique=True, null=False)
    
    @property
    def bbref_url(self):
        return f'/teams/{self.team_abr}/2026.html'



class Player(models.Model):
    name = models.CharField(max_length=300)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    games = models.IntegerField()
    minutes = models.FloatField()
    points = models.IntegerField()
    fgm = models.IntegerField()
    fga = models.IntegerField()
    ast = models.IntegerField()
    reb = models.IntegerField()
    fta = models.IntegerField()
    ftm = models.IntegerField()
    fg3m = models.IntegerField()
    fg3a = models.IntegerField()
    win_share = models.FloatField(null=True)
    ws_rank = models.IntegerField(null=True)
    losses_rank = models.IntegerField(null=True)
    ppg_rank = models.IntegerField(null=True)
    ast_rank = models.IntegerField(null=True)
    trb_rank = models.IntegerField(null=True)
    bb_ref_link = models.CharField(max_length=150)

    
