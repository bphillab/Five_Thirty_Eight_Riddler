"""
Riddler Classic
After a long night of frivolous quackery, two delirious ducks are having a difficult time finding each other in their
pond. The pond happens to contain a 3×3 grid of rocks.

Every minute, each duck randomly swims, independently of the other duck, from one rock to a neighboring rock in the
3×3 grid — up, down, left or right, but not diagonally. So if a duck is at the middle rock, it will next swim to one
of the four side rocks with probability 1/4. From a side rock, it will swim to one of the two adjacent corner rocks
or back to the middle rock, each with probability 1/3. And from a corner rock, it will swim to one of the two
adjacent side rocks with probability 1/2.

If the ducks both start at the middle rock, then on average, how long will it take until they’re at the same rock
again? (Of course, there’s a 1/4 chance that they’ll swim in the same direction after the first minute, in which case
it would only take one minute for them to be at the same rock again. But it could take much longer, if they happen to
keep missing each other.)

Extra credit: What if there are three or more ducks? If they all start in the middle rock, on average, how long will
it take until they are all at the same rock again?
"""

import numpy as np

neighbors = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [6, 4, 8], [7, 5]]


def duck_turn(duck):
    return np.random.choice(neighbors[duck])


def ducks_turn(ducks):
    return [duck_turn(i) for i in ducks]


def monte_carlo_way(num_ducks=2, num_sims=1000000, upper_bounds=1000):
    tally = 0
    for _ in range(num_sims):
        ducks = [4 for _ in range(num_ducks)]
        ducks = ducks_turn(ducks)
        count = 1
        while count <= upper_bounds and len(np.unique(ducks)) > 1:
            ducks = ducks_turn(ducks)
            count = count + 1
        if len(np.unique(ducks)) == 1:
            tally = tally + count
    return tally / num_sims


# Stolen from: https://stackoverflow.com/questions/28824874/pythonic-way-to-do-base-conversion
def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)


def str_base(number, base):
    while number > 0:
        number, digit = divmod(number, base)
        yield digit_to_char(digit)


def i_to_coor(i, num_ducks):
    return [int(j) for j in list(''.join([_ for _ in str_base(i, 9)])[::-1].zfill(num_ducks))]


def coor_to_i(coors):
    coor_temp = coors
    coor_temp.reverse()
    return sum([9 ** i * coor_temp[i] for i in range(len(coors))])


def are_neighbors(i, j, num_ducks):
    coors_i = i_to_coor(i, num_ducks)
    coors_j = i_to_coor(j, num_ducks)
    for k in range(len(coors_i)):
        if not coors_j[k] in neighbors[coors_i[k]]:
            return False
    return True


def count_neighbors(i, num_ducks):
    coors_i = i_to_coor(i, num_ducks)
    prod = 1
    for j in coors_i:
        prod = prod * len(neighbors[j])
    return prod


def lin_alg_way(num_ducks):
    mat = []
    for i in range(9 ** num_ducks):
        num_neighbors = count_neighbors(i, num_ducks)
        mat = mat + [[are_neighbors(i, j) / num_neighbors for j in range(9 ** num_ducks)]]
    mat_inv = np.linalg.inv(mat)


if __name__ == '__main__':
    x = monte_carlo_way()
    print('Num times: ', x)
