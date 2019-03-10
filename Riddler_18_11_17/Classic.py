import random
def simulate_a_round(cups):
    num_cups = len(cups)
    temp_cups = cups.copy()
    thrown_balls = 0
    while sum([i==0 for i in temp_cups]) > 0:
        thrown_balls = thrown_balls + 1
        ball = random.choice(range(num_cups))
        cup = random.choice(range(num_cups))
        temp_cups[cup] = 1
        if ball == cup:
            cups[ball] = 1
    return (thrown_balls, cups)

def simulate_multiple_rounds(N):
    cups = [0]*N
    num_rounds = 0
    num_balls = 0
    while sum([i==0 for i in cups]) > 0:
        num_rounds = num_rounds+1
        temp = simulate_a_round(cups)
        num_balls = temp[0]+num_balls
        cups = temp[1]
    return (num_rounds, num_balls)

def simulate_multiple_games(N,n):
    num_rounds = []
    num_balls = []
    for i in range(n):
        temp = simulate_multiple_rounds(N)
        num_rounds = num_rounds+[temp[0]]
        num_balls = num_balls + [temp[1]]
    return (num_rounds, num_balls)