def update_prob(old, n, l = 1/2):
    return old + (1-old)*l**(n+1)


if __name__ == '__main__':
    x = 0
    n = 0
    for n in range(1000):
        x = update_prob(x, n)
    print("Value: ")
    print(x)
    print("Next step difference added: ")
    print(x-update_prob(x,n+1))
