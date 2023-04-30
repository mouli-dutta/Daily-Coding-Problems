# Good morning! Here's your coding interview problem for today.

# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def getMinRooms(intervals):
    room_count = 0
    max_end_time = 0

    for interval in intervals:
        start_time = interval[0]
        end_time = interval[1]
        
        if start_time >= max_end_time:
            max_end_time = end_time            
        else:
            room_count += 1
        
        max_end_time = max(max_end_time, end_time)
  
    print(room_count)

getMinRooms([(30, 75), (0, 50), (60, 150)])
