def score_a_point_flat(a,b,c,i):
    dist_a = abs(a-i)
    dist_b = abs(b - i)
    dist_c = abs(c - i)
    min_dist = min([dist_a,dist_b,dist_c])
    flag_a = False
    flag_b = False
    flag_c = False
    if dist_a == min_dist:
        flag_a = True
    if dist_b == min_dist:
        flag_b = True
    if dist_c == min_dist:
        flag_c = True
    num_closest = flag_a+flag_b+flag_c
    return (flag_a/(num_closest),flag_b/num_closest, flag_c/num_closest)


def score_flat(a,b,c, n):
    scores = [[i*j for j in score_a_point_flat(a,b,c,i)] for i in range(1,n+1)]
    return (sum([i[0] for i in scores]), sum([i[1] for i in scores]), sum([i[2] for i in scores]))


def score_a_point_clock(a,b,c,i):
    dist_a = min([abs(a-i),abs(a-i-12),abs(a-i+12)])
    dist_b = min([abs(b - i),abs(b-i-12),abs(b-i+12)])
    dist_c = min([abs(c - i),abs(c-i-12),abs(c-i+12)])
    min_dist = min([dist_a,dist_b,dist_c])
    flag_a = False
    flag_b = False
    flag_c = False
    if dist_a == min_dist:
        flag_a = True
    if dist_b == min_dist:
        flag_b = True
    if dist_c == min_dist:
        flag_c = True
    num_closest = flag_a+flag_b+flag_c
    return (flag_a/(num_closest),flag_b/num_closest, flag_c/num_closest)


def score_clock(a,b,c, n):
    scores = [[i*j for j in score_a_point_clock(a,b,c,i)] for i in range(1,n+1)]
    return (sum([i[0] for i in scores]), sum([i[1] for i in scores]), sum([i[2] for i in scores]))


def c_move(a,b,n,score_func = score_flat):
    scores = [tuple([c])+score_func(a,b,c,n) for c in range(1,n+1) if c not in [a,b]]
    scores.sort(key = lambda x:-x[3])
    return scores[0]


def b_move(a,n,score_func = score_flat):
    scores = [tuple([b])+c_move(a,b,n,score_func) for b in range(1,n+1) if b != a]
    scores.sort(key = lambda x:-x[3])
    return scores[0]


def a_move(n,score_func = score_flat):
    scores = [tuple([a])+b_move(a,n,score_func) for a in range(1,n+1)]
    scores.sort(key = lambda x:-x[3])
    return scores[0]



if __name__=='__main__':
    print("For on line, 10 spots: ")
    print(a_move(10))
    print("For on a clock: ")
    print(a_move(12, score_clock))
