"""
From Robert Berger comes a question of maximizing magnetic volume:

Robert’s daughter has a set of Magna-Tiles, which, as their name implies, are tiles with magnets on the edges that
can be used to build various polygons and polyhedra. Some of the tiles are identical isosceles triangles with one 30
degree angle and two 75 degree angles. If you were to arrange 12 of these tiles with their 30 degree angles in the
center, they would lay flat and form a regular dodecagon. If you were to put fewer (between three and 11) of those
tiles together in a similar way, they would form a pyramid whose base is a regular polygon. Robert has graciously
provided a photo of the resulting pyramids when three and 11 tiles are used:

3 magnatiles arranged into a tall pyramid, and 11 magnatiles arranged into a short pyramid.
If Robert wanted to maximize the volume contained within the resulting pyramid (presumably to store as much candy for
his daughter as possible), how many tiles should he use?

"""

""" 
Ans: Again seems a bit straightforward. We know that area is going to be 1/3 (A_b h). h is determinable from some 
simple trig:
h = sqrt(tan(theta)^2 * a^2/4 - (r_insribed)^2)
r_inscribed = a/(2 tan(pi/n)) for n-sides

A_b is base area for regular polygon: a^2 n /(4 tan(pi/n))

V = (a^3/24)(n/tan(pi/n)^2)(sqrt(tan(pi/n)^2 tan(theta)^2 - 1))
Options: Calculus: Take a derivative set to zero solve... This looks annoying
         There's only 3-11 try each
          
"""
from math import tan, pi, sqrt


def volume(a, n, theta=75 * pi / 180):
    return (a ** 3 / 24) * (n / tan(pi / n) ** 2) * (sqrt(tan(pi / n) ** 2 * tan(theta) ** 2 - 1))


if __name__ == "__main__":
    for i in range(2, 13):
        print(i, " ", volume(1, i))
