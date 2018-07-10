def select_name_of_player_with_shortest_name():
    return " SELECT name FROM players GROUP BY name ORDER BY LENGTH(name) LIMIT 1";

def select_all_new_york_players_names():
    return " SELECT players.name FROM players JOIN teams on teams.id= players.team_id WHERE teams.id = 1 or teams.id =3";

def select_team_name_and_total_goals_scored_for_new_york_rangers():
    return "SELECT teams.name, SUM(team_games.score)FROM teams JOIN team_games on team_games.team_id = teams.id WHERE teams.id= 1;"

def select_all_games_date_and_info_teams_name_and_score_for_teams_in_nhl():
    return "SELECT games.date, games.info, teams.name, team_games.score FROM games JOIN team_games on team_games.game_id = games.id JOIN teams on teams.id = team_games.team_id JOIN leagues on leagues.id = teams.league_id WHERE leagues.id =1";
    #JOIN leagues on leagues.id = teams.league_id GROUP BY leagues.id HAVING leagues.id = 1";

def select_date_info_and_total_points_for_highest_scoring_nba_game():
    return "SELECT games.date, games.info, SUM(team_games.score) FROM games JOIN team_games on team_games.game_id = games.id JOIN teams on team_games.team_id = teams.id GROUP BY team_games.game_id HAVING teams.league_id = 2 ORDER BY team_games.score DESC LIMIT 1 ";

#SELECT games.date, SUM(team_games.score) FROM games JOIN team_games on team_games.game_id = games.id JOIN teams on team_games.team_id = teams.id GROUP BY team_games.game_id HAVING teams.league_id = 2  ;
