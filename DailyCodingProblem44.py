# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

# You may assume each element in the array is distinct.

# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.


# -------------------------------------------------------------------------------------------------------#

# using combinations TC: O(N^2)
from itertools import combinations

def count_inversions_way1(arr):
    count = 0

    for comb in combinations(arr, 2):
        if comb[0] > comb[1]:
            count += 1

    return count


# -------------------------------------------------------------------------------------------------------#


# using bisect module, TC: O(N logN)
import bisect

def count_inversions_way2(arr):
    sorted_arr = []
    count = 0
    for num in arr:
        # Find the index where num should be inserted in the sorted_arr
        idx = bisect.bisect_right(sorted_arr, num)
        # Add the number to the sorted_arr
        sorted_arr.insert(idx, num)
        # The number of inversions is the number of elements to the right of the index
        count += len(sorted_arr) - idx - 1
    return count


# -------------------------------------------------------------------------------------------------------#


# using merge sort algorithm, TC: O(N logN)
def count_inversions_way3(arr):
    # Base case: if array is empty or has only one element, it is sorted
    if len(arr) < 2:
        return 0
    
    # Recursive case: split the array in two and count inversions in each half
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    inversions = count_inversions_way3(left) + count_inversions_way3(right)
    
    # Merge the two sorted halves while counting inversions
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            i += 1
        else:
            inversions += len(left) - i
            j += 1
            
    return inversions


# -------------------------------------------------------------------------------------------------------#

# tests
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 1, 3, 5]
arr3 = [5, 4, 3, 2, 1] 

print("Total inversions way1:", count_inversions_way1(arr1))
print("Total inversions way2:", count_inversions_way2(arr2))
print("Total inversions way3:", count_inversions_way3(arr3))