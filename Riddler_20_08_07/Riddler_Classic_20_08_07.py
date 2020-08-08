"""
Riddler Classic
This week’s Riddler Classic is inspired by Kareem Carr:

We usually think of addition as an operation applied to a field like the rational numbers or the real numbers. And
there is good reason for that — as Kareem says, “Mathematicians have done all the hard work of figuring out how to
make calculations track with reality. They kept modifying and refining the number system until everything worked out.
It took centuries of brilliant minds to do this!”

Now suppose we defined addition another (admittedly less useful) way, using a classic model organism: the nematode.
To compute the sum of x and y, you combine groups of x and y nematodes and leave them for 24 hours. When you come
back, you count up how many you have — and that’s the sum!

It turns out that, over the course of 24 hours, the nematodes pair up, and each pair has one offspring 50 percent of
the time. (If you have an odd number of nematodes, they will still pair up, but one will be left out.) So if you want
to compute 1+1, half the time you’ll get 2 and half the time you’ll get 3. If you compute 2+2, 25 percent of the time
you get 4, 50 percent of the time you’ll get 5, and 25 percent of the time you’ll get 6.

While we’re at it, let’s define exponentiation for sums of nematodes. Raising a sum to a power means leaving that sum
of nematodes for the number of days specified by the exponent.

With this number system, what is the expected value of (1+1)4?

Extra credit: As N gets larger and larger, what does the expected value of (1+1)N approach?
"""

import numpy as np
from scipy.special import binom


def nem_sum(sm, max_len):
    x = int(np.floor(sm / 2))
    return np.array([binom(x, i - sm) / 2 ** x for i in range(max_len)])


def wait_a_day(arr):
    temp = np.zeros(len(arr))
    for i in range(len(arr)):
        temp = temp + arr[i] * nem_sum(i, len(arr))
    return temp


def find_weighted_sum(arr):
    sm = 0
    for i in range(len(arr)):
        sm = sm + i * arr[i]
    return sm


def find_sum_exp(sm, num_days, max_len):
    start = np.zeros(max_len)
    start[sm] = 1
    for i in range(num_days):
        start = wait_a_day(start)
    return start


def main(sm, exp, max_len):
    print(find_weighted_sum(find_sum_exp(sm, exp, max_len)))


if __name__ == '__main__':
    main(2, 4, 100)
