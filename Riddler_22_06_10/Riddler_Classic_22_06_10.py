import numpy as np


def turn(position):
    newpos = position + np.random.uniform(-0.2, 0.2)
    while newpos > 0.5 or newpos < -0.5:
        newpos = position + np.random.uniform(-0.2, 0.2)
    return newpos


def round(numturns):
    position = 0
    for _ in range(numturns):
        position = turn(position)
    return position


def fullsim(numsims, numturns):
    endpos = []
    for _ in range(numsims):
        endpos += [round(numturns)]
    return endpos


class Simulator:
    def __init__(self, numsites):
        self.numsites = numsites
        self.sites = [1 / numsites for _ in range(numsites)]
        self.len_site = 1 / numsites
        self.numrelevant = [0 for _ in range(self.numsites)]
        self.windowlen = 1.0
        for i in range(self.numsites):
            for j in range(-int(self.windowlen / self.len_site), int(self.windowlen / self.len_site) + 1):
                if 0 <= i + j < len(self.sites):
                    self.numrelevant[i] = self.numrelevant[i] + 1

    def update(self):
        updated_sites = [0 for _ in range(self.numsites)]
        for i in range(self.numsites):
            for j in range(-int(self.windowlen / self.len_site), int(self.windowlen / self.len_site) + 1):
                if 0 <= i + j < len(self.sites):
                    updated_sites[i + j] += self.sites[i] / self.numrelevant[i]
        self.sites = updated_sites


import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = Simulator(100)
    for i in range(1000):
        x.update()
    plt.plot(x.sites)
    plt.show()
