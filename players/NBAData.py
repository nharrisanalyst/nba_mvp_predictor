
class NBAData:
    def __init__(self, players_endpoint, teams_endpoint):
        self.players_endpoint = players_endpoint
        self.teams_endpoint =teams_endpoint
        
        self.players = self._set_players()
        self.teams = self._set_teams()
    
    def _set_players(self):
        return self.players_endpoint()
    
    def _set_teams(self):
        return self.teams_endpoint()