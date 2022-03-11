from collections import Counter

import numpy as np


def roll_dice(numdice=4, numfaces=6):
    return Counter(np.floor(np.random.uniform(1, numfaces, numdice)))


def getsums(dice):
    sums = set()
    for i1 in range(len(dice)):
        for i2 in range(i1 + 1, len(dice)):
            sums.add(dice[i1] + dice[i2])
    return sums


def exact_estimate(goals, numfaces=6):
    counter = 0
    for i1 in range(1, numfaces + 1):
        for i2 in range(1, numfaces + 1):
            for i3 in range(1, numfaces + 1):
                for i4 in range(1, numfaces + 1):
                    sums = getsums([i1, i2, i3, i4])
                    if len(goals.intersection(sums)) > 0:
                        counter += 1
    return counter / numfaces ** 4


def find_missing(goals, numfaces=6):
    missing = []
    for i1 in range(1, numfaces + 1):
        for i2 in range(1, numfaces + 1):
            for i3 in range(1, numfaces + 1):
                for i4 in range(1, numfaces + 1):
                    sums = getsums([i1, i2, i3, i4])
                    if len(goals.intersection(sums)) == 0:
                        missing += [[i1, i2, i3, i4]]

    return missing


if __name__ == '__main__':
    maxprob = 0
    maxlist = []

    for i1 in range(1, 13):
        for i2 in range(i1 + 1, 13):
            for i3 in range(i2 + 1, 13):
                for i4 in range(i3 + 1, 13):
                    if exact_estimate({i1, i2, i3, i4}) > maxprob:
                        maxlist = [i1, i2, i3, i4]
                        maxprob = exact_estimate({i1, i2, i3, i4})
    print(maxlist)
    print(maxprob, " or ", maxprob * 6 ** 4, "/", 6 ** 4)
