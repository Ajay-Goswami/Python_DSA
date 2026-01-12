# Combination Sum - Leetcode 39

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# Input : candidates = [2,3,6,7], target = 7
# Output : [[7],[2,2,3]]

def combination_sum(candidates, target):
    def backtrack(remaining, combination, start):
        if remaining == 0:
            result.append(list(combination))
            return
        elif remaining < 0:
            return

        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            backtrack(remaining - candidates[i], combination, i)
            combination.pop()

    result = []
    backtrack(target, [], 0)
    return result

candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))