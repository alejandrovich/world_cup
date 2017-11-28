from collections import namedtuple


Team = namedtuple('Team', ('name', 'rank'))
Conference = namedtuple('Conference', ('name', 'max_teams', 'teams'))
Pot = namedtuple('Pot', ('name', 'teams',))
Group = namedtuple('Group', ('name', 'teams', 'strength'))
Draw = namedtuple('Draw', ('groups',))
