INSERT INTO leagues (name) VALUES ('American'),('National');
INSERT INTO teams (name, league_id) VALUES ('data_science', 1), ('web_dev',1), ('analyst', 2), ('developer',2);

INSERT INTO players (name, team_id) VALUES ('jennifer', 1), ('chris',2), ('jeff',3), ('forest',4);

INSERT INTO games (date, location) VALUES ( '2018-06-25', 'NYC'), ('2018-05-05', 'MIA'), ('2018-01-15','MTL');

INSERT INTO team_games(team_id, game_id, score) VALUES (1, 1,10), (2,1,5), (3,2,1), (4,2,4), (1,3,5), (4,3,4);
