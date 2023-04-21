#Good morning! Here's your coding interview problem for today.

#This problem was asked by Stripe.

#Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#You can modify the input array in-place.




# Runs in O(n) time and uses O(1) auxiliary space, but
# rearranges the elements of the array
def first_missing(arr):

    for i in range(len(arr)):
         toPlace = arr[i]
         
         while 1 <= toPlace <= len(arr) and arr[toPlace - 1] != toPlace:
             arr[i], arr[toPlace - 1] = arr[toPlace - 1], arr[i]
             toPlace = arr[i]
    
    for i in range(len(arr)):
        if arr[i] != i + 1:
             return i + 1
    
    return len(arr)


a1 = [3, 4, -1, 1]
a2 = [1, 2, 0]
print(first_missing(a1))
print(first_missing(a2))