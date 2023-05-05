# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

import numpy as np

# convert x.0 to x, where x is an integer
def to_int(n):
    if n.is_integer():
        n = int(n)
    return n

# find the running median
def running_median(arr):
    print(arr[0]) # median of the array containing single element

    # inserting sort algorithm
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        
        # find median
        res = np.median(arr[:i+1])

        # print
        print(to_int(res))



test_arr = [2, 1, 5, 7, 2, 0, 5]
running_median(test_arr)