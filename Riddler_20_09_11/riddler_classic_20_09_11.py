import numpy as np


def sim_a_ride():
    """
    Simulates a random ride up the mountain player 0 is you, players 2,3 are the partners.
    :return: number of points earned
    """
    riders = np.random.choice(4, 4, replace = False)
    beat_solo = 0
    beat_duo = 0
    # figure out if we beat unpaired
    if riders[0] < riders[1]:
        beat_solo = 1
    # figure out if we beat the pair
    if riders[0] < min([riders[2], riders[3]]):
        beat_duo = 1
    if beat_solo == 1 and beat_duo == 1:
        return 5
    if beat_solo == 0 and beat_duo == 1:
        return 3
    if beat_solo == 1 and beat_duo == 0:
        return 2
    if beat_solo == 0 and beat_duo == 0:
        return 1
    print('Something dumb happened')
    return 1000000


def sim_multiple_runs(num_runs):
    return np.mean([sim_a_ride() for _ in range(num_runs)])


if __name__ == '__main__':
    runs = [sim_multiple_runs(10000) for _ in range(100)]
    print(np.mean(runs), " +/- ", np.std(runs))
