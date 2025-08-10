from classes import Club, Matches

# Globale Listen für Daten
teams = []
season_matches = []

# Vereine hinzufügen
teams.append(Club(clubname = "FCB",  colours = "Red/White",          founded = 1900, eternal_rank = 1 ))
teams.append(Club(clubname = "S04",  colours = "Blue/White",         founded = 1904, eternal_rank = 2 ))
teams.append(Club(clubname = "BVB",  colours = "Black/Yellow",       founded = 1909, eternal_rank = 3 ))
teams.append(Club(clubname = "HSV",  colours = "Blue/White/ Black",  founded = 1887, eternal_rank = 4 ))
teams.append(Club(clubname = "RBL",  colours = "Red/White",          founded = 2006, eternal_rank = 81 ))
teams.append(Club(clubname = "VfB",  colours = "Red/White",          founded = 1892, eternal_rank = 8 ))
teams.append(Club(clubname = "SVW",  colours = "Green/White",        founded = 1900, eternal_rank = 18 ))
teams.append(Club(clubname = "FCU",  colours = "Red/White",          founded = 1966, eternal_rank = 25 ))
teams.append(Club(clubname = "B04",  colours = "Red/Black",          founded = 1904, eternal_rank = 17 ))
teams.append(Club(clubname = "SGE",  colours = "Black/White",        founded = 1900, eternal_rank = 9 ))

# Spiele hinzufügen
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[0], team_away = teams[9]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[1], team_away = teams[8]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[2], team_away = teams[7]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[3], team_away = teams[6]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[4], team_away = teams[5]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[9], team_away = teams[1]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[8], team_away = teams[2]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[7], team_away = teams[3]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[6], team_away = teams[4]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[5], team_away = teams[0]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[0], team_away = teams[8]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[1], team_away = teams[7]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[2], team_away = teams[6]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[3], team_away = teams[5]))
season_matches.append(Matches(match_index = len(season_matches) + 1,team_home = teams[4], team_away = teams[9]))
