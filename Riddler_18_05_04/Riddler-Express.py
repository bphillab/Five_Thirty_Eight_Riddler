if __name__ == '__main__':
    for A in range(10):
        for B in range(10):
            for C in range(10):
                for D in range(10):
                    for E in range(10):
                        if (100000*A+10000*B+1000*C+100*C+10*D+E)*4 == (100000*E+10000*D+1000*C+100*C+10*B+A):
                            print(str(100000*A+10000*B+1000*C+100*C+10*D+E))