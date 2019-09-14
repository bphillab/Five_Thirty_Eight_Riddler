'''
Recent Riddlers have tackled Scrabble Superstrings and road trips through 48 states. For this week’s Riddler Classic,
Max Maguire combines these two puzzles into one:

The challenge is to find the longest string of letters in which (1) every pair of consecutive letters is a two-letter
state or territory abbreviation, and (2) no state abbreviation occurs more than once. For example, Guam, Utah and Texas
can be combined into the valid four-letter string GUTX. Another valid string is ALAK (Alabama, Louisiana and Alaska),
while ALAL (Alabama, Louisiana and Alabama) is invalid because it includes the same state, Alabama, twice.

For reference, the full list of abbreviations is available here, courtesy of the United States Postal Service.


'''


def load_abbreviations():
    abbreviations = []
    f = open('./abbreviations.txt')
    for i in f:
        abbreviations = abbreviations + [i[0]+i[-2]]
    return abbreviations


def determine_followers(origin, words):
    followers = []
    for word in words:
        if origin[1] == word[0] and word != origin:
            followers = followers + [word]
    return followers


def create_follower_graph(words):
    follower_dict = {}
    for word in words:
        follower_dict[word] = determine_followers(word, words)
    return follower_dict


def trickle_down_max(path,  follow_graph):
    next_step = [i for i in follow_graph[path[-1]] if i not in path]
    if len(next_step) == 0:
        return path
    candidate_results = [trickle_down_max(path+[i], follow_graph) for i in next_step]
    candidate_results.sort(key=lambda x: len(x))
    return candidate_results[-1]


def convert_winner_to_string(winner):
    return ''.join([winner[0]]+[i[1] for i in winner[1:]])


if __name__ == '__main__':
    abbs = load_abbreviations()
    followers = create_follower_graph(abbs)
    possible_ends = [trickle_down_max([i],followers) for i in abbs]
    possible_ends.sort(key=lambda x:len(x))
    print(possible_ends[-1])
    print(convert_winner_to_string(possible_ends[-1]))
    'FMPWVARIASDCTNCALAKSCOHINMNVIDE'
