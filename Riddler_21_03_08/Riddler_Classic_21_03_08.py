if __name__ == "__main__":
    upper_limit = 1000
    temp = 0
    for i in range(1, 1000):
        blah = round(1000 * (1000 - i - temp - 1) / (1000 - i))
        if blah == 1000 - i:
            continue
        if blah < 1000 - i:

            temp = temp - 1
            blah = round(1000 * (1000 - i - temp - 1) / (1000 - i))
            if blah != 1000 - i:
                print(1000 - i)
                break
        if blah > 1000 - i:
            temp = temp + 1
            blah = round(1000 * (1000 - i - temp - 1) / (1000 - i))
            if blah != 1000 - i:
                print(1000 - i)
                break
