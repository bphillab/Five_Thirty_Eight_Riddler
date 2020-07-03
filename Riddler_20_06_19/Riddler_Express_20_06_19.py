"""
Riddler Express
I have a coin with a sun on the front and a moon on the back. I claim that on most days, it’s a fair coin,
with a 50 percent chance of landing on either the sun or the moon.

But once a year, on the summer solstice, the coin absorbs the sun’s rays and exhibits a strange power: It always
comes up the opposite side as the previous flip.

Of course, you are skeptical of my claim. You figure there’s a 1 percent chance that the coin is magical and a 99
percent chance that it’s just an ordinary fair coin. You then ask me to “prove” the coin is magical by flipping it
some number of times.

How many successfully alternating coin flips will it take for you to think there’s a 99 percent chance the coin is
magical (or, more likely, that I’ve rigged it in some way so it always alternates)?
"""


def bayes_rule_for_this(prior):
    return 2 * prior / (1 + prior)


def main():
    initial_prior = 0.01
    count = 0
    prior = initial_prior
    end = 0.99
    while prior < end:
        count = count + 1
        prior = bayes_rule_for_this(prior)
    print("99% confident after: ", count, " moves!")


if __name__ == '__main__':
    main()
