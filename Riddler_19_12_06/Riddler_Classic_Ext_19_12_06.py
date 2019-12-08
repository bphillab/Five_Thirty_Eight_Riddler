from random import randint

from numpy import mean


def exact_calc2(thresh):
    return thresh * (thresh + 1) / (2 * thresh + 1) + 100 / (2 * thresh + 1)


def collect_stats2(num_games, thresh):
    return mean([play_a_round2(thresh) for _ in range(num_games)])


def play_a_round2(thresh):
    curr = randint(0, 99)
    count = 1
    while curr > 0:
        curr = strat2(curr, thresh)
        count = count + 1
    return count


def strat2(curr, thresh):
    if curr <= thresh:
        return curr - 1
    if 100 - curr <= thresh:
        return (curr + 1) % 100
    else:
        return randint(0, 99)
