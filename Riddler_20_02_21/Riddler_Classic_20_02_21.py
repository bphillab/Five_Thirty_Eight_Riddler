"""
From Abijith Krishnan comes a game of coin flipping madness:

You have two fair coins, labeled A and B. When you flip coin A, you get 1 point if it comes up heads, but you lose 1
point if it comes up tails. Coin B is worth twice as much — when you flip coin B, you get 2 points if it comes up
heads, but you lose 2 points if it comes up tails.

To play the game, you make a total of 100 flips. For each flip, you can choose either coin, and you know the outcomes
of all the previous flips. In order to win, you must finish with a positive total score. In your eyes, finishing with
2 points is just as good as finishing with 200 points — any positive score is a win. (By the same token,
finishing with 0 or −2 points is just as bad as finishing with −200 points.)

If you optimize your strategy, what percentage of games will you win? (Remember, one game consists of 100 coin flips.)

Extra credit: What if coin A isn’t fair (but coin B is still fair)? That is, if coin A comes up heads with
probability p and you optimize your strategy, what percentage of games will you win?


"""
from functools import lru_cache


@lru_cache(maxsize=40000)
def opt_strat(current_score, coins_remaining, p1=0.5, p2=0.5):
    if -1 * current_score >= 2 * coins_remaining:
        return 0
    if current_score > coins_remaining:
        return 1
    return max([p1 * opt_strat(current_score + 1, coins_remaining - 1, p1, p2) +
                (1 - p1) * opt_strat(current_score - 1, coins_remaining - 1, p1, p2),
                p2 * opt_strat(current_score + 2, coins_remaining - 1, p1, p2) +
                (1 - p2) * opt_strat(current_score - 2, coins_remaining - 1, p1, p2)])


if __name__ == "__main__":
    print(opt_strat(0, 100))
