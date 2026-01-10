# Fruit Into Baskets

# Leetcode : 904

# You have a row of fruit trees, each producing one type of fruit. You can use only two baskets, and each basket can hold only one fruit type (no quantity limit).
# Start from any tree and move only to the right, picking one fruit from each tree.
# You must stop as soon as you encounter a fruit type that doesn’t fit into either basket.

# Input: fruits = [1,2,1]
# Output: 3

# Input: fruits = [1,2,3,2,2]
# Output: 4

def totalFruit(fruits: list[int]) -> int:  # Sliding Window Approach: O(N) time | O(1) space
    left = 0
    max_fruits = 0
    fruit_count = {}

    for right in range(len(fruits)):
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1

        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

fruits = [1,2,3,2,2]
print(totalFruit(fruits))  # Output: 4