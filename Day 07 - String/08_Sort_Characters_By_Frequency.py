# Leetcode 451 : Sort Characters By Frequency

# Input: s = "tree"
# Output: "eert"

# Input: s = "cccaaa"
# Output: "cccaaa"

s = "cccaaa"

def frequencySort(s)-> str:
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    res = ""
    for i in freq:
        res += i[0] * i[1]
    return res

print(frequencySort(s))