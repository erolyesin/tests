def getMinimumUniqueSum(arr):
    count = 0
    for indx, val in enumerate(arr):
        try:
            found = arr[indx + 1:].index(val)
            new_val = 1
            arr[found + indx + 1] = 0
            while new_val in arr:
                new_val += 1
            arr[found + indx + 1] = new_val
        except:
            pass
        count += val
    return count


if __name__ == '__main__':
    arr_count = int(raw_input())

    arr = []

    for _ in xrange(arr_count):
        arr_item = int(raw_input())
        arr.append(arr_item)

    res = getMinimumUniqueSum(arr)

    print(str(res) + '\n')
