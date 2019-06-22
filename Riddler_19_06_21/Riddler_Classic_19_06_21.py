"""
Problem Statement:
From Michael Sarkis, a puzzle that his friend was asked to answer during an interview at an investment bank:

There is a square table with a quarter on each corner. The table is behind a curtain and thus out of your view. Your
goal is to get all of the quarters to be heads up — if at any time all of the quarters are heads up, you will
immediately be told and win.

The only way you can affect the quarters is to tell the person behind the curtain to flip over as many quarters as you
would like and in the corners you specify. (For example, “Flip over the top left quarter and bottom right quarter,” or,
“Flip over all of the quarters.”) Flipping over a quarter will always change it from heads to tails or tails to heads.
However, after each command, the table is spun randomly to a new orientation (that you don’t know), and you must give
another instruction before it is spun again.

Can you find a series of steps that guarantees you will have all of the quarters heads up in a finite number of moves?

Answer:

This one also doesn't require coding:
There are four relevant states:
1) All coins match
2) One coin is different
3) Two coins are different and next to each other
4) Two coins are different and are opposite of each other

If (1) then either we are done as all are heads or we need to flip all of the coins

If (4) then flipping the coins doesn't change us from (4) and flipping coins on the diagonal takes us to (1)

If (3) then flipping all coins takes us back to (3) and flipping diagonal coins takes us to (3) flipping either a
vertical or horizontal pair of coins will take us to (1), where we are done, or (4), where flipping the diagonal takes
us to (1)

If (2) then flipping a random coin will take us to (1), (3), or (4) which we can solve without interfering. (see above)

We thus have an invariant way of solving this!

"""