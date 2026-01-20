# N Meetings in One Room

# Given N meetings with their start and end times, the task is to find the maximum number of meetings that can be accommodated in a single room, assuming that only one meeting can be held in the room at a time.
# The meetings are represented as pairs of (start_time, end_time).

# Input : [(0, 30), (5, 10), (15, 20), (25, 30)]
# Output : 2

def max_meetings(meetings):
    meetings.sort(key=lambda x: x[1])
    
    count = 1
    last_end_time = meetings[0][1]
    
    for i in range(1, len(meetings)):
        if meetings[i][0] >= last_end_time:
            count += 1
            last_end_time = meetings[i][1]
            
    return count

meetings = [(0, 30), (5, 10), (15, 20), (25, 30)]
print("Maximum number of meetings that can be accommodated:", max_meetings(meetings))