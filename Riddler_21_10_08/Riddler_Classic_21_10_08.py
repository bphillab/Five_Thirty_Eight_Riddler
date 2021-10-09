from math import sqrt, sin, pi


def dthetadt(theta, v, h):
    return v / h * sin(theta) ** 2


def dRdt(R, theta, v, h):
    return sqrt(4 * v ** 2 - R ** 2 * dthetadt(theta, v, h) ** 2)


def drdt(r, theta, v, h):
    return sqrt(max(v ** 2 - r ** 2 * dthetadt(theta, v, h) ** 2, 0))


h = 100
dt = 0.01
v = 1

theta = pi / 4
R = h / sin(theta)
t = 0

while theta < 3 * pi / 4:
    t = t + dt
    theta = theta + dthetadt(theta, v, h) * dt
    R = R + dRdt(R, theta, v, h) * dt
    if theta < pi / 2 and R > 2 * h:
        R = 2 * h
