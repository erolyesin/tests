from __future__ import print_function


def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    const_count = 0
    vowel_count = 0
    for idx, letter in enumerate(string):
        if letter in vowels:
            vowel_count += len(string) - idx
        else:
            const_count += len(string) - idx

    if const_count == vowel_count:
        print('Draw')
    if const_count > vowel_count:
        print('Stuart %d' % const_count)
    if vowel_count > const_count:
        print('Kevin %d' % vowel_count)


if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)