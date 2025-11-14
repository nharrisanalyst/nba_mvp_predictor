from django.test import TestCase
from players.data.NBAData import NBAData, NBADataCreate

from nba_api.stats.static import teams, players 
from nba_api.stats.endpoints import leaguedashplayerstats, leaguestandingsv3

from players.models import Team, Player

from unittest.mock import MagicMock


class NBADataTest(TestCase):
    
    def test_nbadata_initializes_with_proper_api(self):
        teams = MagicMock()
        players = MagicMock()
        nba_data = NBAData(teams_endpoint=teams, players_endpoint=players)
        ## Nba data asserts all teams and all players
        teams.assert_called_once()
        players.assert_called_once()
        
        
class NBADataCreateTest(TestCase):
    def setUp(self):
        self.nba_data = NBAData(teams_endpoint= teams.get_teams,   players_endpoint=players.get_active_players)
        
    def test_nba_data_create(self):
        nba_data_create = NBADataCreate(nba_data= self.nba_data, 
                                        team_data = leaguestandingsv3.LeagueStandingsV3(
                                                    league_id = "00",
                                                    season = "2025-26",
                                                    season_type= "Regular Season",
                                                ),
                                        player_data = leaguedashplayerstats.LeagueDashPlayerStats(
                                        season = "2025-26",
                                        season_type_all_star = "Regular Season",
                                         measure_type_detailed_defense= 'Base'
                                        ),
                                        TeamModel= Team,
                                        PlayerModel = Player,
                                    )
        
        nba_data_create.create_data()
        all_teams = Team.objects.all()
        ## test we have thirty teams
        self.assertEqual(len(all_teams), 30)
        
        ## test we have a team named the Thunder
        thunder = Team.objects.get(team_name='Thunder')
        self.assertEqual(thunder.team_name, 'Thunder')
        self.assertEqual(thunder.team_abr, 'OKC')
        
        ## test the player data was made 
        all_players = Player.objects.all()
        ## test we have players 
        self.assertGreater(len(all_players), 300)
        
        ## test we have a player with a name 
        aaron_gordon = Player.objects.get(name="Aaron Gordon")
        self.assertEqual(aaron_gordon.name, 'Aaron Gordon')
        sga = Player.objects.get(name="Shai Gilgeous-Alexander")
        self.assertEqual(sga.name, 'Shai Gilgeous-Alexander')
        
        