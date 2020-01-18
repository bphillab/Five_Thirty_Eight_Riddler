"""
Riddler Express
The Riddler Football League (RFL) playoffs are upon us! As the coach, you’ve devised a new strategy for scoring after
a touchdown. Your team will line up 2 yards away from the goal line in such a way that it could attempt either a
1-point conversion or a 2-point conversion. (Unlike other football leagues, the distance is the same for both types
of conversion, and you need not announce which you’ll be attempting.) Your opponent can only properly defend against
one of those two possibilities, so they’ll have to guess.

If you attempt a 1-point conversion and the other team defends against it properly, you’ll score 90 percent of the
time. If they don’t defend it properly, you’ll score 100 percent of the time.

If you instead attempt a 2-point conversion and the other team defends against it properly, you’ll score 40 percent
of the time. If they don’t defend it properly, you’ll score 60 percent of the time.

To tell your team which they should attempt, your team’s offensive coordinator will communicate to your team’s
captain the probability with which they should attempt each. For example, the coordinator might say: “Go for 1 with a
51 percent chance, and go for 2 with a 49 percent chance.” Using a random number generator, the captain will then
ultimately decide to go for 1 point or 2 points. (Naturally, every athlete in the RFL has a random number generator
handy.)

However, given all the spying that occurs in the RFL these days, you can assume that the offensive coordinator’s
message will also be heard by your opponent — that means the defense knows the exact probability with which you’ll
attempt either conversion. Your opponent also knows the probability of you scoring in each of the four scenarios
listed above.

With all that said, what strategy will maximize the average number of points you’ll score (i.e., how often should
your team go for 1 or 2)? What should your opponent’s defensive strategy be? How many points will you score,
on average, after each touchdown?
"""

"""
Let's look at the number of expected number of points scored and apply a min-max idea to it:
Let P_O be the probability of the offense selecting strategy 1
Let P_D be the probability of the defense selecting strategy 1
Then:
E = P_O P_D (0.9) + P_O(1-P_D)(1) + 2 (1-P_O)P_D(0.6) + 2(1-P_O)(1-P_D)(0.4)
  = 0.8 + (1-0.8)P_O + (1.2-0.8)P_D + (0.9-1-1.2+0.8)P_O P_D
  = 0.8 + 0.2 P_O + (0.4 - 0.5 P_O)P_D
This is minimized when for a given P_O as follows:
If P_O < 4/5 then P_D = 0
If P_O > 4/5 then P_D = 1
If P_O = 4/5 then P_D is irrelevant

Given these minima:

If P_O < 4/5 then E is maximized for larger P_O
If P_O > 4/5 then E is maximized for smaller P_O
P_O is thus optimal at 4/5 giving an E of 0.96
"""
