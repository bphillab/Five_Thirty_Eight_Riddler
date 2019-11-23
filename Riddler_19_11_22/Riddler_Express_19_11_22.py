"""
From Dave Moran comes a question about baseball’s unusual 2019 World Series:

In the World Series, one team hosts Games 1, 2, 6 and 7, while the other team hosts Games 3, 4 and 5. When the
Nationals beat the Astros last month, it marked the first time in World Series history that the home team lost all
seven games. On average, the home team actually wins about 54 percent of the time in baseball. Running the numbers,
you’ll quickly see that seven home losses is a once-in-a-lifetime event.

But putting seven aside for a moment, what’s the probability that the home team will lose at least six consecutive
games?

Extra credit: What’s the probability the home team will lose at least five consecutive games? Four consecutive games?
"""


"""
This problem can be solved analytically for 6 games fairly quickly:
<Insert binomial maths here>
Extra credit gets a bit more difficult because the number of consecutive losses may not always be realized if the 
tournament stops at one team winning 4. I will thus code up the possible outcomes below.
"""
import numpy as np


def shorten(arr):
    arr1 = arr
    temp = []
    score = [0, 0]
    while score[0] < 4 and score[1] < 4:
        temp = temp + [arr1[0]]
        score[arr1[0]] = score[arr1[0]] + 1
        arr1 = arr1[1:]
    return temp


def produce_all_tourney():
    temp = []
    for g1 in range(2):
        for g2 in range(2):
            for g3 in range(2):
                for g4 in range(2):
                    for g5 in range(2):
                        for g6 in range(2):
                            for g7 in range(2):
                                temp = temp + [shorten([g1, g2, g3, g4, g5, g6, g7])]
    return np.unique(temp)


def convert_to_home_games(arr):
    p1_home = [1, 2, 6, 7]
    p2_home = [3, 4, 5]
    temp = []
    for i in range(len(arr)):
        if i + 1 in p1_home:
            temp = temp + [arr[i]]
        if i + 1 in p2_home:
            temp = temp + [1 - arr[i]]
    return temp


def convert_to_proba(arr, p_h=0.54):
    p_a = 1 - p_h
    temp_prob = 1
    for i in arr:
        if i == 1:
            temp_prob = temp_prob * p_h
        if i == 0:
            temp_prob = temp_prob * p_a
    return temp_prob


def home_losses_in_a_row(arr):
    most_losses = 0
    temp_losses = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            temp_losses = temp_losses + 1
        if arr[i] == 1:
            if most_losses < temp_losses:
                most_losses = temp_losses
                temp_losses = 0
    if temp_losses > most_losses:
        most_losses = temp_losses
    return most_losses


if __name__ == '__main__':
    games = [convert_to_home_games(i) for i in produce_all_tourney()]
    in_a_row = [(home_losses_in_a_row(i), convert_to_proba(i)) for i in games]
    for i in range(7 + 1):
        print("Print number of games with at least", i, " wins:", sum([j[1] for j in in_a_row if j[0] >= i]))
