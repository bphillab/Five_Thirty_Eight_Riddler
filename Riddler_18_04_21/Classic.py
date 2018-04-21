import numpy as np


def get_T(omega):
    return np.random.uniform(1, omega, 1)


def simulate_cross(omega, num_times):
    """
    :param omega: Largest value for T
    :param num_times: number of iterations to run
    :return: Average waiting time before making it to restaurant
    """
    times = []
    for i in range(num_times):
        # Decide to cross
        temp_time = 0
        T = get_T(omega)
        t_obs = np.average([1]+ np.ceil(np.random.uniform(1, T, 2)))
        t_this = np.max(np.append(np.ceil(np.random.uniform(-T, T, 1)),0))
        if t_this < t_obs:
            times = times + [t_this]
        else:
            times = times + [np.max(np.append(np.ceil(np.random.uniform(-T, T, 1)),0))]

    return times

print("Trying until I reach 1: ")
omega = 1
while(np.mean(simulate_cross(omega, 10000))< 1):
    omega = omega+1

print("Breaks 1 at: ", omega)