# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

# Do this in O(N) time and O(1) space.


# O(N) time and space
from collections import Counter

def find_single_number(arr):
    return next(filter(lambda x: Counter(arr)[x] == 1, arr))

tests = [[6, 1, 3, 3, 3, 6, 6], [13, 19, 13, 13]]
print("\n".join(str(find_single_number(test)) for test in tests))