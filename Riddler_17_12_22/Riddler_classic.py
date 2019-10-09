import numpy.random as random


def __initialize_game(num_players, num_dollars):
    return [num_dollars for i in range(num_players)]


def __eliminate_dead_players(players):
    return [i for i in players if i > 0]


def __pass_dollars(players):
    players = __eliminate_dead_players(players)
    for i in range(len(players)):
        players[i] = players[i] - 1
        what_happens = random.choice(range(3))
        if what_happens == 0:
            players[(i-1)%len(players)] += 1
        if what_happens == 1:
            players[(i+1)%len(players)] += 1
    return __eliminate_dead_players(players)


def play_a_game(num_players, num_dollars):
    players = __initialize_game(num_players,num_dollars)
    num_rounds = 0
    while(len(players)>1):
        players = __pass_dollars(players)
        num_rounds+=1
    return num_rounds


def simulate_mult_games(num_games, num_players, num_dollars):
    num_rounds = []
    for i in range(num_games):
        num_rounds = num_rounds + [play_a_game(num_players, num_dollars)]
    return num_rounds


