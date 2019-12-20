"""
From Mark Hannan comes a holiday party stumper:

You’re new at your job, and your office is voting on a theme for its holiday party. It’s fallen on you to record the
percent of your coworkers (including yourself) who voted for each one. Well, since you’re in a hurry, you just write
down everything in the percentage that comes before the decimal point. So for example, 35.0 percent, 35.17 percent
and 35.92 percent would all be written simply as “35 percent.”

After the votes are tallied, you found that the winner received 73 percent of the vote (at least, that’s what you
wrote down), while second place had 58 percent, and third place had 32 percent. Your first realization is that you
work with a bunch of cheaters who voted more than once. But your second thought is that you might be able to use this
information to figure out how many people work in your office. (As I said, you’re new, and this isn’t something you
know off the top of your head.)

Based on these percentages, what’s the minimum number of people who could work in your office?

Extra credit: Your office could be filled with many possible numbers of people. Based on the percentages given in the
problem, what’s the greatest number of people your office can’t have?
"""
from math import floor, ceil

import numpy as np


def your_scheme(x):
    return floor(x)


if __name__ == '__main__':
    to_check = [0.73, 0.58, 0.32]
    tol = 0.00001
    updater_min = 100
    updater_max = 0
    for i in range(100, 1, -1):
        if np.all([abs(your_scheme(ceil(i * j) * 100 / i) - j * 100) < tol for j in to_check]):
            updater_min = i
    for i in range(1, 300):
        if not np.all([abs(your_scheme(ceil(i * j) * 100 / i) - j * 100) < tol for j in to_check]):
            updater_max = i
    print("Minimum possible is: ", updater_min)
    print("Maximum possible is: ", updater_max)
