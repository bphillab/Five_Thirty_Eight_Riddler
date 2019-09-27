"""
Riddler Nation’s Jibriel Taha, an avid baseball fan, saw the following tweet from the Milwaukee Brewers’ beat writer
Adam McCalvy:


Inspired by the Brewers’ apparent mediocrity (they’ve since gone on a roll to clinch a playoff spot) Jibriel asks the
following:

If a baseball team is truly .500, meaning it has a 50 percent chance of winning each game, what’s the probability that
it has won two of its last four games and four of its last eight games?

Answer: The probability that you will have w wins and l losses is: Binomial(w+l,w)/2^{w+l}
        Probability of 2 of last 4 and 4 of last 8 is basically two sets of 4 winning 2 of each.
"""

import numpy as np
from scipy.special import binom


def sim_game():
    games = np.random.binomial(1, 0.5, 8)
    return np.sum(games) == 4 and np.sum(games[-4:]) == 2


def simulate(n):
    """
    simulate: Simulates a number of sets of 8 games to see if 2 of the last 4 and 4 of the last 8 games were won
    :param n: number of simulations
    :return: probability of 4 of last 8 and 2 of last 4 won.
    """
    return np.mean([sim_game() for i in range(n)])


if __name__ == "__main__":
    print("Exact Answer: ", (binom(2 * 2, 2) / 4 ** 2) ** 2)
    print("Simulated answer: ", simulate(10000))
