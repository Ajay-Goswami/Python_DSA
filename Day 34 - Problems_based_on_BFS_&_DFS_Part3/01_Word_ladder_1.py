# 01. Word Ladder – LeetCode 127
# BFS based shortest path problem

# Problem: You are given two words: beginWord and endWord, and a wordList.
# Each step you can change only ONE character and the new word must exist in wordList.
# Return the length of the shortest transformation sequence. If no such sequence exists, return 0.

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: hit -> hot -> dot -> dog -> cog

from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque()
    queue.append((beginWord, 1))  # (current_word, level)

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + ch + word[i+1:]

                if newWord in wordSet:
                    wordSet.remove(newWord)   # visited
                    queue.append((newWord, level + 1))

    return 0


# Driver code
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))
