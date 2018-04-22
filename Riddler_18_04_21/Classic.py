import numpy as np


def get_t(omega):
    return np.floor(np.random.uniform(1, omega+1, 1))[0]

def simulate_cross(omega, num_times):
    """
    :param omega: Largest value for T
    :param num_times: number of iterations to run
    :return: Average waiting time before making it to restaurant
    """
    times_cross = []
    times_dont_cross = []
    i = 0
    while i < num_times:
        # Decide to cross
        t = get_t(omega)
        if np.ceil(np.random.uniform(0,t,1))[0] != 1:
            continue

        vert_or_horiz = np.random.choice(range(2),1)[0]
        i = i + 1
        t1 = 0
        t2 = 1
        t3 = np.maximum(np.ceil(np.random.uniform(-t,t,1)),0)[0]
        t4 = np.maximum(np.ceil(np.random.uniform(-t,t,1)),[0])[0]
        t5 = 0
        t6 = 0
        t7 = np.maximum(np.ceil(np.random.uniform(-t,t,1)),[0])[0]
        times_cross = times_cross + [t1+t3+t4]
        if vert_or_horiz == 1:
            times_dont_cross = times_dont_cross + [t2 + t6 + t7]
        if vert_or_horiz == 0:
            times_dont_cross = times_dont_cross + [t2 + t5 + t4]
    return np.mean(times_cross), np.mean(times_dont_cross)

if __name__ == '__main__':
    print('Starting at 1, trying until cross threshold:')
    i = 1
    tempx, tempy = simulate_cross(i, 10000)
    while tempx < tempy:
        i = i+1
        tempx, tempy = simulate_cross(i, 10000)

    print('Crossed threshold at i = ', i)
    print('Diagnostics: ')
    print(tempx)
    print(tempy)