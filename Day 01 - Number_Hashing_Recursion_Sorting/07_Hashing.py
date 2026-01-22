# Hashing - A hash table is a data structure that stores data in a way that allows for fast access to specific elements based on their unique keys.

# Ques - Check if Two Strings Are Anagrams
# input : s = "anagram", t = "nagaram"
# output : True

# brute force - time complexity O(nlogn)
s = "anagram"
t = "nagaram"
if sorted(s) == sorted(t): # O(nlogn)
    print("True")
else:
    print("False")

# optimized - time complexity O(n)
s = "anagram"
t = "nagaram"
if len(s) != len(t):
    print("False")
else:
    count = [0] * 26 # O(1)
    for i in s: # O(n)
        count[ord(i) - ord('a')] += 1 # O(1)
    for i in t: # O(n)
        count[ord(i) - ord('a')] -= 1 # O(1)
    for i in count: # O(1)
        if i != 0:
            print("False")
            break
    else:
        print("True")

# Optimised using dictionary and Function - time complexity O(n)
def is_anagram(s, t): # O(n)
    if len(s) != len(t): # O(1)
        return False

    count = {} # O(1)
    for ch in s: # O(n)
        count[ch] = count.get(ch, 0) + 1 # O(1)
    for ch in t:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1
    return True

print(is_anagram("anagram", "nagaram"))


# Using Counter - time complexity O(n)
from collections import Counter
s = "anagram"
t = "nagaram"
print(Counter(s) == Counter(t)) # O(n) 

