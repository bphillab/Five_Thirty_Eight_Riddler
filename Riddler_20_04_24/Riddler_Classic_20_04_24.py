"""
Riddler Classic
The Monty Hall problem is a classic case of conditional probability. In the original problem, there are three doors,
two of which have goats behind them, while the third has a prize. You pick one of the doors, and then Monty (who
knows in advance which door has the prize) will always open another door, revealing a goat behind it. It’s then up to
you to choose whether to stay with your initial guess or to switch to the remaining door. Your best bet is to switch
doors, in which case you will win the prize two-thirds of the time.

Now suppose Monty changes the rules. First, he will randomly pick a number of goats to put behind the doors: zero,
one, two or three, each with a 25 percent chance. After the number of goats is chosen, they are assigned to the doors
at random, and each door has at most one goat. Any doors that don’t have a goat behind them have an identical prize
behind them.

At this point, you choose a door. If Monty is able to open another door, revealing a goat, he will do so. But if no
other doors have goats behind them, he will tell you that is the case.

It just so happens that when you play, Monty is able to open another door, revealing a goat behind it. Should you
stay with your original selection or switch? And what are your chances of winning the prize?


"""

from random import sample

import numpy as np


def is_valid(doors):
    if doors[1] == "G" or doors[2] == "G":
        return True
    else:
        return False


def sim_doors():
    num_goats = np.random.choice(4)
    doors = sample(["C" if i < 3 - num_goats else "G" for i in range(3)], 3)
    while not is_valid(doors):
        num_goats = np.random.choice(4)
        doors = sample(["C" if i < 3 - num_goats else "G" for i in range(3)], 3)
    return doors


def sim_host():
    doors = sim_doors()
    if doors[0] == "C":
        return 1
    if doors[0] == "G":
        return 0


def run_many_sim(num_sim):
    return [sim_host() for _ in range(num_sim)]


def get_an_exact_solution():
    pass


def main():
    num_trials = 10000000
    sims = run_many_sim(num_trials)
    print("After ", num_trials, " staying wins ", np.mean(sims), " times.")


if __name__ == "__main__":
    main()
