def getOneBits(n):
    count = 0
    n = int(n)
    arr = [0]
    bin_str = list(bin(n))[2:]
    indx = 2
    print("%d: %s" % (n, bin_str))
    while (n):
        n &= (n - 1)
        count += 1
        # next three lines determines the location of the 1's
        indx = bin_str.index('1')
        bin_str[indx] = '-'
        arr.append(indx+1)

    arr[0] = count
    return arr


if __name__ == '__main__':
    n = 255

    result = getOneBits(n)

    print('\n'.join(map(str, result)))
    print('\n')
