"""
From Dave Moran comes a question about baseball’s unusual 2019 World Series:

In the World Series, one team hosts Games 1, 2, 6 and 7, while the other team hosts Games 3, 4 and 5. When the
Nationals beat the Astros last month, it marked the first time in World Series history that the home team lost all
seven games. On average, the home team actually wins about 54 percent of the time in baseball. Running the numbers,
you’ll quickly see that seven home losses is a once-in-a-lifetime event.

But putting seven aside for a moment, what’s the probability that the home team will lose at least six consecutive
games?

Extra credit: What’s the probability the home team will lose at least five consecutive games? Four consecutive games?
"""

"""
This problem can be solved analytically for 6 games fairly quickly:
<Insert binomial maths here>
Extra credit gets a bit more difficult because the number of consecutive losses may not always be realized if the 
tournament stops at one team winning 4. I will thus code up the possible outcomes below.
"""
