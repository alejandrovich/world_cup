import itertools
import logging

from conferences import check_conference
from groups import GROUP_LETTERS, GROUP_SEEDS
from models import Pot, Group
from pots import Pot2, Pot3, Pot4

logging.basicConfig(filename='logs/worldcup.log', level=logging.DEBUG)
_RESULT_COUNT = 0
   

def draw_groups():
    pots = (Pot2, Pot3, Pot4)
    select_group(0, pots, selected_groups=())


def select_group(group_index, pots, selected_groups):
    if group_index == len(GROUP_LETTERS):
        log_results(selected_groups)
        
        return

    letter = GROUP_LETTERS[group_index]
    group_seed = GROUP_SEEDS[letter]
    teams_by_pot = tuple(pot.teams for pot in pots)

    valid_selections = tuple(
        group_teams
        for group_teams in tuple(
            (group_seed,) + group_selection
            for group_selection in tuple(itertools.product(*teams_by_pot))
        )
        if check_conference(group_teams)
    )

    for possible_teams in valid_selections:
        group = Group(
            name=letter, 
            teams=possible_teams, 
            strength=sum(team.rank for team in possible_teams)
        )
        new_pots = tuple(
            Pot(
                name=pot.name,
                teams=tuple(set(pot.teams) - set(group.teams))
            )
            for pot in pots
        )
        select_group(group_index + 1, new_pots, selected_groups + (group,))
        
        
def result_statement(selected_groups):
    return '{}\n{}'.format(
        _RESULT_COUNT,
        '\n'.join(
            '{} str {}: {}'.format(
                group.name,
                group.strength,
                ', '.join(team.name for team in group.teams)
            )
            for group in selected_groups
        )
    )

    
def log_results(selected_groups):
    global _RESULT_COUNT
    _RESULT_COUNT += 1

    output = result_statement(selected_groups)

    logging.debug(output)


if __name__ == '__main__':
    draw_groups()
