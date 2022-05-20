import numpy as np

numplayers = 10


def trial():
    e1 = np.arange(numplayers)
    e2 = np.arange(numplayers)
    e3 = np.arange(numplayers)
    np.random.shuffle(e1)
    np.random.shuffle(e2)
    np.random.shuffle(e3)
    score = e1 + e2 + e3
    return np.sort(score)[9]


min([trial() for _ in range(10000)])
