from django.test import TestCase
from players.NBAData import NBAData

from unittest.mock import MagicMock


class NBADataTest(TestCase):
    
    def test_nbadata_initializes_with_proper_api(self):
        teams = MagicMock()
        players = MagicMock()
        nba_data = NBAData(teams_endpoint=teams, players_endpoint=players)
        ## Nba data asserts all teams and all players
        teams.assert_called_once()
        players.assert_called_once()
        