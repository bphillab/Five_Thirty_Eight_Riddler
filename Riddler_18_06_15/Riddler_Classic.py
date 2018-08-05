from numpy.random import negative_binomial
import numpy as np


def simulate_1_round():
    return sum([negative_binomial(1,1/(2*i-1),1)+1 for i in range(1,11)])


def simulate_n_rounds(num_rounds):
    return [simulate_1_round() for i in range(num_rounds)]


if __name__ == '__main__':
    temp = simulate_n_rounds(100000)
    print("Mean ")
    print(np.mean(temp)*2)
    print("Median ")
    print(np.median(temp)*2)
