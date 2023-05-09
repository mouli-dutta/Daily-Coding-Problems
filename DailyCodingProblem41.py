# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.




# Time Complexity: O(E log E), where E is the number of flights (i.e., the number of edges in the graph), due to the sorting step. 
# Space Complexity: O(E), to store the graph.

from collections import defaultdict

def find_itinerary(flights, start):
    # Construct the graph
    graph = defaultdict(list)
    for origin, destination in flights:
        graph[origin].append(destination)

    # Sort the destinations lexicographically
    for origin in graph:
        graph[origin].sort()

    # Perform a depth-first search
    def dfs(origin):
        nonlocal itinerary
        while graph[origin]:
            dfs(graph[origin].pop(0))
        itinerary.append(origin)

    # Initialize the itinerary and perform the search
    itinerary = []
    dfs(start)

    # Return the reversed itinerary (since we built it backwards)
    return itinerary[::-1] if len(itinerary) == len(flights) + 1 else None



# tests
flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
start = 'YUL'
print(find_itinerary(flights, start))


flights2 = [('SFO', 'COM'), ('COM', 'YYZ')] 
start2 = 'COM'
print(find_itinerary(flights2, start2))


flights3 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
start3 = 'A'
print(find_itinerary(flights3, start3))