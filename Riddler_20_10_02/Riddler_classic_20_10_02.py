'''
From mathematician (and author of Basic Probability: What Every Math Student Should Know) Henk Tijms comes a choice
matter of chance and chocolate:

I have 10 chocolates in a bag: Two are milk chocolate, while the other eight are dark chocolate. One at a time,
I randomly pull chocolates from the bag and eat them — that is, until I pick a chocolate of the other kind. When I
get to the other type of chocolate, I put it back in the bag and start drawing again with the remaining chocolates. I
keep going until I have eaten all 10 chocolates.

For example, if I first pull out a dark chocolate, I will eat it. (I’ll always eat the first chocolate I pull out.)
If I pull out a second dark chocolate, I will eat that as well. If the third one is milk chocolate, I will not eat it
(yet), and instead place it back in the bag. Then I will start again, eating the first chocolate I pull out.

What are the chances that the last chocolate I eat is milk chocolate?

'''

import numpy as np


def one_round(Ndark, Nmilk):
    chocolates = [1] * Ndark + [0] * Nmilk
    chocolates = np.random.choice(chocolates, Ndark + Nmilk, replace = False)
    ndark_eaten = 0
    nmilk_eaten = 0
    chocolate_start = 0
    while ndark_eaten < Ndark and nmilk_eaten < Nmilk:
        chocolate_start = chocolates[0]
        if chocolate_start == 0:
            nmilk_eaten += 1
        if chocolate_start == 1:
            ndark_eaten += 1
        chocolates = chocolates[1:]
        while chocolates[0] == chocolate_start:
            if chocolate_start == 0:
                nmilk_eaten += 1
            if chocolate_start == 1:
                ndark_eaten += 1
            chocolates = chocolates[1:]
        chocolates = np.random.choice(chocolates, len(chocolates), replace = False)
    return chocolate_start


def multi_round(Nround, Ndark, Nmilk):
    return [one_round(Ndark, Nmilk) for _ in range(Nround)]
