import numpy as np


def trial():
    fatch, fetch, fitch = np.random.uniform(0, 1, 3)
    if fetch > fatch and fitch > fatch:
        return 1
    if fetch < fatch and fitch < fatch:
        return 1
    else:
        return 0


if __name__ == "__main__":
    num_try = 10000
    print("Probability of same color is: ", np.mean([trial() for _ in range(num_try)]))
