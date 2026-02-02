# Replace each array element by its corresponding rank

# Leetcode – Similar to Rank Transform of an Array
# Given an array, replace each element by its rank.
# Rank is defined as:
# - The smallest element gets rank 1
# - Same values get the same rank
# - Ranks increase sequentially

# Input:  nums = [40, 10, 20, 30]
# Output: [4, 1, 2, 3]

# Input:  nums = [100, 100, 100]
# Output: [1, 1, 1]

nums = [40, 10, 20, 30]

# ----------------------------------------------------
# Brute Force Approach
# Time Complexity -> O(n log n)
# Space Complexity -> O(n)
# ----------------------------------------------------
def replace_with_rank_bruteforce(nums):
    # Sort unique elements
    sorted_unique = sorted(set(nums))

    # Assign ranks
    rank_map = {}
    rank = 1
    for num in sorted_unique:
        rank_map[num] = rank
        rank += 1

    # Replace elements with ranks
    result = []
    for num in nums:
        result.append(rank_map[num])

    return result

print("Rank using Brute Force ->", replace_with_rank_bruteforce(nums))


# ----------------------------------------------------
# Optimal Approach (Cleaner & Interview Friendly)
# Time Complexity -> O(n log n)
# Space Complexity -> O(n)
# ----------------------------------------------------
def replace_with_rank_optimal(nums):
    # Create rank mapping using sorted unique values
    rank_map = {num: idx + 1 for idx, num in enumerate(sorted(set(nums)))}

    # Replace original array values with ranks
    return [rank_map[num] for num in nums]

print("Rank using Optimal Approach ->", replace_with_rank_optimal(nums))