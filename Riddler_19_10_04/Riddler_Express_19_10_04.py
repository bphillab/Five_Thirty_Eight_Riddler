"""
From Thomas Sneller comes a puzzle that brings us back to the game show to end all game shows, “Who Wants to Be a
Riddler Millionaire?” As you’ll remember, for each question you must pick the correct option from four choices.

You’ve made it to the $1 million question, but it’s a tough one. Out of the four choices, A, B, C and D, you’re 70
percent sure the answer is B, and none of the remaining choices looks more plausible than another. You decide to use
your final lifeline, the 50:50, which leaves you with two possible answers, one of them correct. Lo and behold, B
remains an option! How confident are you now that B is the correct answer?
"""

"""
Approach 1: Bayes Theorem:
P(B|50-50 Choices) = P(50-50 Choices|B)P(B)/P(50-50 choices)

P(B) = 0.7
P(50-50 Choices|B) = 1 [If B is correct then it kinda has to be there]
P(50-50 Choices) = P(50-50 Choices|B)P(B) + P(50-50 Choices| Not B) P(Not B)
                 = .7 + .3 * (1/3) = .8
P(B|50-50 Choices) = 1 * .7/.8 = 7/8
"""
