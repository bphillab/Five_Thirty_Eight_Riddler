from scipy.special import binom
import itertools
import pandas as pd


def calc_num_states(row):
    """
    Given a row which tells you which cards are in the tableau figure out how many combinations exist
    when you include the stock. The separation between tableau and stock is necessary because there
    are different requirements for each to be unplayable. (looser on the stock)
    :param row: a row from a database that contains indicators for presence of various card/colors
    :return: number of states that can exist
    """
    # Start by looking at possible cards that can be played upon (test_titles) and the cards that
    # would be played (paired titles)
    test_titles = [str(i[1]) + i[0] for i in itertools.product(['R', 'B'], [i for i in range(3, 14)])]
    paired_titles = [str(i[1]) + i[0] for i in itertools.product(['B', 'R'], [i for i in range(2, 13)])]

    # Based on the above, checkout out which restrictions apply (which cards can not be
    #  in the stock due to being playable in the tableau).
    # Also for what is possible, what cards are already played in the tableau.
    options_row = [1-i for i in row[test_titles].values]
    already_chosen = row[paired_titles].values

    # Count how many cards are able to be played and already taken by the tableau. Adding in Kings which were missed to
    # make lengths match above.
    opt_not_alr = int(sum([options_row[i] * (1-already_chosen[i]) for i in range(len(test_titles))]) + 1-row['13R']+1-row['13B'])

    # Finally the calculation: For the tableau you have some number of cards num/color. Fill up the first
    # possible suit of those, then begin filling the second suit. This leaves: n choose 7-n where n is
    # the number of number/color combinations. Also there should be 2*n-7 openings which corresponds to
    # a degeneracy (either suit) so multiply by 2^(2*n-7)
    #
    # For the stock calculation we have whatever's left: 2*(playable)+(what's left from tableau) choose 8
    #

    return binom(row.num_spots, 7-row.num_spots)*binom(2*opt_not_alr+row.num_color_flips, 8)* (2 ** row.num_color_flips)


def direct_calc():
    """
    direct_calc: Function that calculates directly the number of
                 possible states where a solitaire game is not playable

    :rtype: Integer
    """
    # Create all possible states
    base = pd.DataFrame({'key': [1, 1], 'ind': [0, 1]})
    total = base
    for i in range(23):
        total = pd.merge(total, base, on='key')

    total = total.drop(columns='key')
    titles = [str(i[1]) + i[0] for i in itertools.product(['R', 'B'], [i for i in range(2, 14)])]
    total.columns = titles

    # Calculate the number of types (number/color) of cards present
    total['num_spots'] = total.sum(axis=1)

    # Can't have more than 7 spots since that's the number of cards
    total = total[total.num_spots <= 7]

    # Needs to provide at least 7 spots since that's the number of cards
    total = total[2 * total.num_spots >= 7]

    # Checking to make sure that there isn't anything playable: (X R, X+1 B)
    # or (X B, X+1 R)
    total = total[total['2B'] * total['3R'] == 0]
    total = total[total['2R'] * total['3B'] == 0]

    total = total[total['3B'] * total['4R'] == 0]
    total = total[total['3R'] * total['4B'] == 0]

    total = total[total['4B'] * total['5R'] == 0]
    total = total[total['4R'] * total['5B'] == 0]

    total = total[total['5B'] * total['6R'] == 0]
    total = total[total['5R'] * total['6B'] == 0]

    total = total[total['6B'] * total['7R'] == 0]
    total = total[total['6R'] * total['7B'] == 0]

    total = total[total['7B'] * total['8R'] == 0]
    total = total[total['7R'] * total['8B'] == 0]

    total = total[total['8B'] * total['9R'] == 0]
    total = total[total['8R'] * total['9B'] == 0]

    total = total[total['9B'] * total['10R'] == 0]
    total = total[total['9R'] * total['10B'] == 0]

    total = total[total['10B'] * total['11R'] == 0]
    total = total[total['10R'] * total['11B'] == 0]

    total = total[total['11B'] * total['12R'] == 0]
    total = total[total['11R'] * total['12B'] == 0]

    total = total[total['12B'] * total['13R'] == 0]
    total = total[total['12R'] * total['13B'] == 0]

    # Number of suit/color flips
    total['num_color_flips'] = total['num_spots'] * 2 - 7

    # Calculate the number of states
    total['num_states'] = total.apply(lambda x: calc_num_states(x), axis=1)

    # return sum over all states
    return total['num_states'].sum()


if __name__ == '__main__':
    x = direct_calc()
    print("Number of states that are unplayable: ")
    print(x)
    print("Number of states: ")
    print(binom(52, 8)*binom(44, 7))
    print("Percent of unplayable games")
    print(x/(binom(52, 8)*binom(44, 7)))
