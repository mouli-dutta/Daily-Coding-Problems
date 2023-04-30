# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board. 
# Each True boolean represents a wall. 
# Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate, 
# return the minimum number of steps required to reach the end coordinate from the start. 
# If there is no possible path, then return null. 
# You can move up, left, down, and right. 
# You cannot move through walls. 
# You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.


import heapq

def min_steps(board, start, end):
    # Define the directions we can move in
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Initialize the distances of all nodes from the start node to infinity
    distances = [[float('inf')] * len(board[0]) for _ in range(len(board))]
    distances[start[0]][start[1]] = 0
    
    # Initialize the priority queue with the start node
    pq = [(0, start)]
    
    # Start the Dijkstra's algorithm
    while pq:
        dist, curr = heapq.heappop(pq)
        
        if curr == end:
            return dist
        
        for d in directions:
            next_pos = (curr[0] + d[0], curr[1] + d[1])
            
            # Check if the next position is within bounds and can be visited
            if 0 <= next_pos[0] < len(board) and 0 <= next_pos[1] < len(board[0]) and \
                board[next_pos[0]][next_pos[1]] == False:
                
                # Calculate the distance of the next position from the start node
                next_dist = dist + 1
                
                # Update the distance of the next position if it is shorter than its current distance
                if next_dist < distances[next_pos[0]][next_pos[1]]:
                    distances[next_pos[0]][next_pos[1]] = next_dist
                    
                    # Add the next position to the priority queue
                    heapq.heappush(pq, (next_dist, next_pos))
    
    # If we reach here, there is no path from start to end
    return None

# Test case
board = [[False, False, False, False],
         [True, True, False, True],
         [False, False, False, False],
         [False, False, False, False]]
start = (3, 0)
end = (0, 0)
print(min_steps(board, start, end)) 
