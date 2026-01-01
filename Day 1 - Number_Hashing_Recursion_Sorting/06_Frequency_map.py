# Frequency Map / Dictionary - A frequency map is a data structure that stores the frequency of each element in an array or list.

# input : [4, 4, 2, 5, 6, 4, 7, 1, 7]
# output : {4 : 4, 2 : 1, 5 : 1, 6 : 1, 7 : 2, 1 : 1}

arr = [4, 4, 2, 5, 6, 4, 7, 1, 7]
freq_map = {}  
for i in arr: # O(n)
    if i in freq_map: # O(1)
        freq_map[i] += 1
    else:
        freq_map[i] = 1
print(freq_map)

x=4
print(freq_map[x])

# Time Complexity - O(n)
# Space Complexity - O(n)

nums = [4, 4, 2, 5, 6, 4, 7, 1, 7]
freq_map = {}  
for i in nums: # O(n)
    freq_map[i] = freq_map.get(i, 0) + 1 # O(1)
print(freq_map)

# how this line works - freq_map[i] = freq_map.get(i, 0) + 1 
# get(i, 0) returns the value of the key i if it exists in the dictionary, otherwise it returns the default value 0