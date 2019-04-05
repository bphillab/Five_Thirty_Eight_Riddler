import numpy as np


def latte_sim(num_lattes):
    cards = [num_lattes,num_lattes]
    draws = np.random.binomial(1,0.5,101)
    i=0
    while cards[0] >= 0 and cards[1] >= 0:
        cards[draws[i]] = cards[draws[i]] - 1
        i = i + 1
    if cards[0] >= 0:
        return cards[0]
    if cards[1] >= 0:
        return cards[1]


def sim_mult_latte(num_lattes, num_trials):
    results = [latte_sim(num_lattes) for _ in range(num_trials)]
    return np.mean([i>0 for i in results]), np.mean(results)


if __name__ == '__main__':
    num_latte = 50
    num_trials = 10000
    latte_results = sim_mult_latte(num_latte, num_trials)
    print('After ', num_trials, ' trials ', latte_results[0]*100,
          ' percent of the time at least one latte was on the other card')
    print('After ', num_trials, ' trials there were on average ',
           latte_results[1], ' lattes left on the other card.')
