"""From Josh Streeter, a participatory tie-breaker:

Suppose every Riddler reader, you included, is a coach of a soccer team in the Riddler Official Football League, or
ROFL. They are instructing their players on strategies for taking penalty kicks to decide a soccer game that has been
tied through regulation and extra time.

The goal is divided into two rows (upper and lower) and three columns (left, center and right). The player taking the
penalty selects one of these six areas at which to aim their shot, and the goalie chooses one of the six to defend. If
the goalie guesses the same area as the shot, she automatically saves the ball. But even if the goalie does not guess
right, aiming at the outer regions of the goal carries some risk of the shot missing the goal altogether. For example,
an undefended shot to the upper left corner will score 70 percent of the time. (See the illustration below.)

Every reader — er, coach — should submit two inputs: the area they want their shooter to target and the area they
want their goalkeeper to defend. Like with the Battle for Riddler Nation, each participant’s inputs for shooting and
for defending will be simulated against each another’s, and whoever accumulates the most net goals will be crowned
ROFL Coach of the Year.
"""

import random
import numpy as np


class tmptype(object):
    pass


def score(kick):
    if kick == 0:
        return .7
    if kick == 1:
        return .9
    if kick == 2:
        return .8
    if kick == 3:
        return .8
    if kick == 4:
        return 1
    if kick == 5:
        return .9


def battle(p1, p2):
    p1_score = 0
    p2_score = 0
    if p1.kick != p2.block:
        p1_score = score(p1.kick)
    if p2.kick != p1.block:
        p2_score = score(p2.kick)
    return p1_score, p2_score


def update_players(players, num_players_chosen):
    for i in range(len(players)):
        players[i].score = 0
    for i in range(len(players)):
        for j in range(len(players)):
            res1,res2 = battle(players[i], players[j])
            players[i].score = players[i].score + res1
            players[j].score = players[j].score + res2
    total_points = sum([i.score for i in players])
    p_chosen = [i.score/total_points for i in players]
    chosen_players = np.random.choice(players, num_players_chosen, replace=False, p = p_chosen)
    return chosen_players


def mate_chosen_players(chosen_players, num_players):
    players = []
    for i in range(num_players):
        p1 = random.choice(chosen_players)
        p2 = random.choice(chosen_players)
        p = tmptype()
        p.kick = random.choice([p1.kick, p2.kick])
        p.block = random.choice([p1.block, p2.block])
        p.score = 0
        players = players + [p]
    return players


def mutate_players(players, num_to_mutate):
    which_mutated = random.sample(range(len(players)), num_to_mutate)
    for i in which_mutated:
        players[i].kick = random.choice(range(6))
        players[i].block = random.choice(range(6))
    return players


def main():
    num_players = 100
    num_to_mutate = 5
    num_players_chosen = 30
    num_iters = 1000
    start_players = []
    for i in range(num_players):
        p = tmptype()
        p.kick = random.choice(range(6))
        p.block = random.choice(range(6))
        p.score = 0
        start_players = start_players + [p]
    for i in range(num_iters):
        start_players = mutate_players(
            mate_chosen_players(
                update_players(start_players, num_players_chosen),
                num_players),
            num_to_mutate)
    end_state = [(i.kick,i.block) for i in start_players]
    for i in range(6):
        for j in range(6):
            print("(", i, ",", j, ˚",): ", end_state.count((i, j)))


if __name__ == "__main__":
    main()

