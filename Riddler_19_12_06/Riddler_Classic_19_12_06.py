"""
From Austin Chen comes a riddle of efficiently finding a song:

You have a playlist with exactly 100 tracks (i.e., songs), numbered 1 to 100. To go to another track, there are two
buttons you can press: (1) “Next,” which will take you to the next track in the list or back to song 1 if you are
currently on track 100, and (2) “Random,” which will take you to a track chosen uniformly from among the 100 tracks.
Pressing “Random” can restart the track you’re already listening to — this will happen 1 percent of the time you
press the “Random” button.

For example, if you started on track 73, and you pressed the buttons in the sequence “Random, Next, Random, Random,
Next, Next, Random, Next,” you might get the following sequence of track numbers: 73, 30, 31, 67, 12, 13, 14, 89,
90. You always know the number of the track you’re currently listening to.

Your goal is to get to your favorite song (on track 42, of course) with as few button presses as possible. What
should your general strategy be? Assuming you start on a random track, what is the average number of button presses
you would need to make to reach your favorite song?

"""

from random import randint

from numpy import mean


def strat(curr, thresh):
    if curr <= thresh:
        return curr - 1
    else:
        return randint(0, 99)


def play_a_round(thresh):
    curr = randint(0, 99)
    count = 1
    while curr > 0:
        curr = strat(curr, thresh)
        count = count + 1
    return count


def collect_stats(num_games, thresh):
    return mean([play_a_round(thresh) for _ in range(num_games)])


def exact_calc(thresh):
    return thresh / 2 + 100 / (thresh + 1)


if __name__ == '__main__':
    rand_selected = [randint(0, 99) for _ in range(10)]
    x = [collect_stats(10000, i) for i in range(100)]
    y = [exact_calc(i) for i in range(100)]
    print("Checking a few examples to establish credible: ")
    for i in rand_selected:
        print("Testing ", i, " percent error:", (x[i] - y[i]) / x[i])
    print("Based on exact calc: ", y[10:20])
