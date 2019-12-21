"""
Riddler Classic
From Kathy Bischoping comes a question we’ve all asked ourselves at one time or another:

I have 10 pairs of socks in a drawer. Each pair is distinct from another and consists of two matching socks. Alas,
I’m negligent when it comes to folding my laundry, and so the socks are not folded into pairs. This morning,
fumbling around in the dark, I pull the socks out of the drawer, randomly and one at a time, until I have a matching
pair of socks among the ones I’ve removed from the drawer.

On average, how many socks will I pull out of the drawer in order to get my first matching pair?

(Note: This is different from asking how many socks I must pull out of the drawer to guarantee that I have a matching
pair. The answer to that question, by the pigeonhole principle, is 11 socks. This question is instead asking about
the average.)

Extra credit: Instead of 10 pairs of socks, what if I have some large number N pairs of socks?
"""


def exact_sol(num_pairs):
    return sum([i * (i - 1) / (2 * num_pairs + 1 - i) * prods(i, num_pairs) for i in range(1, num_pairs + 2)])


def prods(j, num_pairs):
    if j == 1:
        return 1
    return (1 - (j - 2) / (2 * num_pairs + 2 - j)) * prods(j - 1, num_pairs)


if __name__ == '__main__':
    print("For 10 pairs: ", exact_sol(10))
