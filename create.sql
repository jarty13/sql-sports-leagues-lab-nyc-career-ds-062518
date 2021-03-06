CREATE TABLE leagues(
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE teams(
  id INTEGER PRIMARY KEY,
  name TEXT,
  league_id INTEGER
);

CREATE TABLE players(
  id INTEGER PRIMARY KEY,
  name TEXT,
  team_id INTEGER
);

CREATE TABLE games(
  id INTEGER PRIMARY KEY,
  date DATE,
  location TEXT
);

CREATE TABLE team_games(
  id INTEGER PRIMARY KEY,
  team_id INTEGER,
  game_id INTEGER,
  score INTEGER
  );
