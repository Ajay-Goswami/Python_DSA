# 04. Number of Distinct Substrings in a String
# Tries

# Problem: Given a string 's', return the count of distinct substrings of
# the string (including the empty substring). Use a trie based approach.

# Input: s = "abab"
# Output: 8

# Explanation: All possible substrings are:
# "", "a", "b", "ab", "ba", "aba", "bab", "abab"
# That's 8 distinct substrings counting the empty one.
# Note: "a" appears at index 0 and 2 but we count it once.
# Similarly "ab" appears at index 0 and 2 but counted once.

# Time Complexity: O(n^2) | Space Complexity: O(n^2)
# where n is the length of the string


class TrieNode:
    def __init__(self):
        self.children = {}


# ---- Approach: Trie Based ----
# Time: O(n^2) | Space: O(n^2) for trie nodes in worst case
# Idea: Insert all suffixes of the string into a trie. Every time we
# create a new node in the trie, that means we found a new distinct
# substring. At the end, add 1 for the empty substring.

def countDistinctSubstrings(s):
    root = TrieNode()
    n = len(s)
    count = 0

    for i in range(n):
        node = root
        for j in range(i, n):
            ch = s[j]
            if ch not in node.children:
                node.children[ch] = TrieNode()
                count += 1  # new distinct substring found
            node = node.children[ch]

    return count + 1  # +1 for the empty substring


s = "abab"
print(f"Distinct substrings of '{s}': {countDistinctSubstrings(s)}")  # 8

s2 = "aaa"
print(f"Distinct substrings of '{s2}': {countDistinctSubstrings(s2)}")  # 4
# "", "a", "aa", "aaa" -> 4
