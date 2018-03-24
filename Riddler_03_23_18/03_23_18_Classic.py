import numpy as np

def produce_next_digit(a, b):
    '''Function that produces the next digit for a transpose double'''
    if b>=5:
        return divmod(2*a+1,10)[1]
    else:
        return divmod(2*a,10)[1]


def make_the_number(base,upper_digit_bound=20):
    '''Function that takes a base number and produces the full integer that makes the transposed double'''
    num = [base]
    temp = produce_next_digit(base,0)
    while (temp != base or num[0]>=5 or num[0]==0) and len(num)<upper_digit_bound:
        num = [temp]+num
        temp = produce_next_digit(num[0],num[1])
    return int(''.join([str(i) for i in num]))


def check_the_digits():
    '''checks all digits'''
    sols = []
    for i in range(2,10): #Presumably no 0s in front, 1 doesn't work either
        temp = make_the_number(i)
        if temp < 10**20:
            sols = sols+[temp]
    least = np.min(sols)
    return divmod(least,10)[1],least


if __name__ == '__main__':
    print(check_the_digits())
    #(2, 105263157894736842)
