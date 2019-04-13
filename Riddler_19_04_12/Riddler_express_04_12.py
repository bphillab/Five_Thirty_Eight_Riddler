'''
From Keith Wynroe, what time is it? Puzzle time!

You purchase a new clock but are dismayed to realize that both of its hands are identical. At first, it seems it’s going to be impossible to tell the time because you don’t know which hand is for the minutes and which is for the hours.

However, you realize you don’t need to know which is which for every time — for example, when it’s 12:30, the minute hand will be exactly on the 6 and the hour hand will be halfway between the 12 and the 1. It can’t be the other way around because if the hour hand were exactly on 6, the minute hand would have to exactly on 12, which it’s not. So you know what time it is.

How many times during the day will you not be able to tell the time?
'''

'''Ambiguos time occurs when hour/minute hand could be interchanged, this 11 times per hour times 24 hors = 264
Essentially looking for solutions to x-[x]=y/12, y-[y]=x/12. (x,y) = (X+dx,Y+dy)
gives (dx,dy) = (144 X /143+12Y/143,12X/143+144Y/143). Works for all X,Y except X=Y=11. 

One other note is that the time is not ambiguous if X=Y which happens once per hour.
12-1 = 11 times per hour.
'''

