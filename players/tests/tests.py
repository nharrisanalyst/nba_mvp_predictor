from django.test import TestCase
from players.models import Player, Team 

class PlayerTest(TestCase):
    def setUp(self):
        team_1 = Team(
            team_id = '00106',
            team_name = 'Rockets',
            wins = 52,
            losses = 20,
            team_abr='HOU'
        )
        
        team_1.save()
        
        player_1 = Player(
            name='Nathan Harris',
            team= team_1,
            games = 43,
            minutes=32,
            fgm = 27.6,
            fga = 45.2,
            points = 27.03,
            reb = 3,
            ast = 4,
            fg3m= 9,
            fg3a= 23,
            fta =5,
            ftm= 4,
        )
        player_1.save()
    
    def test_create_player_with_data(self):
        self.assertEqual(Player.objects.count(), 1)
    
    def test_that_player_has_a_team(self):
        player = Player.objects.get(name='Nathan Harris')
        
        self.assertEqual(player.team.team_name, 'Rockets')
        
    def test_create_player_add_in_null(self):
        team_2 = Team(team_id = '00103', team_name='Jazz', wins=23, losses=59, team_abr='HGO')
        team_2.save()
        player_2 =Player(
            name='Jeramiah',
            team= team_2,
            games = 43,
            minutes=32,
            fgm = 27.6,
            fga = 45.2,
            points = 27.03,
            reb = 3,
            ast = 4,
            fg3m= 9,
            fg3a= 23,
            fta =5,
            ftm= 4,
        )
        player_2.save()
        self.assertEqual(Player.objects.count(), 2)
        
        ##win share rank
        player_2.win_share = 3
        player_2.save()
        player_2.refresh_from_db()
        self.assertGreater(len(Player.objects.filter(win_share=3)), 0)
        
        ##win share rank
        player_2.ws_rank= 3
        player_2.save()
        player_2.refresh_from_db()
        self.assertGreater(len(Player.objects.filter(ws_rank=3)), 0)
        ## Losses rank  
        ## we are rnking losses becuase wins are not until the end of the season 
        ##but every loss means you are limited on you end of season win coutn
        
        player_2.losses_rank= 3
        player_2.save()
        player_2.refresh_from_db()
        self.assertGreater(len(Player.objects.filter(losses_rank=3)), 0)
        
        player_2.ppg_rank= 3
        player_2.save()
        player_2.refresh_from_db()
        self.assertGreater(len(Player.objects.filter(ppg_rank=3)), 0)
        
        player_2.ast_rank= 3
        player_2.save()
        player_2.refresh_from_db()
        self.assertGreater(len(Player.objects.filter(ast_rank=3)), 0)
        
        player_2.trb_rank= 3
        player_2.save()
        player_2.refresh_from_db()
        self.assertGreater(len(Player.objects.filter(trb_rank=3)), 0)
        
        player_2.bb_ref_link = '/players/g/gilgesh01.html'
        player_2.save()
        player_2.refresh_from_db()
        self.assertGreater(len(Player.objects.filter(bb_ref_link='/players/g/gilgesh01.html')), 0)
    
    


class TestTeam(TestCase): 
    
    def test_team_as_been_created(self):
        Team.objects.create(
            team_id = '00101',
            team_name='rockets',
            wins=50,
            losses=22,
            team_abr='HOU'
        )
        self.assertEqual(Team.objects.count(), 1)
        
    def test_bbref_url(self):
        Team.objects.create(
            team_id = '001010',
            team_name='Kings',
            wins=50,
            losses=22,
            team_abr='SAC'
        )
        
        sac = Team.objects.get(team_name='Kings')
        self.assertEqual(sac.bbref_url, '/teams/SAC/2026.html')
        