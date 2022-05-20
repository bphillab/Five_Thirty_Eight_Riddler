from collections import Counter

import numpy as np


def roll_dice(num_dice=4, uniq=[]):
    num_rep = num_dice - len(uniq)
    result = np.ceil(np.random.uniform(0, 4, num_rep)).tolist() + uniq
    return result


def count_unique(dice):
    ct = Counter()
    for i in dice:
        ct[i] += 1
    return {j for j in ct if ct[j] == 1}


numruns = 10000
results = []

for i in range(numruns):
    uniques = 9999
    un = []
    while uniques != 0 and uniques != 4:
        dc = roll_dice(4, un)
        un = list(count_unique(dc))
        uniques = len(un)
    results += [uniques]

results
