"""
Riddler Classic
From Mark Bradwin comes a fishy puzzle about state names:

Ohio is the only state whose name doesn’t share any letters with the word “mackerel.” It’s strange, but it’s true.

But that isn’t the only pairing of a state and a word you can say that about — it’s not even the only fish! Kentucky
has “goldfish” to itself, Montana has “jellyfish” and Delaware has “monkfish,” just to name a few.

What is the longest “mackerel?” That is, what is the longest word that doesn’t share any letters with exactly one
state? (If multiple “mackerels” are tied for being the longest, can you find them all?)

Extra credit: Which state has the most “mackerels?” That is, which state has the most words for which it is the only
state without any letters in common with those words?

(For both the Riddler and the extra credit, please refer to Friend of the Riddler™ Peter Norvig’s word list.)

"""

import numpy as np


def convert_to_letters(word):
    return np.unique(list(word.lower()))


def import_words(file_loc):
    word_list = {}
    f = open(file_loc, "r")
    for word in f:
        word_list[word[:-1]] = convert_to_letters(word[:-1])
    return word_list


def is_there_overlap(word1, word2):
    return len(np.intersect1d(word1, word2)) > 0


def find_mackerels(words, states):
    words_overlap = {}
    mackerels = []
    state_mack = []
    for i in words:
        words_overlap[i] = [state for state in states if is_there_overlap(words[i], states[state])]
        if len(words_overlap[i]) == 49:
            mackerels += [i]
            state_mack = np.append(state_mack, np.setdiff1d(list(states.keys()), words_overlap[i]))
    return mackerels, state_mack


def detect_longest_mackerel(mackerels):
    longest_mackerels = []
    longest_length = 0
    for i in mackerels:
        if len(i) == longest_length:
            longest_mackerels = longest_mackerels + [i]
        if len(i) > longest_length:
            longest_length = len(i)
            longest_mackerels = [i]
    return longest_mackerels


def detect_state_with_most(state_macks):
    state_tallies = np.unique(state_macks, return_counts=True)
    largest_states = []
    len_largest_state = 0
    for i in range(len(state_tallies[1])):
        if state_tallies[1][i] == len_largest_state:
            largest_states = largest_states + [state_tallies[0][i]]
        if state_tallies[1][i] > len_largest_state:
            largest_states = [state_tallies[0][i]]
            len_largest_state = state_tallies[1][i]
    return largest_states, len_largest_state


def main():
    base_dir = './'

    print('Loading words: ')
    words = import_words(base_dir + 'word_list.txt')

    print('Loading states: ')
    states = import_words(base_dir + 'state_list.txt')

    print('Detecting mackerels: ')
    mackerels, state_macks = find_mackerels(words, states)

    print('Detecting longest mackerel: ')
    longest_mackerels = detect_longest_mackerel(mackerels)

    print('Detecting state with most mackerels: ')
    most_mack, num = detect_state_with_most(state_macks)

    print('Longest Mackerels: ')
    for i in longest_mackerels:
        print(i)

    print('States with most Mackerels: ')
    for i in most_mack:
        print(i)

    print('Length of longest Mackerel: ', len(longest_mackerels[0]))
    print('Most Mackerels in a state: ', num)
    return


if __name__ == '__main__':
    main()
