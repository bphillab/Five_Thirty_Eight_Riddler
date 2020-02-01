"""
At the recent World Indoor Bowls Championships in Great Yarmouth, England, one of the rolls by Nick Brett went viral.
Here it is in all its glory:


In order for Nick’s green bowl to split the two red bowls, he needed expert precision in both the speed of the roll
and its final angle of approach.

Suppose you were standing in Nick’s shoes, and you wanted to split two of your opponent’s bowls. Let’s simplify the
math a little, and say that each bowl is a sphere with a radius of 1. Let’s further suppose that your opponent’s two
red bowls are separated by a distance of 3 — that is, the centers of the red bowls are separated by a distance of 5.
Define ɸ as the angle between the path your bowl is on and the line connecting your opponent’s bowls.

For example, here’s how you could split your opponent’s bowls when ɸ is 75 degrees:

Two red circles of radius 1 are vertically aligned, and their centers are separated by distance 5. A green circle
passes through them, making a 75 degree angle with the line connecting the centers of the red circles.
What is the minimum value of ɸ that will allow your bowl to split your opponents’ bowls without hitting them?
"""

"""
Ans: Seems like simple trig. At closest approach you get a right triangle where the length of the side opposite to 
phi is 2, the hypotenuse is 2.5 just gotta take that arcsine
"""
