# Minimun number of platforms required for a railway

# Given arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits.
# We are given two arrays that represent the arrival and departure times of trains that stop.
# We need to find the minimum number of platforms required for the railway station so that no train waits.

# Input: arrival = [900, 940, 950, 1100, 1500, 1800]
#        departure = [910, 1200, 1120, 1130, 1900, 2000]
# Output: 3

def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()
    
    platform_needed = 0
    max_platforms = 0
    i = 0
    j = 0
    n = len(arrival)
    
    while i < n and j < n:
        if arrival[i] < departure[j]:
            platform_needed += 1
            max_platforms = max(max_platforms, platform_needed)
            i += 1
        else:
            platform_needed -= 1
            j += 1
            
    return max_platforms

arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
print(min_platforms(arrival, departure))