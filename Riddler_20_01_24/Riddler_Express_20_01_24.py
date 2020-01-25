"""
Riddler Express

From Stephanie Thompson comes a question of ballot optimization:

Derek Jeter and Larry Walker were just elected to the Baseball Hall of Fame! That got Stephanie thinking. Suppose
there are 20 players on the ballot and 400 voters in a given year. Each voter can select up to 10 players for
induction without voting for any given player more than once. To gain entry, a player must have been selected on at
least 75 percent of the ballots.

Under these circumstances, what is the maximum number of players that can be inducted into the Hall of Fame?
"""

"""
Number of votes = 400*10 = 4000
Number of votes for a player to be inducted = 300
Number of votes/Number of votes for a player to be inducted = Max number of inductable players = 13 + 1/3
No matter what there will be 100 "wasted" votes (either for non-viable candidates or candidates that don't need more)
Question then becomes can we make a scheme to vote for 13?
Blocks of 100:
1-100: vote for 1-10
101-200: vote for 4-13
201-300: vote for 1-3 and 7-13
301-400: vote for 1-6 and 10-13
10 gets the extra hundred votes in this scenario
"""
