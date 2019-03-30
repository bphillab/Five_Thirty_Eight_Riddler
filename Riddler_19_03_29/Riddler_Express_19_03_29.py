"""
   From Tom Hanrahan, a probability puzzle; or, a mini-lesson in
   surprising results:
   You are playing your first ever game of “Ticket to Ride,” a board
   game in which players compete to lay down railroad while getting so
   competitive they risk ruining their marriages. At the start of the
   game, you are randomly dealt a set of three Destination Tickets out
   of a deck of 30 different tickets. Each reveals the two terminals
   you must connect with a railroad to receive points. During the game,
   you eventually pick up another set of three Destination Tickets, so
   you have now seen six of the 30 tickets in the game.

   Later, because you enjoyed it so much, you and your friends play a
   second game. The ticket cards are all returned and  reshuffled.
   Again, you are dealt a set of three tickets to begin play. Which is
   more likely: that you had seen at  least one of these three tickets
   before, or that they were all new to you?
"""

import scipy.special

print("Probability of the cards all being new: ", scipy.special.binom(24, 3) / scipy.special.binom(30, 3))
