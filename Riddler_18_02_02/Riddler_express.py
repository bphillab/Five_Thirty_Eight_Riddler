import numpy as np
from scipy.special import binom

def sim_a_bottle(num_red_pills=30,num_blue_pills=30):
    num_pills = num_red_pills+num_blue_pills
    bottle = np.random.choice(['R']*num_red_pills + ['B']*num_blue_pills,num_pills)
    good_pills = 0
    bad_pills = 0
    for i in range(int(num_pills/4)):
        pills_drawn = bottle[i:i+4]
        num_good = (pills_drawn == 'R').sum()
        num_bad = (pills_drawn=='B').sum()
        good_pills += min(num_good,2)
        bad_pills += max(num_bad-2, 0)
    return good_pills/(good_pills+bad_pills)


def sim_bottles(num_bottles, num_red=30,num_blue=30):
    return [sim_a_bottle(num_red,num_blue) for i in range(num_bottles)]


class Memoize:

    '''Memoization procedure from:
     https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python'''

    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

@Memoize
def calc_bottle(num_red, num_blue):
    if num_red == 0 and num_blue == 0:
        return 0
    return np.sum([binom(num_red,i)*binom(num_blue,4-i)/binom(num_red+num_blue,4)*(max([i-2,0])+calc_bottle(num_red-i,num_blue+i-4)) for i in range(max(0,4-num_blue),1+min(num_red,4))])


if __name__ == '__main__':
    print("Calculation from memoizaiton/dynamic programming approach: ",1-calc_bottle(30,30)/30)
    print("Calculation from monte carlo approach: ", np.mean(sim_bottles(10000,30,30)))

