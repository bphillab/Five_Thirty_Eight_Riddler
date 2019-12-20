"""
From Steve Abney comes a particularly prismatic puzzle:

Suppose I have a rectangle whose side lengths are each a whole number, and whose area (in square units) is the same
as its perimeter (in units of length). What are the possible dimensions for this rectangle?

Alas, that’s not the riddle — that’s just the appetizer. The rectangle could be 4 by 4 or 3 by 6. You can check both
of these: 4 · 4 = 16 and 4 + 4 + 4 + 4 = 16, while 3 · 6 = 18 and 3 + 6 + 3 + 6 = 18. These are the only two whole
number dimensions the rectangle could have. (One way to see this is to call the rectangle’s length a and its width b.
You’re looking for whole number solutions to the equation ab = 2a + 2b.)

On to the main course! Instead of rectangles, let’s give rectangular prisms a try. What whole number dimensions can
rectangular prisms have so that their volume (in cubic units) is the same as their surface area (in square units)?

To get you started, Steve notes that 6 by 6 by 6 is one such solution. How many others can you find?
"""

"""
Given the problem we are looking for an a,b,c such that: 1/a + 1/b + 1/c = 1/2
"""

from math import floor, ceil

if __name__ == '__main__':
    d = 5
    tol = 9e-7

    counter = 0
    counted_steps = 0
    max_tol = 0

    for i in range(3, 2 * d + 1):
        for j in range(max([i, floor(1 / (1 / 2 - 1 / i)) + 1]), ceil((d - 1) / (1 / 2 - 1 / i)) + 1):
            if abs(1 / i + 1 / j - 1 / 2) < tol:
                continue
            for k in range(max([j, floor(1 / (1 / 2 - 1 / i - 1 / j)) + 1]),
                           ceil((d - 2) / (1 / 2 - 1 / i - 1 / j)) + 1):
                if abs(1 / i + 1 / j + 1 / k - 1 / 2) < tol:
                    continue
                for l in range(max([k, floor(1 / (1 / 2 - 1 / i - 1 / j - 1 / k)) + 1]),
                               ceil((d - 3) / (1 / 2 - 1 / i - 1 / j - 1 / k)) + 1):
                    if abs(1 / i + 1 / j + 1 / k + 1 / l - 1 / 2) < tol:
                        continue
                    a = 1 / (1 / 2 - 1 / i - 1 / j - 1 / k - 1 / l)

                    if abs(a - round(a)) < tol and a >= l >= k >= j >= i:
                        if max_tol < abs(a - round(a)):
                            max_tol = abs(a - round(a))
                        print(abs(a - round(a)), " ", i, " ", j, " ", " ", k, " ", l, " ", a, )
                        counter = counter + 1
    print("Total found: ", counter)
    print(max_tol)
