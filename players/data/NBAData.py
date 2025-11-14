
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
    

class NBADataCreate:
    def __init__(self, nba_data, team_data, player_data, TeamModel, PlayerModel):
       self.nba_data = nba_data
       self.team_data = team_data
       self.player_data = player_data
       self.TeamModel = TeamModel
       self.Playermodel = PlayerModel
    
    def _create_team_data(self):
        team_df = self.team_data.get_data_frames()[0]
        for row in team_df[['TeamID','TeamName', 'WINS','LOSSES']].itertuples():
            filter_teams = list(filter(lambda team: team['id'] == row.TeamID, self.nba_data.teams))
            self.TeamModel.objects.create(
                team_id = row.TeamID,
                team_name = row.TeamName,
                wins = row.WINS,
                losses = row.LOSSES,
                team_abr = filter_teams[0]['abbreviation']
            )
            
    def _create_player_data(self):
        player_df = self.player_data.get_data_frames()[0]
        for row in player_df[['TEAM_ID', 'PLAYER_NAME', 'GP', 'MIN', 'FGM', 'FGA', 'PTS', 'REB', 'AST', 'FG3M', 'FG3A', 'FTM','FTA']].itertuples():
            team = self.TeamModel.objects.get(team_id = row.TEAM_ID)
            self.Playermodel.objects.create(
                name = row.PLAYER_NAME,
                team = team,
                games = row.GP,
                minutes = row.MIN,
                points = row.PTS,
                fgm = row.FGM,
                fga = row.FGA,
                ast = row.AST,
                reb = row.REB,
                fta = row.FTA,
                ftm = row.FTM,
                fg3m =row.FG3M,
                fg3a =row.FG3A,
            )
   
    def create_data(self):
        self._create_team_data()
        self._create_player_data()