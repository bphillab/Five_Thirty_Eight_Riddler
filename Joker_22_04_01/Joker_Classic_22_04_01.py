def pred_next(x):
    temp = {2 * x}
    if x % 2 == 0 and x % 3 == 1:
        temp.add((x - 1) / 3)
    return temp


def step(curr, prev):
    nxt = set()
    for i in curr:
        nxt = nxt.union(pred_next(i))
    nxt = nxt.difference(prev)
    return nxt


if __name__ == '__main__':
    curr = {1}
    prev = {1}
    for i in range(40):
        curr = step(curr, prev)
        prev = curr.union(prev)
    print(sorted({i for i in range(400)}.difference(prev)))
