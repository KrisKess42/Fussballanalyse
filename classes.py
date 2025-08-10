from dataclasses import dataclass

@dataclass
class Club:
    clubname: str
    colours: str
    founded: int
    eternal_rank: int

@dataclass
class Matches:
    match_index: int
    team_home: Club
    team_away: Club
    goals_home: int = 0
    goals_away: int = 0

@dataclass
class Tipper:
    tipper_index: int
    name: str
    email: str = ""
    points: int = 0

@dataclass
class Tipp:
    tipper: Tipper
    match: Matches
    tipp_goals_home: int
    tipp_goals_away: int
    points_earned: int = 0
