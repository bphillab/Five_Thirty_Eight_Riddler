class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]


@Memoize
def prob_reach_end(current, n):
    if n==1:
        return 1
    if current >= (n+1)/2:
        return sum([prob_reach_end(i,n-1) for i in range(1,current)])/(n-1)
    if current < (n+1)/2:
        return sum([prob_reach_end(i,n-1) for i in range(current,n)])/(n-1)

def calc_for_a_n(n):
    return sum([prob_reach_end(i,n) for i in range(1,n+1)])/n