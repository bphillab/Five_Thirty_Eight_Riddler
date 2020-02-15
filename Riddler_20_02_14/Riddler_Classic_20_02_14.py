"""
From David Lewis comes an additional, original twist on Riddler City’s urban planning:

The mayor ultimately decided not to pursue diagonal sidewalks, but the petitioners haven’t given up yet. One of them
recently visited Barcelona and was inspired by its octagonal city blocks.

Now, there’s a second petition on the mayor’s desk, asking that the grid layout of the city’s sidewalks be replaced
with an octagonal pattern, represented by the thicker blue lines in the diagram below:

Riddler City octagonal sidewalks
Under this second proposal, now what fraction of the employees would have a shorter walk home if the city replaced
its traditional sidewalks with these new sidewalks?
"""

"""
Ans: 1/2

2Y(1-2l+sqrt(2)l) + (X-Y-1) (1-2l+2sqrt(2)l) = X+Y
Solving:
Y/X = sqrt(2)-1 +O(l/x) ~ sqrt(2)-1
"""
