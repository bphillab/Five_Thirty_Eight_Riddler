"""
From Charlie Cordova comes a puzzle that brings logic and number theory to the lottery:

Five friends with a lot in common are playing the Riddler Lottery, in which each must choose exactly five numbers
from 1 to 70. After they all picked their numbers, the first friend notices that no number was selected by two or
more friends. Unimpressed, the second friend observes that all 25 selected numbers are composite (i.e., not prime).
Not to be outdone, the third friend points out that each selected number has at least two distinct prime factors.
After some more thinking, the fourth friend excitedly remarks that the product of selected numbers on each ticket is
exactly the same. At this point, the fifth friend is left speechless. (You can tell why all these people are friends.)

What is the product of the selected numbers on each ticket?

Extra credit: How many different ways could the friends have selected five numbers each so that all their statements
are true?
"""
import math

import numpy as np
from scipy.special import binom


def factorize(n):
    """Shamelessly stolen: https://en.wikipedia.org/wiki/Talk%3APrime_factorization_algorithm"""

    def isPrime(n):
        return not [x for x in range(2, int(math.sqrt(n)) + 1)
                    if n % x == 0]

    primes = []
    candidates = range(2, n + 1)
    candidate = 2
    while not primes and candidate in candidates:
        if n % candidate == 0 and isPrime(candidate):
            primes = primes + [candidate] + factorize(int(n / candidate))
        candidate += 1
    return primes


def remove_primes_prime_powers(x):
    return [i for i in x if len(np.unique(factorize(i))) > 1]


def remove_too_large(arr, primes, max_n, n_players):
    to_remove = sum([[j * i for j in range(1, n_players + 2)] for i in primes if (n_players + 1) * i > max_n], [])
    return [i for i in arr if i not in to_remove]


def multinom(num, grps):
    temp = grps
    if sum(grps) > num:
        return 0
    if sum(grps) < num:
        temp = temp + [num - sum(grps)]
    cum_prod = 1
    cum_sum = 0
    while cum_sum < num:
        cum_prod = cum_prod * binom(num - cum_sum, temp[0])
        cum_sum = cum_sum + temp[0]
        temp = temp[1:]
    return cum_prod


def calc_repeats(arr, gp=[2, 3, 5, 7, 11]):
    for i in gp:
        temp_counter = 0
        for j in [k for k in arr if k % i == 0]:
            temp_temp = j / i
            while int(temp_temp) == temp_temp:
                temp_counter = temp_counter + 1
                temp_temp = temp_temp / i
        print("Number of ", i, ": ", temp_counter)


if __name__ == '__main__':
    max_num = 70
    num_players = 5
    num_per_player = 5
    print("Starting with the range(1-70) we begin by removing primes and prime powers. ")
    start = [i for i in range(1, max_num + 1)]
    primes_in_range = [i for i in range(2, max_num + 1) if len(factorize(i)) == 1]
    start = remove_primes_prime_powers(start)
    print("Next we remove any numbers which have too large primes as a factor (6*p > 70)")
    start = remove_too_large(start, primes_in_range, max_num, num_players)
    print("Remaining elements: ", len(start))
    print("Need to remove: ", len(start) - num_players * num_per_player)
    good_primes = [2, 3, 5, 7, 11]
    calc_repeats(start, good_primes)
    print("We therefore must cut 35, 63,70")
    start = [i for i in start if i not in [35, 63, 70]]
    calc_repeats(start, good_primes)

    cum_prod = 1
    for i in start:
        cum_prod = cum_prod * i
    print("We have the 25 needed so next we could take the fifth root: ", int(cum_prod ** .2))
    print("Now onto the extra credit, we need to investigate distribution of primes/powers: ")
    factored = {i: factorize(i) for i in start}
    for i in good_primes:
        point = 1
        num_hits = len([k for k in factored.keys() if len([j for j in factored[k] if j == i]) == point])
        while num_hits > 0:
            num_hits = len([k for k in factored.keys() if len([j for j in factored[k] if j == i]) == point])
            if num_hits > 0:
                print(i, ": ", point, ": ", num_hits)
            point = point + 1
    print("First clues: the {50} can not be in the same group as {55}")
    print("           : the {54} can not be in the same group as {18,36,45}")
