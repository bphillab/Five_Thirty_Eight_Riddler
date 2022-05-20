import random
from math import floor

num_sessions = 10000
top_floor = 10
i = top_floor
acc = []

for j in range(num_sessions):
    i = top_floor
    cnt = 0
    while not i == 0:
        if i > 0:
            i = floor(random.uniform(-1, i))
        elif i < 0:
            i = floor(random.uniform(0, top_floor + 1))
        cnt = cnt + 1
    acc = acc + [cnt]
