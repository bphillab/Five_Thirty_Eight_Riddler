from math import floor
from numpy.random import uniform


exp_prs_len = 3/2


def next_step(pos_0, pos_1,l):
    num_steps = floor((pos_1 - pos_0)/2)
    if uniform(0,1,1)<0.5:
        pos_0 = pos_0 + num_steps
        pos_1 = l
        dt = num_steps
    else:
        pos_0 = 1
        pos_1 = pos_1 - num_steps
        dt = num_steps
    return pos_0, pos_1, dt + exp_prs_len


def simulate(l):
    time = 0
    pos_0 = 1
    pos_1 = l
    while pos_0 !=l and pos_1 != 1:
        if pos_0 == l-1 or pos_1 == 2:
            dt = 1
            pos_0 = pos_0 + 1
            pos_1 = pos_1 - 1
        else:
            pos_0, pos_1, dt = next_step(pos_0, pos_1,l)
        time = time + dt
    return time


def simulate_many(n,l):
    return [simulate(l) for i in range(n)]

if __name__ == '__main__':
    print('Estimated length for 8: ', sum(simulate_many(1000000,8))/1000000)
    print('Estimated length for 58,59,60: ',sum(simulate_many(100000,58)),
          ' ',sum(simulate_many(100000,59))/100000,' ',sum(simulate_many(100000,60))/100000)
