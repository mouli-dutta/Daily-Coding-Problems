# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.


def get_edit_distance(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    dist = abs(n1 - n2)

    for i in range(min(n1, n2)):
        if str1[i] != str2[i]:
            dist += 1

    return dist


tests = [("kitten", "sitting"), ("horse", "ros"), ("intention", "execution"), ("abcdefg", "hijklmnop"), ("", "abc"), ("abcd", "abcd")]

for test in tests:
    print(get_edit_distance(test[0], test[1]))