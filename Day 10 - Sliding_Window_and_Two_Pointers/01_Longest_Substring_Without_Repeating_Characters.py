# Longest Substring Without Repeating Characters

# Leetcode : 3

# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3

# Input: s = "bbbbb"
# Output: 1

def lengthOfLongestSubstring(s: str) -> int: # Sliding Window Approach: O(N) time | O(min(N, M)) space
    char_index_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3