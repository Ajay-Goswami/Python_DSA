# Combination Sum II  - Leetcode 40

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

def combination_sum2(candidates, target):
    def backtrack(remaining, combination, start):
        if remaining == 0:
            result.append(list(combination))
            return
        elif remaining < 0:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            combination.append(candidates[i])
            backtrack(remaining - candidates[i], combination, i + 1)
            combination.pop()

    candidates.sort()
    result = []
    backtrack(target, [], 0)
    return result

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combination_sum2(candidates, target))
