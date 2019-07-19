"""
Riddler Express
From Tyler Barron, where in the square?:

You are given an empty 4-by-4 square and one marker. You can color in the individual squares or leave them untouched.
After you color as many or as few squares as you’d like, I will secretly cut out a 2-by-2 piece of it and then show it
to you without rotating it. You then have to tell me where it was (e.g., “top middle” or “bottom right,” etc.) in the
original 4-by-4 square.

Can you design a square for which you’ll always know where the piece came from?

Yes:
---------
|.| |.|.|
---------
|.| |.|.|
---------
|.|.| | |
---------
|.| |.| |
---------

Translates to one of the following 2x2:
=============================
|| ----- || ----- || ----- ||
|| |.| | || | |.| || |.|.| ||
|| ----- || ----- || ----- ||
|| |.| | || | |.| || |.|.| ||
|| ----- || ----- || ----- ||
=============================
|| ----- || ----- || ----- ||
|| |.| | || | |.| || |.|.| ||
|| ----- || ----- || ----- ||
|| |.|.| || |.| | || | | | ||
|| ----- || ----- || ----- ||
=============================
|| ----- || ----- || ----- ||
|| |.|.| || |.| | || | | | ||
|| ----- || ----- || ----- ||
|| |.| | || | |.| || |.| | ||
|| ----- || ----- || ----- ||
=============================


As a note the max achievable is capped at 16 from a pure binary standpoint. That ceiling could be reduced further if
geometric effects prevent all binary outcomes from being achievable.
"""