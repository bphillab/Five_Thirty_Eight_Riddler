import numpy as np


def trial(p):
    team1, team2 = np.random.binomial(5, p, 2)
    if team1 != team2:
        return 5
    counter = 5
    while team1 == team2:
        counter += 1
        team1, team2 = np.random.binomial(1, p, 2)
    return counter


if __name__ == "__main__":
    num_test = 10000
    print("Mean number of attempts is: ", np.mean([trial(.7) for _ in range(num_test)]))
