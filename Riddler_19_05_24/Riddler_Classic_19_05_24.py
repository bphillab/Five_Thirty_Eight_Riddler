"""
Riddler Classic
From Dean Ballard, one small step for man, one giant problem for The Riddler:

Sometime in the near future people from Earth will land on Mars. Someone will step out of the landing pod and become the
 first human to leave his or her footprints on another planet.

Imagine two astronauts sitting in the pod, both of whom would love to take that first step. But they would also like to
decide which of them gets the honor in a fair manner, so they flip a coin. Despite the change in gravity, this method is
fair as long as the coin is fair. If there were four astronauts in the landing pod, then they could flip a fair coin
twice, assigning the four possible outcomes — heads-heads, heads-tails, tails-heads and tails-tails — to each of the
four astronauts. This would also be fair as long as the coins were fair.

But what if there were three astronauts in the landing pod? Then our fair coin doesn’t work so well. We could, for
example, assign three of the four possible outcomes — say heads-heads, heads-tails and tails-heads — to each of the
astronauts. Then, if the outcome were tails-tails, they could simply start over again with two more flips. This would
give an ever-increasing probability that a fair decision would eventually be made, but that could take a long time, and
the required number of flips would be unknown. And there’s a planet to walk on!

Another approach, however, is to use an “unfair coin” — one in which the probabilities of heads and tails are not equal.
Is it possible to make a fair choice among three astronauts with a fixed number of flips of an unfair coin?

You are able to set the coin’s probability of heads to any number you like between 0 and 1. You may flip the coin as
many times as you like, as long as that is some known, fixed number. And, you may assign any combination of possible
outcomes to each of the three astronauts.

Extra credit: What if there were five astronauts?
"""
from math import ceil
from scipy.special import binom


def find_sols(possible_values, target, possible_sizes=None, eps=0.000000001):
    if not possible_values:
        return abs(target)< eps, []

    possible_sizes_i = possible_sizes
    if possible_sizes is None:
        possible_sizes_i = [9999 for _ in possible_values]

    sols = []
    for i in range(min(ceil(target/possible_values[0])+1,possible_sizes_i[0]+1)):
        res, temp = find_sols(possible_values[1:], target - i*possible_values[0], possible_sizes_i[1:],eps)
        if res:
            if len(temp) == 0:
                sols = sols + [[i]]
            else:
                sols = sols + [[i]+j for j in temp]
    return sols != [], sols


def find_possible_sols(num_astro, num_flips, p, eps=0.000000001):
    target = 1/num_astro
    possible_values = [p**i * (1-p)**(num_flips-i) for i in range(num_flips+1)]
    possible_size = [int(binom(num_flips,i)) for i in range(num_flips+1)]
    return find_sols(possible_values, target, possible_size, eps)


"""
Solution ended up not requiring these functions:

The answer by its nature must be somewhat degenerate thus we are motivated to look for an ansatz that will make our life
easier. We can look for symmetric situations where the "middle" outcomes make up all but one of the answers. For three 
astronauts our ansatz takes the form of having all of the inner coefficients up to a modulo 2 make up 2/3 and the rest 
be the remaining 1/3. This works for N=4.

ie 2(1-p)^3 p + 3p^2 (1-p)^2 + 2(1-p) p^3 = 1/3
    p^4+(1-p)^4 = 1/3
    
For m astronauts we can get away with a similar ansatz up to modulo m-1. We then try to solve for p to make this 
possible.


"""