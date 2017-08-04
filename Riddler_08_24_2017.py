from numpy.random import uniform
from math import floor
import pandas as pd

number_of_games = 10000
number_of_players = 31


def convert_random_flip_into_pass(flip):
    """Convert a coin flip into a pass direction"""
    return 2 * (flip - 1 / 2)


def pass_potato(num_players, current_player):
    """Simulate a round ie passing the potato"""
    flip_coin = floor(uniform() * 2)
    return (current_player + convert_random_flip_into_pass(flip_coin)) % num_players


def one_game(num_players):
    """Simulate a game for a given number of players"""
    active_players = list(range(1, num_players))
    current_player = 0
    while len(active_players) != 1:
        current_player = pass_potato(current_player=current_player, num_players=num_players)
        active_players = list(filter(lambda x: x != current_player, active_players))
    return active_players[0]


def multiple_games(num_games, num_players):
    """Simulate multiple games with a set number of players"""
    tracker = []
    for i in range(num_games):
        tracker = tracker + [one_game(num_players)]
    return tracker


print(pd.DataFrame(multiple_games(number_of_games, number_of_players)).groupby(0).size() / number_of_games)
