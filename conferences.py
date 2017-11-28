import teams
from models import Conference


Asia = Conference(name='Asia', max_teams=1, teams=(
    teams.Australia,
    teams.Japan,
    teams.SouthKorea,
    teams.SaudiArabia,
    teams.Iran,
))
Africa = Conference(name='Africa', max_teams=1, teams=(
    teams.Tunisia,
    teams.Egypt,
    teams.Senegal,
    teams.Nigeria,
    teams.Morocco,
))
SouthAmerica = Conference(name='South America', max_teams=1, teams=(
    teams.Brazil,
    teams.Argentina,
    teams.Uruguay,
    teams.Peru,
    teams.Colombia,
))
Europe = Conference(name='Europe', max_teams=2, teams=(
    teams.Russia,
    teams.Germany,
    teams.Portugal,
    teams.Belgium,
    teams.Poland,
    teams.France,
    teams.Spain,
    teams.Switzerland,
    teams.England,
    teams.Croatia,
    teams.Denmark,
    teams.Iceland,
    teams.Sweden,
    teams.Serbia,
))
NorthAmerica = Conference(name='North America', max_teams=1, teams=(
    teams.Mexico,
    teams.Panama,
    teams.CostaRica,
))

CONFERENCES = (
    Asia,
    Africa,
    SouthAmerica,
    Europe,
    NorthAmerica,
)


def check_conference(group_teams):
    conference_count = {
        conference: len(
            tuple(
                team for team in group_teams
                if team in conference.teams
            )
        )
        for conference in CONFERENCES
    }

    return all(
        conference.max_teams >= num_teams
        for conference, num_teams in conference_count.iteritems()
    )
