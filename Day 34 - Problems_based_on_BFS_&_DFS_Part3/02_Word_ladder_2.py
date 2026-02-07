# 02. Word Ladder II – LeetCode 126
# BFS + DFS (Backtracking)

# Problem: Find ALL shortest transformation sequences from beginWord to endWord.

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]

from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList)
    parents = defaultdict(list)
    level = {beginWord}
    found = False

    while level and not found:
        next_level = defaultdict(list)

        for word in level:
            wordSet.discard(word)

        for word in level:
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in wordSet:
                        next_level[newWord].append(word)
                        if newWord == endWord:
                            found = True

        level = next_level
        for k in next_level:
            parents[k].extend(next_level[k])

    res = []

    def dfs(word, path):
        if word == beginWord:
            res.append(path[::-1])
            return
        for p in parents[word]:
            dfs(p, path + [p])

    if found:
        dfs(endWord, [endWord])

    return res


# Driver code
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(findLadders(beginWord, endWord, wordList))
