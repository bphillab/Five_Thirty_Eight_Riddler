import sys
from math import e

import numpy as np
from scipy.special import binom


class Memoize:
    '''Stolen memoization code'''
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        # Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]


def get_partition_function(current_rank, so_far, total):
    '''Essentially something to let me gather the probability distribution for adding to rank'''
    remaining = total - so_far
    return np.array(
        [binom(current_rank + i, i) * binom(total - current_rank - i - 1, remaining - i) for i in range(remaining + 1)])


@Memoize
def score_stop(current_rank, so_far, total):
    '''Score if you stop'''
    partition_function = get_partition_function(current_rank, so_far, total)
    denom = sum(partition_function)
    expected_value = -sum([partition_function[i] * (current_rank + i) / denom for i in range(len(partition_function))])
    return expected_value


@Memoize
def optimal_decider(current_rank, so_far, total):
    '''At each iteration decide to continue or stop'''
    remaining = total - so_far
    if remaining == 0:
        return -current_rank
    expected_score_if_continue = sum(
        [optimal_decider(i, so_far + 1, total) * 1 / (so_far + 1) for i in range(so_far + 1)])
    expected_score_if_stop = score_stop(current_rank, so_far, total)
    return np.max([expected_score_if_continue, expected_score_if_stop])


@Memoize
def optimize_all(num_suitor):
    return 1 - optimal_decider(0, 1, num_suitor)


def main(num_suit):
    sys.setrecursionlimit(num_suit * 10)
    print("For ", num_suit, " suitors the minimal rank score is: ", optimize_all(num_suit))
    print("Compare for large in with ", 1 + e)

if __name__ == '__main__':
    main(10)
