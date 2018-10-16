from __future__ import print_function


def count_substring(string, sub_string):
    count = 0
    indx = 0
    while True:
        indx = string.find(sub_string, indx)
        if indx == -1:
            break
        count += 1
        indx += 1
    return count


if __name__ == '__main__':
    string = "sususofsus"
    sub_string = "sus"

    count = count_substring(string, sub_string)
    print(count)
