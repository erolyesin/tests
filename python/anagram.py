from __future__ import division
from collections import Counter


# Checks if the two strings are anagrams of each other
# This method uses only built-ins
# Params: str1, str2  strings to compare
# Return: True if anagrams, otherwise False
def is_anagram_wo_lib(str1, str2):
    if str1 == str2:
        return False

    if sorted(str1) == sorted(str2):
        return True

    return False


# Checks if the two strings are anagrams of each other
# This method uses the collections library
# Params: str1, str2  strings to compare
# Return: True if anagrams, otherwise False
def is_anagram_w_lib(str1, str2):
    if str1 == str2:
        return False
    return Counter(str1) == Counter(str2)


if __name__ == "__main__":
    str1 = "Hello"
    str2 = "Ohell"
    str3 = "oelhll"
    str4 = "hhhhh"
    str5 = "Mello"
    str6 = "Hello"
    str7 = "oHell"
    str8 = "oHeel"

    is_anagram_func = is_anagram_wo_lib

    print(str1 + " angram of " + str2 + '? ' + str(is_anagram_func(str1, str2)))
    print(str2 + " angram of " + str3 + '? ' + str(is_anagram_func(str2, str3)))
    print(str3 + " angram of " + str1 + '? ' + str(is_anagram_func(str3, str1)))
    print(str4 + " angram of " + str1 + '? ' + str(is_anagram_func(str4, str1)))
    print(str1 + " angram of " + str5 + '? ' + str(is_anagram_func(str1, str5)))
    print(str1 + " angram of " + str6 + '? ' + str(is_anagram_func(str1, str6)))
    print(str1 + " angram of " + str7 + '? ' + str(is_anagram_func(str1, str7)))
    print(str1 + " angram of " + str8 + '? ' + str(is_anagram_func(str1, str8)))
