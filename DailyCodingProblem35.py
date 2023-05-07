# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def sort_RGB(arr):
    low, mid, high = 0, 0, len(arr)-1
    
    while mid <= high:

        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 'B':
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

        else:
            mid += 1

    print(arr)


arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
sort_RGB(arr)
