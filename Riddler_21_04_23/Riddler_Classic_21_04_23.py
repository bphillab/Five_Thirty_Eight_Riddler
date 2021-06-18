import numpy as np


def simulator(n, num_trial):
    switchSides = lambda x: x if x < 2 * n / 5 else 4 * n / 5 - x
    switchSidesvec = np.vectorize(switchSides)

    changeOccurred = lambda x: 1 if x > n / 2 else 0
    changevec = np.vectorize(changeOccurred)

    initial = switchSidesvec(np.random.binomial(4 * n / 5, 1 / 2, num_trial))
    final = np.random.binomial(n / 5, 1 / 2, num_trial)
    return np.mean(changevec(initial + final))
