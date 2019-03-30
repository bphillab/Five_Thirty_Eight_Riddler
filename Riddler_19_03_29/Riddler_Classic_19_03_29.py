"""
From Steven Pratt, ordinal bee probability:

You are competing in a spelling bee alongside nine other contestants.
You can each spell words perfectly from a certain portion of the
dictionary but will misspell any word not in that portion of the book.
Specifically, you have 99 percent of the dictionary down cold, and your
opponents have 98 percent, 97 percent, 96 percent, and so on down to
90 percent memorized. The bee’s rules are simple: The contestants take
turns spelling in some fixed order, which then restarts with the first
surviving speller at the end of a round. Miss a word and you’re out,
and the last speller standing wins. The bee words are chosen randomly
from the dictionary.

First, say the contestants go in decreasing order of their knowledge,
so that you go first. What are your chances of winning the spelling bee?
Second, say the contestants go in increasing order of knowledge, so that
you go last. What are your chances of winning now?
"""

from copy import deepcopy
import numpy as np


def simulate_bee(probas: list) -> float:
    contestants = deepcopy(probas)
    i = 0
    while len(contestants) > 1:
        if contestants[i] < np.random.uniform(0, 1):
            contestants.pop(i)
        i = (i + 1) % len(contestants)
    return contestants[0]


def simulate_multiple_bees(num_bees, probas):
    return np.unique([simulate_bee(probas) for _ in range(num_bees)], return_counts=True)


def make_a_table(tallies):
    i = tallies[0]
    j = tallies[1]
    for k in range(len(i)):
        print((i[k], j[k] / sum(j)))
    return [(i[k], j[k] / sum(j)) for k in range(len(i))]


if __name__ == '__main__':
    contestants = [i / 100 for i in range(90, 100)]
    print('Evaluating ascending with 100000 simulations: ')
    make_a_table(simulate_multiple_bees(100000, contestants))
    contestants.reverse()
    print('Evaluating descending with 100000 simulations: ')
    make_a_table(simulate_multiple_bees(100000, contestants))
