"""
From Anna Engelsone comes a riddle about a historic chess battle:

The infamous 1984 World Chess Championship match between the reigning world champion Anatoly Karpov and 21-year-old
Garry Kasparov was supposed to have been played until either player had won six games. Instead, it went on for 48
games: Karpov won five, Kasparov won 3, and the other 40 games each ended in a draw. Alas, the match was
controversially terminated without a winner.

We can deduce from the games Karpov and Kasparov played that, independently of other games, Karpov’s chances of
winning each game were 5/48, Kasparov’s chances were 3/48, and the chances of a draw were 40/48. Had the match been
allowed to continue indefinitely, what would have been Kasparov’s chances of eventually winning the match?
Bonus: What if we use these chances starting from scratch
"""

"""
Solution:

For starting at the 5-3 point Kasparov must win the 3 non-draw games. (3/8)^3
For starting at the 0-0 point Kasparov must win 6 non-draw games before Karpov can get to 6 games. This is best 
described by the sum of a negative-binomial distribution call it nbinom with k wins, r losses
nbinom(r;k,p) = choose(r+k-1,r) p^k (1-p)^r
sum over r=0,1,2,3,4,5 and k=6 and p= 3/8
"""
from scipy.stats import nbinom

if __name__ == '__main__':
    p_kas_win = 3 / 8
    print("Probability starting at 5-3: ", nbinom.pmf(0, 3, 3 / 8))
    print("Probability starting at 0-0: ", sum([nbinom.pmf(i, 6, 3 / 8) for i in range(6)]))
