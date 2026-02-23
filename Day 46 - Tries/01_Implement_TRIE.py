# 01. Implement TRIE (Prefix Tree)
# Tries

# Problem: Implement a Trie data structure that supports three operations.
# insert(word) - inserts a word into the trie. search(word) - returns True
# if the word exists in the trie, otherwise False. startsWith(prefix) -
# returns True if any previously inserted word starts with the given prefix.

# Input:
# insert("apple"), insert("app"), search("apple"), search("app"),
# search("appl"), startsWith("app"), startsWith("ban")
# Output: True, True, False, True, False

# Explanation: After inserting "apple" and "app", searching "apple" returns
# True because it was inserted. "app" also returns True. But "appl" was
# never inserted so it returns False. startsWith("app") is True since both
# words start with "app". startsWith("ban") is False, nothing starts with it.

# Time Complexity: O(len(word)) for each operation | Space Complexity: O(N * len(word))
# where N is number of words inserted


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # ---- Insert ----
    # Time: O(len(word)) | Space: O(len(word)) worst case for new nodes
    # We go character by character. If the char doesn't have a node yet,
    # we create one. At the end, mark that node as end of word.

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    # ---- Search ----
    # Time: O(len(word)) | Space: O(1)
    # Traverse the trie following each character. If at any point the char
    # is missing, the word doesn't exist. If we reach the end, check isEnd.

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd

    # ---- StartsWith (Prefix Search) ----
    # Time: O(len(prefix)) | Space: O(1)
    # Same as search but we don't need isEnd to be True. Just reaching the
    # end of prefix means some word with that prefix was inserted before.

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


trie = Trie()

trie.insert("apple")
trie.insert("app")

print(f"search('apple'): {trie.search('apple')}")     # True
print(f"search('app'): {trie.search('app')}")           # True
print(f"search('appl'): {trie.search('appl')}")         # False
print(f"startsWith('app'): {trie.startsWith('app')}")   # True
print(f"startsWith('ban'): {trie.startsWith('ban')}")   # False
