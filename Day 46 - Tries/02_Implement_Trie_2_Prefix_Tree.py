# 02. Implement Trie II (Prefix Tree II)
# Tries

# Problem: Implement a Trie that supports the following operations:
# insert(word) - inserts a word into the trie.
# countWordsEqualTo(word) - returns how many times the exact word was inserted.
# countWordsStartingWith(prefix) - returns how many inserted words have this prefix.
# erase(word) - removes one occurrence of the word from the trie.

# Input:
# insert("apple"), insert("apple"), insert("apps"),
# countWordsEqualTo("apple"), countWordsStartingWith("app"),
# erase("apple"), countWordsEqualTo("apple")
# Output: 2, 3, 1

# Explanation: "apple" was inserted twice so countWordsEqualTo returns 2.
# All three words ("apple", "apple", "apps") start with "app" so prefix
# count is 3. After erasing one "apple", count drops to 1.

# Time Complexity: O(len(word)) for each operation | Space Complexity: O(N * len(word))


class TrieNode:
    def __init__(self):
        self.children = {}
        self.countEndsWith = 0    # how many words end exactly here
        self.countPrefix = 0      # how many words pass through this node


class Trie2:
    def __init__(self):
        self.root = TrieNode()

    # ---- Insert ----
    # Time: O(len(word)) | Space: O(len(word)) worst case
    # Traverse char by char, increment countPrefix at every node along the way.
    # At the final node, also increment countEndsWith.

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.countPrefix += 1
        node.countEndsWith += 1

    # ---- Count Words Equal To ----
    # Time: O(len(word)) | Space: O(1)
    # Walk through the trie. If any char is missing, return 0.
    # Otherwise return countEndsWith at the last node.

    def countWordsEqualTo(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.countEndsWith

    # ---- Count Words Starting With ----
    # Time: O(len(prefix)) | Space: O(1)
    # Same traversal but return countPrefix instead of countEndsWith.

    def countWordsStartingWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.countPrefix

    # ---- Erase ----
    # Time: O(len(word)) | Space: O(1)
    # Only call this if the word actually exists. Walk through and decrement
    # countPrefix at each node. At the end decrement countEndsWith too.

    def erase(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.countPrefix -= 1
        node.countEndsWith -= 1


trie = Trie2()

trie.insert("apple")
trie.insert("apple")
trie.insert("apps")

print(f"countWordsEqualTo('apple'): {trie.countWordsEqualTo('apple')}")           # 2
print(f"countWordsStartingWith('app'): {trie.countWordsStartingWith('app')}")     # 3

trie.erase("apple")
print(f"countWordsEqualTo('apple') after erase: {trie.countWordsEqualTo('apple')}")  # 1
