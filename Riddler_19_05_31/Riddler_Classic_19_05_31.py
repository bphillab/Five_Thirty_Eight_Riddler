"""
From Ben Wiles, a mathematical trip across the pond:

My favorite game show is “Countdown” on Channel 4 in the UK. I particularly enjoy its Numbers Game. Here is the premise:
There are 20 “small” cards, two of each numbered 1 through 10. There are also four “large” cards numbered 25, 50, 75 and
100. The player asks for six cards in total: zero, one, two, three or four “large” numbers, and the rest in “small”
numbers. The hostess selects that chosen number of “large” and “small” at random from the deck. A random-number generator
then selects a three-digit number, and the players have 30 seconds to use addition, subtraction, multiplication and
division to combine the six numbers on their cards into a total as close to the selected three-digit number as they can.


There are four basic rules: You can only use a number as many times as it comes up in the six-number set. You can only
use the mathematical operations given. At no point in your calculations can you end on something that isn’t a counting
number. And you don’t have to use all of the numbers.

For example, say you ask for one large and five smalls, and you get 2, 3, 7, 8, 9 and 75. Your target is 657.
One way to solve this would be to say 7×8×9 = 504, 75×2 = 150, 504+150 = 654 and 654+3 = 657. You could also say
75+7 = 82, 82×8 = 656, 3-2 = 1 and 656+1 = 657.

This riddle is twofold. One: What number of “large” cards is most likely to produce a solvable game and what number of
“large” cards is least likely to be solvable? Two: What three-digit numbers are most or least likely to be solvable?
"""
from math import floor
from itertools import combinations
from random import sample


def generate_outcomes(l):
    """
    Function that generates a list of outcomes for a given list of numbers
    :param l: list of numbers we'd like to see the results of
    :return: set of potential results
    """
    temp = l.copy()
    temp.sort(reverse=True)
    vals = []
    for i in range(len(temp)-1):
        for j in range(i+1,len(temp)):
            vals = vals + [temp[:i]+temp[i+1:j]+temp[j+1:]+[temp[i]+temp[j]]]\
                        + [temp[:i] + temp[i + 1:j] + temp[j + 1:] + [temp[i] * temp[j]]]\
                        + [temp[:i] + temp[i + 1:j] + temp[j + 1:] + [temp[i] - temp[j]]]\
                        + [temp[:i] + temp[i + 1:j] + temp[j + 1:] + [int(temp[i] / max(1,temp[j]))*(floor(temp[i] / max(temp[j],1)) ==
                                                                                         temp[i] / max(1,temp[j]))]]
    [i.sort(reverse=True) for i in vals]
    return vals


def list_uniq(l):
    return [list(x) for x in set(tuple(x) for x in l)]


def iter_step(l, orig_l):
    added = [i for i in combinations(orig_l, len(l[0]))]
    all_together = list_uniq(l + added)
    return sum([generate_outcomes(i) for i in all_together], [])


def all_possible_results(l):
    orig_l = l.copy()
    temp = [l.copy()]
    for i in range(len(l)-1):
        temp = iter_step(temp, orig_l)
    return set([i[0] for i in temp+[[max(orig_l)]] if i[0] >= 100 and i[0] < 1000])


def get_all_possible_countdowns(num_large, num_cards=6):
    num_small = num_cards - num_large
    larges = [25, 50, 75, 100]
    smalls = [i for i in range(1,11)]*2
    return [list(i+j) for i in combinations(larges, num_large) for j in combinations(smalls, num_small)]


def get_statistics(num_cards=6, sample_size=100):
    num_combos = [0,0,0,0,0]
    cards = [0,0,0,0,0]
    card_counts = {i:0 for i in range(100,1000)}
    for i in range(5):
        print(i)
        possible_combos = get_all_possible_countdowns(i, num_cards)
        for j in sample(possible_combos,sample_size):
            print(i," ",j)
            num_combos[i] = num_combos[i] + 1
            results = all_possible_results(j)
            cards[i] = cards[i] + len(results)
            for k in results:
                card_counts[k] = card_counts[k]+1
    return num_combos, cards, card_counts


if __name__ == "__main__":
    number_of_combos, card_coverage, number_appear = get_statistics()
    total_number_of_combos = sum(number_of_combos)
    card_coverage = [card_coverage[i]/number_of_combos[i] for i in range(5)]
    number_appear = {i:number_appear[i]/total_number_of_combos for i in number_appear}
    max_most_often = 0
    max_store = []
    min_most_often = 9999
    min_store = []
    for i in range(100,1000):
        if number_appear[i] == max_most_often:
            max_most_often = number_appear[i]
            max_store = max_store + [i]

        if number_appear[i] > max_most_often:
            max_most_often = number_appear[i]
            max_store = [i]

        if number_appear[i] == min_most_often:
            min_most_often = number_appear[i]
            min_store = min_store + [i]

        if number_appear[i] < min_most_often:
            min_most_often = number_appear[i]
            min_store = [i]



    print("For Countdown the following is happening: ")
    print("Number of Combos: ", total_number_of_combos)
    print("For 0 large:     ", number_of_combos[0])
    print("For 1 large:     ", number_of_combos[1])
    print("For 2 large:     ", number_of_combos[2])
    print("For 3 large:     ", number_of_combos[3])
    print("For 4 large:     ", number_of_combos[4])
    print("Average coverage: ")
    print("For 0 large: ", card_coverage[0])
    print("For 1 large: ", card_coverage[1])
    print("For 2 large: ", card_coverage[2])
    print("For 3 large: ", card_coverage[3])
    print("For 4 large: ", card_coverage[4])
    print("Most likely to be solvable: ",max_store," occurs as often as ",max_most_often)
    print("Least likely to be solvable: ",min_store," occurs as often as ",min_most_often)