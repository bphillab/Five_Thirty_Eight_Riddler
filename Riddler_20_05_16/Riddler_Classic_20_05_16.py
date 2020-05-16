'''
Riddler Classic
Since it was impossible to complete the game of sudoku, you might instead enjoy passing the time with a game of
Dungeons & Dragons, courtesy of Emma Knight:

The fifth edition of Dungeons & Dragons introduced a system of “advantage and disadvantage.” When you roll a die
“with advantage,” you roll the die twice and keep the higher result. Rolling “with disadvantage” is similar,
except you keep the lower result instead. The rules further specify that when a player rolls with both advantage and
disadvantage, they cancel out, and the player rolls a single die. Yawn!

There are two other, more mathematically interesting ways that advantage and disadvantage could be combined. First,
you could have “advantage of disadvantage,” meaning you roll twice with disadvantage and then keep the higher result.
Or, you could have “disadvantage of advantage,” meaning you roll twice with advantage and then keep the lower result.
With a fair 20-sided die, which situation produces the highest expected roll: advantage of disadvantage, disadvantage
of advantage or rolling a single die?

Extra Credit: Instead of maximizing your expected roll, suppose you need to roll N or better with your 20-sided die.
For each value of N, is it better to use advantage of disadvantage, disadvantage of advantage or rolling a single die?
'''
import numpy as np


def base_prob(n):
    return [1 / n for i in range(n)]


def dumb_way_advantage(probs):
    return [2 * sum(probs[:i]) * probs[i] + probs[i] * probs[i] for i in range(len(probs))]


def dumb_way_disadvantage(probs):
    return [2 * sum(probs[i:]) * probs[i] - probs[i] * probs[i] for i in range(len(probs))]


def main(num_sides=20):
    base = base_prob(num_sides)
    adv = dumb_way_advantage(base)
    dis = dumb_way_disadvantage(base)
    adv_dis = dumb_way_advantage(dis)
    dis_adv = dumb_way_disadvantage(adv)
    print('Determining expected_values: ')
    print('Roll one die: ', '%0.4f' % np.sum([base[i] * (i + 1) for i in range(num_sides)]))
    print('Advantage of disadvantage: ', '%0.4f' % np.sum([adv_dis[i] * (i + 1) for i in range(num_sides)]))
    print('Disadvantage of advantage: ', '%0.4f' % np.sum([dis_adv[i] * (i + 1) for i in range(num_sides)]))
    print('EC: ')
    print("To Beat \t 1 die \t Adv of dis \t Dis of adv")
    for i in range(20):
        print(i + 1, "\t\t\t", '%0.4f' % sum(base[i:]), "\t", '%0.4f' % sum(adv_dis[i:]), "\t",
              '%0.4f' % sum(dis_adv[i:]))


if __name__ == '__main__':
    main()
