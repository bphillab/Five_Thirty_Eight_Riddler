from random import randint

from numpy import mean


def exact_calc2(x, y, d):
    return (x * (x + 1) + d * (y) * (y + 1) + 200) / (2 * (x + y + 1))


def collect_stats2(num_games, threshu, threshl, d):
    return mean([play_a_round2(threshu, threshl, d) for _ in range(num_games)])


def play_a_round2(threshu, threshl, d):
    curr = randint(0, 99)
    count = 1
    while curr > 0:
        curr = strat2(curr, threshl, threshu)
        count = count + 1
    return count


def strat2(curr, threshl, threshu):
    if curr <= threshl:
        return curr - 1
    if 100 - curr <= threshu:
        return (curr + 1) % 100
    else:
        return randint(0, 99)


if __name__ == '__main__':
    d = 1
    rand_selected_u = [randint(0, 49) for _ in range(10)]
    rand_selected_l = [randint(0, 49) for _ in range(10)]
    x = []
    y = []
    for i in range(len(rand_selected_l)):
        x = x + [collect_stats2(10000, rand_selected_u[i], rand_selected_l[i], d)]
        y = y + [exact_calc2(rand_selected_l[i], rand_selected_u[i], d)]
    print("Checking a few examples to establish credible: ")
    for i in range(len(rand_selected_l)):
        print("Testing ", i, " percent error:", (x[i] - y[i]) / x[i])
