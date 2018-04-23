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
    dont_cross_correct = []
    i = 0
    while i < num_times:
        # Decide to cross
        t = get_t(omega)
        if np.ceil(np.random.uniform(0,t,1))[0] != 1:
            continue

        vert_or_horiz = np.random.choice(range(2),1)[0]  # type: integer
        i = i + 1
        t1 = 0
        t2 = 1
        t3 = np.maximum(np.ceil(np.random.uniform(-t,t,1)),0)[0]
        t4 = np.maximum(np.ceil(np.random.uniform(-t,t,1)),[0])[0]
        t5 = 0
        t6 = 0
        t7 = np.maximum(np.ceil(np.random.uniform(-t,t,1)),[0])[0]
        cross_time = t1+t3+t4
        times_cross = times_cross + [t1+t3+t4]
        if vert_or_horiz == 1:
            dont_cross_time = t2 + t6 + t7
            times_dont_cross = times_dont_cross + [t2 + t6 + t7]
        if vert_or_horiz == 0:
            dont_cross_time = t2 + t5 + t4
            times_dont_cross = times_dont_cross + [t2 + t5 + t4]
        if cross_time > dont_cross_time:
            dont_cross_correct = dont_cross_correct+[1]
        else:
            dont_cross_correct = dont_cross_correct+[0]
    return np.mean(times_cross), np.mean(times_dont_cross), np.mean(dont_cross_correct)


if __name__ == '__main__':
    print('Starting at 1, trying until cross threshold:')
    i = 1
    tempx, tempy, percent_right = simulate_cross(i, 10000)
    while tempx < tempy:
        i = i+1
        tempx, tempy, percent_right = simulate_cross(i, 10000)

    print('Crossed threshold at i = ', i)
    print('Diagnostics: ')
    print(tempx)
    print(tempy)
    print(percent_right)
    print('Exact solution based on harmonic number gives:')
    print('2.09069')
    print('2.04534')
