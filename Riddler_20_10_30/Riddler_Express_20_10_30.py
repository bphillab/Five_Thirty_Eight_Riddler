'''
Riddler Express
While waiting in line to vote early last week, I overheard a discussion between election officials. Apparently,
there may have been a political sign that was within 100 feet of the polling place, against New York State law.

This got me thinking. Suppose a polling site is a square building whose sides are 100 feet in length. An election
official takes a string that is also 100 feet long and ties one end to a door located in the middle of one of the
building’s sides. She then holds the other end of the string in her hand.

What’s the area of the region outside of the building she can reach while holding the string?

'''

'''
Answer:
Include/Exclude Approach:
Include 4 circles centered at (50,0)(0,50)(0,-50)(-50,0):4 pi (100)^2
Exclude the overlap of those circles to get area covered: 4[2 100^2 (pi/4-1/2)] = 4 pi 100^2/2 -4 100^2
Exclude the building itself: 100^2
4 pi 100^2 - 4 pi 100^2/2+4 100^2 - 100^2=4 pi 100^2/2 + 3 100^2
'''
