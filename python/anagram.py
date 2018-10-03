from __future__ import division
from collections import Counter


# Checks if the two strings are anagrams of each other
# This method does not use any libraries
# Params: str1, str2  strings to compare
# Return: True if anagrams, otherwise False
def is_ana(str1, str2):
    if len(str1) != len(str2):
        return False

    for char in str1:
        if char not in str2:
            return False

    for char in str2:
        if char not in str1:
            return False

    return True


# Checks if the two strings are anagrams of each other
# This method uses the collections library
# Params: str1, str2  strings to compare
# Return: True if anagrams, otherwise False
def is_anagram(str1, str2):
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

    print(str1 + " angram of " + str2 + '? ' + str(is_anagram(str1, str2)))
    print(str2 + " angram of " + str3 + '? ' + str(is_anagram(str2, str3)))
    print(str3 + " angram of " + str1 + '? ' + str(is_anagram(str3, str1)))
    print(str4 + " angram of " + str1 + '? ' + str(is_anagram(str4, str1)))
    print(str1 + " angram of " + str1 + '? ' + str(is_anagram(str1, str1)))
    print(str1 + " angram of " + str5 + '? ' + str(is_anagram(str1, str5)))
    print(str1 + " angram of " + str6 + '? ' + str(is_anagram(str1, str6)))
