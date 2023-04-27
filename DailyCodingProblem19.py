# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

def min_cost(cost):
    n = len(cost)
    k = len(cost[0])
    prev_min_cost = [0] * k
    curr_min_cost = [0] * k
    for j in range(k):
        prev_min_cost[j] = cost[0][j]
    for i in range(1, n):
        for j in range(k):
            curr_min_cost[j] = cost[i][j] + min(prev_min_cost[x] for x in range(k) if x != j)
        prev_min_cost = curr_min_cost[:]
    return min(curr_min_cost)



# Test case 1
cost1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(min_cost(cost1))

# Test case 2
cost2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print(min_cost(cost2))

# Test case 3
cost3 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]

print(min_cost(cost3))

