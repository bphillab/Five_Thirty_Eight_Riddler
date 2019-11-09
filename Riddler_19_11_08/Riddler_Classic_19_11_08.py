"""This week’s Riddler Classic comes to us from Oren, who asked not to be further identified:

Now that Halloween has come and gone, your chances of getting free candy have similarly disappeared. Desperate for
sugar, you wander into the candy store, where three kinds of candy are being sold: Almond Soys (yummy, sounds vegan!),
Butterflingers and Candy Kernels.

You’d like to buy at least one candy and at most 100, but you don’t care precisely how many you get of each or how many
you get overall. So you might buy one of each, or you might buy 30 Almond Soys, six Butterflingers and 64 Candy Kernels.
As long as you have somewhere between one and 100 candies, you’ll leave the store happy.

But as a member of Riddler Nation, you can’t help but wonder: How many distinct ways are there for you to make your
candy purchase?"""

"""
Solution: This is a classic 'stars-and-bars' problem. The solution is to consider 4 types of candy and 100 candies to be
distributed. The fourth type would be a 'trash/non-realized' candy. One issue is that this allows for all trash so we 
subtract one for that.

Stars-and-bars has Binom(N+M,M) - Binom(min+M,min)


"""

from scipy.special import binom


def stars_and_bars(max_num_candy, num_types, min_candy):
    return int(
        binom(max_num_candy + num_types + 1 - 1, num_types) - binom(min_candy - 1 + num_types + 1 - 1, num_types))


if __name__ == '__main__':
    print("Number of ways for max of 100 candies, 3 kinds of candies, min of one candy selected: ",
          stars_and_bars(100, 3, 1))
