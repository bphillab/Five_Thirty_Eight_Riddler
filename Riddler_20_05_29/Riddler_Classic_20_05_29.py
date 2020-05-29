"""
Riddler Classic
From Jim Crimmins comes a puzzle about what would presumably be the largest Zoom meeting of all time:

One Friday morning, suppose everyone in the U.S. (about 330 million people) joins a single Zoom meeting between 8
a.m. and 9 a.m. — to discuss the latest Riddler column, of course. This being a virtual meeting, many people will
join late and leave early.

In fact, the attendees all follow the same steps in determining when to join and leave the meeting. Each person
independently picks two random times between 8 a.m. and 9 a.m. — not rounded to the nearest minute, mind you,
but any time within that range. They then join the meeting at the earlier time and leave the meeting at the later time.

What is the probability that at least one attendee is on the call with everyone else (i.e., the attendee’s time on
the call overlaps with every other person’s time on the call)?

Extra credit: What is the probability that at least two attendees are on the call with everyone else?
"""
import matplotlib.pyplot as plt
import numpy as np


def sim_n_people(n):
    return np.sort(np.random.uniform(0, 1, (n, 2)))


def determine_num_winner(ppl):
    last_to_enter = np.max([i[0] for i in ppl])
    first_to_leave = np.min([i[1] for i in ppl])
    return len([i for i in ppl if i[0] < first_to_leave and i[1] > last_to_enter])


def main(n=10000, n_sc=1000, step=1000):
    print("For n = ", n, ": the probability of one person being on with everyone is: ",
          np.mean([determine_num_winner(sim_n_people(n)) > 0 for _ in range(n_sc)]))
    print("For n = ", n, ": the probability of two people being on with everyone is: ",
          np.mean([determine_num_winner(sim_n_people(n)) > 1 for _ in range(n_sc)]))
    x = [np.mean([determine_num_winner(sim_n_people(j)) > 0 for _ in range(n_sc)]) for j in range(10, n, step)]
    plt.plot(x)
    plt.show()
    x = [np.mean([determine_num_winner(sim_n_people(j)) > 1 for _ in range(n_sc)]) for j in range(10, n, step)]
    plt.plot(x)
    plt.show()


if __name__ == "__main__":
    main()
