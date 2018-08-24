from numpy.random import uniform


def echo_guess(v1,v2,l):
    if v1 <= v2:
        return 0
    # (k+l) v2 = (l-k)v1
    # k = l (v1-v2)/(v1+v2
    k = l*(v1-v2)/(v1+v2)
    return v1/(2*l+2*k), v2/(2*l-2*k), k,v1/(2*l+2*k) - v2/(2*l-2*k)


if __name__ == "__main__":
    v1, v2,l = uniform(0,1,3)
    epsilon = 0.0001
    print(" Checking: ", echo_guess(max(v1,v2)+epsilon, min(v1,v2)-epsilon,l))
