'''
Riddler Nation’s Jibriel Taha, an avid baseball fan, saw the following tweet from the Milwaukee Brewers’ beat writer
Adam McCalvy:


Inspired by the Brewers’ apparent mediocrity (they’ve since gone on a roll to clinch a playoff spot) Jibriel asks the
following:

If a baseball team is truly .500, meaning it has a 50 percent chance of winning each game, what’s the probability that
it has won two of its last four games and four of its last eight games?


'''

'''
Answer: The probability that you will have w wins and l losses is: Binomial(w+l,w)/2^{w+l}
        Probability of 2 of last 4 and 4 of last 8 is basically two sets of 4 winning 2 of them.
'''

from scipy.special import binom

if __name__ == "__main__":
    print(2 * 2, " ", binom(2 * 2, 2) / 4 ** 2)
    print(4 * 2, " ", (binom(2 * 2, 2) / 4 ** 2) ** 2)
