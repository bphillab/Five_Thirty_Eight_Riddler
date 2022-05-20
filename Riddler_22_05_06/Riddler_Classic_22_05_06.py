from sympy import primerange, isprime


def generate_primes(num_digits):
    return [i for i in primerange(10 ** (num_digits - 1), 10 ** (num_digits))]


def gen_part(pr, pl):
    strpr = list(str(pr))
    tmp = strpr
    acc = []
    for i in range(10):
        if pl == strpr[pl]:
            continue
        if pl == 0 and i == 0:
            continue
        tmp[pl] = str(i)
        acc = acc + [int(''.join(tmp))]
    return acc


def generate_next(pr):
    acc = set()
    for i in range(len(str(pr))):
        acc = acc.union(gen_part(pr, i))
    return [i for i in acc if isprime(i)]


def web_step(nxt, acc):
    acc1 = set()
    for i in nxt:
        acc1 = acc1.union(generate_next(i))
    return [i for i in acc1 if i not in acc]


def get_largest(pr):
    i = 0
    acc = [pr]
    nxt = [pr]
    while nxt:
        i = i + 1
        acc = acc + nxt
        nxt = web_step(nxt, acc)
    return i, acc


if __name__ == '__main__':
    n = 3
    length_largest_chain = 0
    largest_start = 1
    largest_end = 1
    primes = generate_primes(n)
    for prime in primes:
        l_chain, largest_chain = get_largest(prime)
        if l_chain > length_largest_chain:
            length_largest_chain = l_chain
            largest_start = prime
            largest_end = largest_chain[-1]
    print(length_largest_chain)
    print(largest_start)
    print(largest_end)
