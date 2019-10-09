"""
In the World Cup’s group stage, each group of four teams plays a round
robin, with every team playing the other teams once each. A win is worth
3 points, a draw 1 point, and a loss 0 points. The points are tallied,
and the top two teams in each group advance to the knockout stage. For
a given group — let’s pick Group A, which includes Russia, Saudi Arabia,
Egypt and Uruguay — how many different final standings, including point
totals, are possible for the group stage?
"""

import numpy as np


def interpret_game(a):
    if a==-1:
        return 0,3
    if a==0:
        return 1,1
    if a==1:
        return 3,0


def interpret_set(set):
    score_1 = 0
    score_2 = 0
    score_3 = 0
    score_4 = 0

    score_1, score_2 = score_1 + interpret_game(set[0])[0], score_2 + interpret_game(set[0])[1]
    score_1, score_3 = score_1 + interpret_game(set[1])[0], score_3 + interpret_game(set[1])[1]
    score_1, score_4 = score_1 + interpret_game(set[2])[0], score_4 + interpret_game(set[2])[1]
    score_2, score_3 = score_2 + interpret_game(set[3])[0], score_3 + interpret_game(set[3])[1]
    score_2, score_4 = score_2 + interpret_game(set[4])[0], score_4 + interpret_game(set[4])[1]
    score_3, score_4 = score_3 + interpret_game(set[5])[0], score_4 + interpret_game(set[5])[1]

    return [score_1, score_2, score_3, score_4]


def get_all_sets():
    scores = [[]]
    for g1 in range(-1,2):
        for g2 in range(-1,2):
            for g3 in range(-1, 2):
                for g4 in range(-1, 2):
                    for g5 in range(-1, 2):
                        for g6 in range(-1, 2):
                            scores = scores+[interpret_set([g1,g2,g3,g4,g5,g6])]
    return np.unique(scores)


if __name__ == '__main__':
    print(len(get_all_sets()[1:]))