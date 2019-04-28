# %%
from numpy import random
from random import shuffle


# %%
def player_sees(id, scen):
    return str(scen[:id] + [0] + scen[id + 1:])


def test_scen(scen, resp):
    num_wins = 0
    for i in range(len(scen)):
        if resp[player_sees(i, scen)] == scen[i]:
            num_wins = num_wins + 1
    return num_wins


def which_match(scen, resp):
    matchers = []
    for i in range(len(scen)):
        if resp[player_sees(i, scen)] == scen[i]:
            matchers = matchers + [player_sees(i, scen)]
    return matchers


def generate_all_scen():
    scens = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    scens += [[i + 1, j + 1, k + 1, l + 1]]
    return scens


def generate_all_resp():
    resps = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    resps += [str(([j + 1, k + 1, l + 1, 0][:i] + [0] + [j + 1, k + 1, l + 1, 0][i:])[:-1])]
    return resps


def fill_in_remaining(resp):
    responses = {}
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    temp = ([j + 1, k + 1, l + 1, 0][:i] + [0] + [j + 1, k + 1, l + 1, 0][i:])[:-1]
                    responses[str(temp)] = random.choice([1, 2, 3, 4])
    for key in resp.keys():
        responses[key] = resp[key]
    return responses


def determine_handled_cases(resp, num_match_needed):
    all_scens = generate_all_scen()
    handled_cases = []
    remaining_cases = []
    dup_cases = []
    for scen in all_scens:
        try:
            l = test_scen(scen, resp)
            if l >= num_match_needed:
                handled_cases += [scen]
            if l > num_match_needed:
                dup_cases += [scen]
            if l < num_match_needed:
                remaining_cases += [scen]
        except:
            remaining_cases += [scen]
    return handled_cases, remaining_cases, dup_cases


def extract_dupes(duped, resps, num_match_needed):
    resp_to_remove = []
    for i in duped:
        counter = 0
        matchers = which_match(i, resps)
        shuffle(matchers)
        for j in matchers:
            counter = counter + 1
            if counter <= num_match_needed:
                continue
            resp_to_remove = resp_to_remove + [j]
    return resp_to_remove


if __name__ == '__main__':
    defined = {}
    resps = fill_in_remaining(defined)
    num_match_needed = 1
    handled, remaining, duped = determine_handled_cases(resps, num_match_needed)


    steps = 0
    while len(remaining) > 0:
        if steps % 100 == 0:
            print("On step: ", steps, ", ", len(remaining), " remaining")
        dupes = extract_dupes(duped, resps, num_match_needed)
        for i in dupes:
            resps.pop(i)
        resps = fill_in_remaining(resps)
        handled, remaining, duped = determine_handled_cases(resps, num_match_needed)
        steps = steps + 1

    print("Completed in ", steps, " steps")
    if len(dupes) == 0:
        print('Not possible to solve as far as I can tell')
    else:
        print(resps)
    # going for 2, probably one of those heat death of the universe things...
    defined = {}
    resps = fill_in_remaining(defined)
    num_match_needed = 2
    handled, remaining, duped = determine_handled_cases(resps, num_match_needed)


    steps = 0
    while len(remaining) > 0 and len(dupes)>0:
        if steps % 100 == 0:
            print("On step: ", steps, ", ", len(remaining), " remaining")
        dupes = extract_dupes(duped, resps, num_match_needed)
        for i in dupes:
            resps.pop(i)
        resps = fill_in_remaining(resps)
        handled, remaining, duped = determine_handled_cases(resps, num_match_needed)
        steps = steps + 1
    print("Completed in ", steps, " steps")
    if len(dupes) == 0:
        print('Not possible to solve as far as I can tell')
    else:
        print(resps)
