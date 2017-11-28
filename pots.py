import teams
from models import Pot


Pot2 = Pot(
    name='Pot 2',
    teams=(
        teams.Spain,
        teams.Peru,
        teams.Switzerland,
        teams.England,
        teams.Colombia,
        teams.Mexico,
        teams.Uruguay,
        teams.Croatia,
    )
)
Pot3 = Pot(
    name='Pot 3',
    teams=(
        teams.Denmark,
        teams.CostaRica,
        teams.Iceland,
        teams.Sweden,
        teams.Tunisia,
        teams.Egypt,
        teams.Senegal,
        teams.Iran,
    )
)
Pot4 = Pot(
    name='Pot 4',
    teams=(
        teams.Serbia,
        teams.Nigeria,
        teams.Australia,
        teams.Japan,
        teams.Morocco,
        teams.Panama,
        teams.SouthKorea,
        teams.SaudiArabia,
    )
)
