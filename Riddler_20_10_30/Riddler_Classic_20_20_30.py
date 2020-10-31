'''
Riddler Classic
From Ricky Jacobson comes a party game that’s just in time for Halloween:

Instead of playing hot potato, you and 60 of your closest friends decide to play a socially distanced game of hot
pumpkin.

Before the game starts, you all sit in a circle and agree on a positive integer N. Once the number has been chosen,
you (the leader of the group) start the game by counting “1” and passing the pumpkin to the person sitting directly
to your left. She then declares “2” and passes the pumpkin one space to her left. This continues with each player
saying the next number in the sequence, wrapping around the circle as many times as necessary, until the group has
collectively counted up to N. At that point, the player who counted “N” is eliminated, and the player directly to his
or her left starts the next round, again proceeding to the same value of N. The game continues until just one player
remains, who is declared the victor.

In the game’s first round, the player 18 spaces to your left is the first to be eliminated. Ricky, the next player in
the sequence, begins the next round. The second round sees the elimination of the player 31 spaces to Ricky’s left.
Zach begins the third round, only to find himself eliminated in a cruel twist of fate. (Woe is Zach.)

What was the smallest value of N the group could have used for this game?

Extra credit: Suppose the players were numbered from 1 to 61, with you as Player No. 1, the player to your left as
Player No. 2 and so on. Which player won the game?

Extra extra credit: What’s the smallest N that would have made you the winner?
'''


def check_m_n(m, n):
    return m % n == 18 and m % (n - 1) == 31 and m % (n - 2) == 0


def ec_round(participants, m, start):
    removed = (start + m) % len(participants)
    participants = participants[:removed] + participants[removed + 1:]
    start = removed
    return participants, start


def ec_q(m, n):
    start = 0
    participants = [i for i in range(1, n + 1)]
    while len(participants) > 1:
        participants, start = ec_round(participants, m, start)
    return participants[0]


if __name__ == '__main__':
    for n in range(33, 34):
        for m in range(9000, 10000):
            if check_m_n(m, n):
                print(m, " ", n)
                break

    for n in range(62, 63):
        for m in range(9000, 1000000):
            if check_m_n(m, n):
                print(m, " ", n)
                break
    print(ec_q(m, n))
