"""
Riddler Classic
Just in time for the Fourth of July, this week’s Classic is about stars on the American flag:

The 50 stars on the American flag are arranged in such a way that they form two rectangles. The larger rectangle is 5
stars wide, 6 stars long; the smaller rectangle is embedded inside the larger and is 4 stars wide, 5 stars long. This
square-like pattern of stars is possible because the number of states (50) is twice a square number (25).

Stars on the US flag, arranged to form two overlapping rectangles
Now that the House of Representatives has passed legislation that would make the District of Columbia the fifty-first
US state — and renamed Washington, Douglass Commonwealth, in honor of Frederick Douglass — a natural question is how
to aesthetically arrange 51 stars on the flag.

One pleasing design has a star in the middle, surrounded by concentric pentagons of increasing side length,
as shown below. The innermost pentagon has five stars, and subsequent pentagons are made up of 10, 15 and 20 stars.
All told, that’s 51 stars.


It just so happens that when N equals 50, N is twice a square and N+1 is a centered pentagonal number. After 50,
what is the next integer N with these properties?
"""
import numpy as np


def centered_pentagonal_number_generator(n):
    return n * (3 * n - 1) / 2


def centered_pentagonal_number_checker(m):
    x = (1 + np.sqrt(1 + 24 * m)) / 6
    return x == np.floor(x)


def proximate_square_checker(l):
    return centered_pentagonal_number_checker(2 * l ** 2 + 1)


def find_vals(min, max):
    return [i for i in range(min, max + 1) if proximate_square_checker(i)]


def main(min_val=5, max_val=100):
    vals = find_vals(min_val, max_val)
    print([2 * i ** 2 for i in vals])
    return 0


if __name__ == '__main__':
    main()
