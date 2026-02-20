# 01. Ninja's Training
# Dynamic Programming - 2D DP

# Problem: A ninja has to train for N days. Each day he can perform one of 3 activities
# (activity 0, 1, or 2). Each activity has some merit points on each day.
# The ninja cannot perform the same activity on two consecutive days.
# Find the maximum merit points the ninja can earn in N days.

# Input: points = [[10, 40, 70],
#                  [20, 50, 80],
#                  [30, 60, 90]]
# Output: 210

# Explanation: Day 0 -> activity 2 (70 points)
#   Day 1 -> activity 1 (50 points)
#   Day 2 -> activity 2 (90 points)
#   Total = 70 + 50 + 90 = 210.
#   We can't pick activity 2 on both day 1 and day 2? Actually we can here because
#   day 0 picked 2, day 1 picked 1 (different), day 2 picked 2 (different from day 1).

# Time Complexity: O(n * 4 * 3) ~ O(n) | Space Complexity: O(1)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * 4 * 3) | Space: O(n * 4) for dp + O(n) recursion stack

def ninjaMemo(day, last, points, dp):
    if day == 0:
        # On day 0, pick the best activity that is not the same as 'last'
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])
        return maxi

    if dp[day][last] != -1:
        return dp[day][last]

    maxi = 0
    for task in range(3):
        if task != last:
            merit = points[day][task] + ninjaMemo(day - 1, task, points, dp)
            maxi = max(maxi, merit)

    dp[day][last] = maxi
    return dp[day][last]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * 4 * 3) | Space: O(n * 4)

def ninjaTabulation(n, points):
    dp = [[0] * 4 for _ in range(n)]

    # Base case: day 0
    # dp[0][last] = max points on day 0 when 'last' activity is excluded
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    merit = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], merit)

    return dp[n - 1][3]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n * 4 * 3) | Space: O(1) basically just O(4) prev array

def ninjaTraining(n, points):
    prev = [0] * 4

    # Base case: day 0
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        curr = [0] * 4
        for last in range(4):
            curr[last] = 0
            for task in range(3):
                if task != last:
                    merit = points[day][task] + prev[task]
                    curr[last] = max(curr[last], merit)
        prev = curr

    return prev[3]


points = [[10, 40, 70],
          [20, 50, 80],
          [30, 60, 90]]
n = len(points)

# Memoization
dp = [[-1] * 4 for _ in range(n)]
print(f"Memoization: {ninjaMemo(n - 1, 3, points, dp)}")

# Tabulation
print(f"Tabulation: {ninjaTabulation(n, points)}")

# Space Optimized
print(f"Space Optimized: {ninjaTraining(n, points)}")
