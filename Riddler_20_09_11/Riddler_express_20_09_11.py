import numpy as np


def simulate_a_night(N):
    teams = np.random.choice(N, 3) + 1
    teams.sort()
    if teams[2] == teams[0] + teams[1]:
        return True
    return False


def run_several_nights(num_players, num_nights):
    results = [simulate_a_night(num_players) for _ in range(num_nights)]
    return np.mean(results)


if __name__ == '__main__':
    print(np.mean([run_several_nights(5, 10000) for _ in range(100)]))

