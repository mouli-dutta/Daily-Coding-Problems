# Good morning! Here's your coding interview problem for today.

# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def largest_sum_nonadjacent(arr):
    if not arr:
        return 0
    if len(arr) <= 2:
        return max(arr)
    max_sum = [0] * len(arr)
    max_sum[0] = arr[0]
    max_sum[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        max_sum[i] = max(max_sum[i-2] + arr[i], max_sum[i-1])
    return max(max_sum[-1], max_sum[-2])



def test():
    assert largest_sum_nonadjacent([2, 4, 6, 2, 5]) == 13
    assert largest_sum_nonadjacent([5, 1, 1, 5]) == 10
    assert largest_sum_nonadjacent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
    assert largest_sum_nonadjacent([10, -10, 10, -10, 10, -10, 10]) == 40
    assert largest_sum_nonadjacent([-5, -1, -2, -4, -3]) == -1
    assert largest_sum_nonadjacent([1, 2, 3, 4, 5, 6, 7, 8, 9, -10]) == 25
    assert largest_sum_nonadjacent([1, 2, 3, 4, 5, 6, 7, 8, -9, 10]) == 30

    print('All tests passed.')

test()