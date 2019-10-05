"""
Riddler League Baseball, also known as the RLB, consists of three teams: the Mississippi Moonwalkers, the Delaware
Doubloons and the Tennessee Taters.

Each time a batter for the Moonwalkers comes to the plate, they have a 40 percent chance of getting a walk and a 60
percent chance of striking out. Each batter for the Doubloons, meanwhile, hits a double 20 percent percent of the time,
driving in any teammates who are on base, and strikes out the remaining 80 percent of the time. Finally, each batter for
the Taters has a 10 percent chance of hitting a home run and a 90 percent chance of striking out.

During the RLB season, each team plays an equal number of games against each opponent. Games are nine innings long and
can go into extra innings just like in other baseball leagues. Which of the three teams is most likely to have the best
record at the end of the season?

"""
import numpy as np


def num_hits(p):
    """
    Returns number of hits given the probability of a hit
    :param p: probability of a hit
    :return: number of hits
    """
    return np.random.negative_binomial(3, 1 - p, 1)[0]


def moonwalker(n):
    """Simulate n innings as moonwalkers"""
    return [max(num_hits(.4) - 3, 0) for i in range(n)]


def doubloons(n):
    """Simulate n innings as doubloons"""
    return [max(num_hits(.2) - 1, 0) for i in range(n)]


def taters(n):
    """Simulate n innings as taters"""
    return [max(num_hits(.1), 0) for i in range(n)]


def play_a_game(p1, p2):
    """
    Simulate a game between two teams
    :param p1:
    :param p2:
    :return:
    """
    pts1 = p1(9)
    pts2 = p2(9)
    while pts1 == pts2:
        pts1 = p1(1)
        pts2 = p2(1)
    return pts2 > pts1


def season(num_games):
    teams = ['m', 'd', 't']
    tm_plays = [moonwalker, doubloons, taters]
    wins = {'m': 0, 'd': 0, 't': 0}
    for k in range(num_games):
        for i in range(3):
            for j in range(i + 1, 3):
                team_1 = teams[i]
                team_2 = teams[j]
                res = play_a_game(tm_plays[i], tm_plays[j])
                if res:
                    wins[team_2] = wins[team_2] + 1
                if not res:
                    wins[team_1] = wins[team_1] + 1
    return wins


def main(num_trials):
    print('For a small season, 5 games a piece: ')
    trials = [season(5) for i in range(num_trials)]
    print('t wins: ', np.mean([i['t'] > i['m'] and i['t'] > i['d'] for i in trials]))
    print('m wins: ', np.mean([i['m'] > i['t'] and i['m'] > i['d'] for i in trials]))
    print('d wins: ', np.mean([i['d'] > i['m'] and i['d'] > i['t'] for i in trials]))

    print('For a longer season, 25 games a piece: ')
    trials = [season(25) for i in range(num_trials)]
    print('t wins: ', np.mean([i['t'] > i['m'] and i['t'] > i['d'] for i in trials]))
    print('m wins: ', np.mean([i['m'] > i['t'] and i['m'] > i['d'] for i in trials]))
    print('d wins: ', np.mean([i['d'] > i['m'] and i['d'] > i['t'] for i in trials]))

    print('For a really long season, 100 games a piece: ')
    trials = [season(100) for i in range(num_trials)]
    print('t wins: ', np.mean([i['t'] > i['m'] and i['t'] > i['d'] for i in trials]))
    print('m wins: ', np.mean([i['m'] > i['t'] and i['m'] > i['d'] for i in trials]))
    print('d wins: ', np.mean([i['d'] > i['m'] and i['d'] > i['t'] for i in trials]))

if __name__ == "__main__":
    main(10000)
