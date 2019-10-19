"""
Riddler Nation has two coins: the Dio, worth $538, and the Phantus, worth $19. When visiting on vacation, Riddler
National Bank will gladly convert your dollars into Dios and Phanti. For example, if you were to give a bank teller
$614, they’d return to you one Dio and four Phanti, since 614 = 1 × 538 + 4 × 19. But if you tried to exchange one
dollar more (i.e., $615), then alas, there is no combination of Dios and Phanti the teller could give you, and you won’t
get your money’s worth in local currency.

To make the bank teller’s job (and your vacation) as miserable as possible, you decide to bring the largest dollar
amount that cannot be converted into Riddler currency. How much money are we talking here? That is, what’s the largest
whole number that cannot be expressed as a sum of 19s and 538s?

Extra Credit: Word is that Riddler Nation is considering minting a third currency, worth $101. If they do, then what
would be the largest dollar amount that cannot be converted into Riddler currency?
"""

"""
This is an example of the Frobenius Coin Problem
https://en.wikipedia.org/wiki/Coin_problem
"""
from math import ceil

from numpy import unique


def solution_for_two(a, b):
    return a * b - a - b


def brute_force(s, ub=0, carry=[0]):
    if len(s) == 0:
        return carry, ub

    x = sorted(s)
    new_carry = carry

    if ub > 0:
        upperbound = ub

    if ub == 0:
        upperbound = solution_for_two(x[0], x[1])

    for j in carry:
        for i in range(1, ceil(upperbound / x[-1]) + 1):
            new_carry = new_carry + [x[-1] * i + j]
    new_carry = [i for i in new_carry if i <= upperbound]
    new_carry = [i for i in unique(new_carry)]
    return brute_force(x[:-1], upperbound, new_carry)


if __name__ == "__main__":
    print("Solution for 19, 538: ", solution_for_two(19, 538))
    sols, ub = brute_force([19, 101, 538])
    missing = max([i for i in range(1, ub + 1) if i not in sols])
    print("Solution for 19,101,538: ", missing)
