"""
Riddler Express
From Taylor Firman, the unluck of the draw:

Lotería is a traditional Mexican game of chance, akin to bingo. Each player receives a four-by-four grid of images.
Instead of a comically large rotating bin of numbered balls, the caller randomly draws a card from a deck containing all
54 possible images. If a player has that image on their grid, they mark it off. The exact rules can vary, but in this
version, the game ends when one of the players fills their entire card (and screams “¡Lotería!”). Each of the 54
possible images can only show up once on each card, but other than that restriction, assume that image selection and
placement on each player’s grid is random.

One beautiful day, you and your friend Christina decide to face off in a friendly game of Lotería. What is the
probability that either of you ends the game with an empty grid, i.e. none of your images was called? How does this
probability change if there were more or fewer unique images? Larger or smaller player grids?
"""

"""
Solvers Note: An exact solution to this problem can be derived from first principles.
1) Note that for cards of size n,m and N symbols the probability of selecting 2 cards with no symbol overlap is:
    Binom(N,n) Binom(N-n,m)/(Binom(N,n)*Binom(N,m))

2) Next given that the two cards do not overlap the probability of winning with the other card having any spaces is:
  1/Binom(n+m,n) + 1/Binom(n+m,m)

3) The total probability is thus
   (Binom(N,n) Binom(N-n,m)/(Binom(N,n) Binom(m)))*(1/Binom(n+m,n)+1/Binom(n+m,m))  
"""

from scipy.special import binom
from random import uniform, sample


def two_card_exact(n, m):
    """
    A function that will take two cards of (possibly differing) sizes and returns the probability that a card is filled
    while the other card is left empty
    :param n: number of entries on card1
    :param m: number of entries on card2
    :return:  probability that a card is filled while the other is empty
    """
    return 1/binom(n+m,n)+1/binom(n+m,m)


def two_card_trial(n, m):
    """
    Simulates a trial, returns true if one card if full and the other is empty
    :param n:
    :param m:
    :return:

    """
    n_left= n
    m_left = m
    while n_left > 0 and m_left > 0:
        draw = uniform(0,1) < n_left/(n_left+m_left)
        if draw:
            n_left = n_left - 1
        if not draw:
            m_left = m_left - 1
    return n_left == n or m_left == m


def two_card_sim(n, m, num_trials):
    """
    Function that simulates filling cards num_trial times
    :param n: size of card 1
    :param m: size of card 2
    :param num_trials: number of trials
    :return: percent of the time out of num_trials that one card was filled while the other was empty
    """
    n_true = 0
    for _ in range(num_trials):
        if two_card_trial(n, m):
            n_true = n_true + 1
    return n_true/num_trials


def different_cards_exact(N, n, m):
    """
    Calculates exact chance that cards of size n,m are drawn with no overlap
    :param N: number of symbols
    :param n: size of card 1
    :param m: size of card 2
    :return: probability
    """
    return binom(N, n)*binom(N-n, m)/(binom(N, n)*binom(N, m))


def different_cards_trial(N, n, m):
    card1 = set(sample(range(N),n))
    card2 = set(sample(range(N),m))
    return not card1.intersection(card2)


def different_cards_sim(N, n, m, num_trials):
    n_true = 0
    for _ in range(num_trials):
        if different_cards_trial(N, n, m):
            n_true = n_true + 1
    return n_true/num_trials


if __name__ == "__main__":
    print("For 54 symbols on a 4x4 grid the probability of filling your board without the other player touching theirs "
          "is: "
          )
    print("from exact calculations: ", two_card_exact(16,16)*different_cards_exact(54,16,16))
    print("from simulation: ", two_card_sim(16, 16,10000) * different_cards_sim(54, 16, 16,10000))
    print("For a more likely to succeed number of symbols, 100, size of cards,4: ")
    print("from exact calculations: ", two_card_exact(4,4)*different_cards_exact(100,4,4))
    print("from simulation: ", two_card_sim(4, 4,10000) * different_cards_sim(100, 4, 4,10000))

