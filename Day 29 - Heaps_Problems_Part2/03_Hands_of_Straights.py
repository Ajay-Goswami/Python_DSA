# Hands of Straights

# Leetcode - 846
# Given an array of integers hand and an integer groupSize,
# return True if the hand can be rearranged into groups of size groupSize.
# Each group must consist of consecutive numbers.

# Input:  hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: True
# Explanation: Groups are [1,2,3], [2,3,4], [6,7,8]

# Input:  hand = [1,2,3,4,5], groupSize = 4
# Output: False

from collections import Counter
import heapq

hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3

# ----------------------------------------------------
# Optimal Greedy Approach using Min Heap + HashMap
# Time Complexity -> O(n log n)
# Space Complexity -> O(n)
# ----------------------------------------------------
def is_n_straight_hand(hand, groupSize):

    # If total cards cannot be divided equally
    if len(hand) % groupSize != 0:
        return False

    # Count frequency of each card
    freq = Counter(hand)

    # Min heap of all unique card values
    min_heap = list(freq.keys())
    heapq.heapify(min_heap)

    # Try forming consecutive groups
    while min_heap:
        first = min_heap[0]  # smallest available card

        # Try to form a group starting from 'first'
        for card in range(first, first + groupSize):
            if freq[card] == 0:
                return False

            freq[card] -= 1

            # Remove card from heap if exhausted
            if freq[card] == 0:
                if card != min_heap[0]:
                    return False
                heapq.heappop(min_heap)

    return True


print("Can form straight hands ->", is_n_straight_hand(hand, groupSize))