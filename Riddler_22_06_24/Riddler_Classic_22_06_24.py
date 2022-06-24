def goatcheck(goats):
    tempgoats = goats
    numgoats = len(goats)
    tempgoats.sort()
    for i in range(numgoats):
        if tempgoats[i] > i:
            return 1
    return 0


if __name__ == "__main__":
    nmg = 9
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
    print(cnt)
