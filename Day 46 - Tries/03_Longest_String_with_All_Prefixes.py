# 03. Longest String with All Prefixes
# Tries

# Problem: You are given an array of strings 'words'. A string is called
# "complete" if every prefix of that string is also present in the array.
# Return the longest complete string. If there are multiple with the same
# length, return the lexicographically smallest one. If no complete string
# exists, return "None".

# Input: words = ["n", "ni", "nin", "ninj", "ninja", "nit"]
# Output: "ninja"

# Explanation: Let's check each word -
# "n" -> prefix "" (empty) is trivially there, and "n" itself is in array. Complete.
# "ni" -> needs "n" in array. Yes. Complete.
# "nin" -> needs "n", "ni". Both present. Complete.
# "ninj" -> needs "n", "ni", "nin". All present. Complete.
# "ninja" -> needs "n", "ni", "nin", "ninj". All present. Complete. Length 5.
# "nit" -> needs "n", "ni". Both present. Complete. But length is only 3.
# Longest complete string is "ninja" with length 5.

# Time Complexity: O(N * L) where N = number of words, L = max word length
# Space Complexity: O(N * L) for the trie


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    # Check if every prefix of the word (including the word itself) was inserted
    def hasAllPrefixes(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if not node.isEnd:
                return False
        return True


# ---- Main Logic ----
# Time: O(N * L) for inserting + O(N * L) for checking = O(N * L)
# Space: O(N * L) for the trie

def longestStringWithAllPrefixes(words):
    trie = Trie()

    # First insert all words into the trie
    for w in words:
        trie.insert(w)

    longest = ""

    # Now check each word if all its prefixes exist
    for w in words:
        if trie.hasAllPrefixes(w):
            # Pick longer one, or lexicographically smaller if same length
            if len(w) > len(longest) or (len(w) == len(longest) and w < longest):
                longest = w

    return longest if longest else "None"


words = ["n", "ni", "nin", "ninj", "ninja", "nit"]
print(f"Longest complete string: {longestStringWithAllPrefixes(words)}")  # ninja

words2 = ["a", "ab", "abc", "b", "bc"]
print(f"Longest complete string: {longestStringWithAllPrefixes(words2)}")  # abc
