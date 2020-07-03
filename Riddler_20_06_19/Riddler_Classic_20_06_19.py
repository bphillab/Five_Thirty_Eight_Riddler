"""
Riddler Classic
From Dean Ballard comes a riddle of radiant spheres and fatherhood, just in time for the summer solstice and Father’s
Day:

King Auric adored his most prized possession: a set of perfect spheres of solid gold. There was one of each size,
with diameters of 1 centimeter, 2 centimeters, 3 centimeters, and so on. Their brilliant beauty brought joy to his
heart. After many years, he felt the time had finally come to pass the golden spheres down to the next generation —
his three children.

He decided it was best to give each child precisely one-third of the total gold by weight, but he had a difficult
time determining just how to do that. After some trial and error, he managed to divide his spheres into three groups
of equal weight. He was further amused when he realized that his collection contained the minimum number of spheres
needed for this division. How many golden spheres did King Auric have?

Extra credit: How many spheres would the king have needed to be able to divide his collection among other numbers of
children: two, four, five, six or even more?
"""

from functools import lru_cache


def sum_of_cubes(i):
    return ((i + 1) ** 2 * i ** 2) / 4


@lru_cache(maxsize = None)
def solver_pair(n):
    if n == 1:
        return [1]
    return sorted([n ** 3 + i for i in solver_pair(n - 1)] + [n ** 3 - i for i in solver_pair(n - 1)], key = lambda
        x: abs(x))


@lru_cache(maxsize = None)
def solver_triplet(n):
    if n == 1:
        return [(0, 1, 0), (1, 0, 0), (0, 0, 1)]
    return sorted([(n ** 3 + i[0], i[1], i[2]) for i in solver_triplet(n - 1)] +
                  [(i[0], n ** 3 + i[1], i[2]) for i in solver_triplet(n - 1)] +
                  [(i[0], i[1], n ** 3 + i[2]) for i in solver_triplet(n - 1)],
                  key = lambda x: abs(x[0] - x[1]) + abs(x[0] - x[2]))
