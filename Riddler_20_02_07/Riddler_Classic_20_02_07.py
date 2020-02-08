"""
Also on Super Bowl Sunday, math professor Jim Propp made a rather interesting observation:


At first glance, this might look like one of those annoying memes about order of operations that goes viral every few
years — but it’s not.

When you write lengthy mathematical expressions using parentheses, it’s always clear which “open” parenthesis
corresponds to which “close” parenthesis. For example, in the expression (1+2(3−4)+5), the closing parenthesis after
the 4 pairs with the opening parenthesis before the 3, and not with the opening parenthesis before the 1.

But pairings of other mathematical symbols can be more ambiguous. Take the absolute value symbols in Jim’s example,
which are vertical bars, regardless of whether they mark the opening or closing of the absolute value. As Jim points
out, |−1|−2|−3| has two possible interpretations:

The two left bars are a pair and the two right bars are a pair. In this case, we have 1−2·3 = 1−6 = −5.
The two outer bars are a pair and the two inner bars are a pair. In this case, we have |−1·2−3| = |−2−3| = |−5| = 5.
Of course, if we gave each pair of bars a different height (as is done in mathematical typesetting), this wouldn’t be
an issue. But for the purposes of this problem, assume the bars are indistinguishable.

How many different values can the expression |−1|−2|−3|−4|−5|−6|−7|−8|−9| have?

"""
import numpy as np


def create_exec_str(arr, prev_str='', depth=0):
    if not arr:
        return [prev_str[1:] + ')']
    if depth == 0:
        return create_exec_str(arr[1:], prev_str + '*abs(-' + str(arr[0]), depth + 1)
    if depth > len(arr):
        return create_exec_str(arr[1:], prev_str + ') -' + str(arr[0]), depth - 1)
    return create_exec_str(arr[1:], prev_str + '*abs(-' + str(arr[0]), depth + 1) + \
           create_exec_str(arr[1:], prev_str + ') -' + str(arr[0]), depth - 1)


def unique_values(num_val):
    to_eval = create_exec_str(list(range(1, num_val + 1)))
    return np.unique([eval(i) for i in to_eval]).size


if __name__ == '__main__':
    print("Number of unique for each number of integers: ")
    tracker = []
    for i in range(1, 39, 2):
        temp = unique_values(i)
        tracker = tracker + [temp]
        print(i, ": ", temp)
