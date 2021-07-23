import numpy as np


def check(arr):
    temp = np.append(arr[1:], 1)
    return max(temp - arr) < 0.1 and arr[0] < 0.1


def place_new_hold(wall, new_hold):
    where_to_place = np.searchsorted(wall, new_hold)
    return np.append(np.append(wall[:where_to_place], new_hold), wall[where_to_place:])


def one_round():
    wall = np.sort(np.random.random(10))
    counter = 10
    while not check(wall):
        new_hold = np.random.random()
        wall = place_new_hold(wall, new_hold)
        counter += 1
    return counter


if __name__ == '__main__':
    print("It will take on average ", np.mean([one_round() for _ in range(10000)]), " holds")
