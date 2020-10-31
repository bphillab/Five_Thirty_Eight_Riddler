import numpy as np


def one_run(num_vars=2):
    a = np.random.uniform(0, 1, num_vars)
    while sum(a) > 1:
        a = np.random.uniform(0, 1, num_vars)
    return (a > 0.5).any() or sum(a) < 0.5


def multirun(numrun, num_vars=2):
    return np.mean([one_run(num_vars) for _ in range(numrun)])
