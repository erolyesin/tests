from __future__ import print_function
import textwrap

def merge_the_tools(string, k):
    word_list = textwrap.wrap(text=string, width=k)
    for word in word_list:
        print(''.join([char for indx, char in enumerate(word) if char not in word[:indx]]))

if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)