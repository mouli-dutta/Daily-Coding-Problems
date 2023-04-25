# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. 
# You can modify the input array in-place and you do not need to store the results. 
# You can simply print them out as you compute them.
# ----------------------------------------------------------------------------------------------


# using two pointer technique
# with O(n) time and O(1) space
def max_values(arr, k):
    # length of the array
    n = len(arr)

    # if k is greater than length of the array simply return none
    if k > n:
        print('Invalid input')

    # Initialize left and right pointers
    left = 0
    right = k

    # Loop through the array, updating pointers and printing max value of each subarray
    while right < n+1:
        # print(f'arr = {arr[left:right]}')

        print(max(arr[left:right]))
        left += 1
        right += 1


max_values([10, 5, 2, 7, 8, 7], 3)
