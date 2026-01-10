# Maximum Points You Can Obtain from Cards

# Leetcode : 1423

# Cards are placed in a row, each with some points; you can pick cards only from the start or the end.
# You must pick exactly k cards, and your score is the sum of their points.

# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12

def maxScore(cardPoints: list[int], k: int) -> int:  # Sliding Window Approach: O(N) time | O(1) space
    n = len(cardPoints)
    total_points = sum(cardPoints)
    window_size = n - k
    current_window_sum = sum(cardPoints[:window_size])
    min_window_sum = current_window_sum

    for i in range(window_size, n):
        current_window_sum += cardPoints[i] - cardPoints[i - window_size]
        min_window_sum = min(min_window_sum, current_window_sum)

    return total_points - min_window_sum

cardPoints = [1,2,3,4,5,6,1]
k = 3
print(maxScore(cardPoints, k))  # Output: 12