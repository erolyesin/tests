from __future__ import print_function
import textwrap


def wrap(string, max_width):
    word_list = (word+'\n' for word in textwrap.wrap(text=string, width=max_width))

    return ''.join(word_list)


if __name__ == '__main__':
    string, max_width = 'dfbiwefweubwebb', 4
    result = wrap(string, max_width)
    print(result)