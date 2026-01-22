# Leetcode 151 - Reverse Words in a String

# Input: s = "the sky is blue"
# Output: "blue is sky the"

s = "the sky is blue"
words = s.split()
words.reverse()
res = " ".join(words)
print(res)