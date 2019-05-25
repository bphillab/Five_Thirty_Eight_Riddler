"""
Riddler Express
From Benni Trachtenberg, it’s time to dust off your football manager’s blazer just in time for the women’s World Cup:

A soccer coach is assembling a team of 11 players to compete in the Riddler League. (For the sake of this problem, all 
players are invincible and will play the entirety of every game of the season.) The coach may pick any player he wants 
from an infinite pool of players. It’s hard to remember that many names, so each player wears a jersey with a unique 
positive integer on the back (so that there is a player for every integer). That number also represents the average 
number of games needed for her to score a goal.

The coach would like his team to average exactly two goals per game but would also like for his weakest player to be as 
strong as possible. What number does the ideal weakest player wear? What are the numbers of the other 10 players the 
coach should select?
"""

from itertools import combinations


def test_all_combinations(high, num, goal):
    """
    Function that tests all combinations to find combinations of players that will match the goal
    :param high: Highest number of players to consider
    :param num:  Number of players on a team
    :param goal: Number of goals per game
    :return: Set of players that fulfill the requirements
    """
    to_test = combinations([1/i for i in range(1, 1+high)], num)
    sols = []
    for i in to_test:
        if sum(i) == goal:
            sols = sols + [[1/j for j in i]]
    return sols


if __name__=="__main__":
    max_found_by_hand = 24
    number_of_players = 11
    goal = 2
    sols = test_all_combinations(max_found_by_hand, number_of_players, goal)
    if len(sols) == 0:
        print("No solution found")
    if len(sols) == 1:
        print("Unique solution found: ", sols[0])
    if len(sols) > 1:
        sols.sort(key = lambda x: x[-1])
        print("Multiple solutions found, least worst player solution is: ", sols[0])
