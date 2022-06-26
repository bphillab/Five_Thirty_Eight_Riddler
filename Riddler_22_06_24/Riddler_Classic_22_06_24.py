from scipy.special import binom


def goatcheck(goats):
    tempgoats = goats
    numgoats = len(goats)
    tempgoats.sort()
    for i in range(numgoats):
        if tempgoats[i] > i:
            return 1
    return 0


def brute_force(nmg):
    cnt = 0
    for a1 in range(nmg):
        for a2 in range(nmg):
            for a3 in range(nmg):
                for a4 in range(nmg):
                    for a5 in range(nmg):
                        for a6 in range(nmg):
                            for a7 in range(nmg):
                                for a8 in range(nmg):
                                    for a9 in range(nmg):
                                        cnt += goatcheck([a1, a2, a3, a4, a5, a6, a7, a8, a9])
    return cnt


def multinomial(params):
    if len(params) == 1:
        return 1
    return binom(sum(params), params[-1]) * multinomial(params[:-1])


def slight_improvement(nmg):
    cnt = 0
    for a1 in range(nmg + 1):
        for a2 in range(nmg + 1):
            if a1 + a2 > nmg:
                continue
            for a3 in range(nmg + 1):
                if a1 + a2 + a3 > nmg:
                    continue
                for a4 in range(nmg + 1):
                    if a1 + a2 + a3 + a4 > nmg:
                        continue
                    for a5 in range(nmg + 1):
                        if a1 + a2 + a3 + a4 + a5 > nmg:
                            continue
                        for a6 in range(nmg + 1):
                            if a1 + a2 + a3 + a4 + a5 + a6 > nmg:
                                continue
                            for a7 in range(nmg + 1):
                                if a1 + a2 + a3 + a4 + a5 + a6 + a7 > nmg:
                                    continue
                                for a8 in range(nmg + 1):
                                    if a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 > nmg:
                                        continue
                                    for a9 in range(nmg + 1):
                                        if a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 != nmg:
                                            continue
                                        if goatcheck(
                                                a1 * [0] + a2 * [1] + a3 * [2] + a4 * [3] + a5 * [4] + a6 * [5] + a7 * [
                                                    6] + a8 * [7] + a9 * [
                                                    8]):
                                            cnt += multinomial([a1, a2, a3, a4, a5, a6, a7, a8, a9])
    return cnt


if __name__ == "__main__":
    num_goats = 9
    count = slight_improvement(num_goats)
    print(count)
