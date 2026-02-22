# 04. Buy and Sell Stock IV
# Dynamic Programming - DP on Stocks

# Problem: You are given an integer k and an array 'prices' where prices[i] is
# the price of a given stock on the ith day. Find the maximum profit you can
# achieve. You may complete at most k transactions. You must sell the stock
# before you buy again.

# Input: k = 2, prices = [3, 2, 6, 5, 0, 3]
# Output: 7

# Explanation: Buy on day 2 (price = 2), sell on day 3 (price = 6), profit = 4.
# Buy on day 5 (price = 0), sell on day 6 (price = 3), profit = 3.
# Total profit = 4 + 3 = 7.

# Time Complexity: O(n * 2 * (k+1)) | Space Complexity: O(1)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * 2 * (k+1)) | Space: O(n * 2 * (k+1)) for dp + O(n) recursion stack
# State: (index, canBuy, transactionsLeft)

def maxProfitMemo(ind, canBuy, cap, prices, n, k, dp):
    if ind == n or cap == 0:
        return 0
    if dp[ind][canBuy][cap] != -1:
        return dp[ind][canBuy][cap]

    if canBuy:
        pick = -prices[ind] + maxProfitMemo(ind + 1, 0, cap, prices, n, k, dp)
        notPick = maxProfitMemo(ind + 1, 1, cap, prices, n, k, dp)
        dp[ind][canBuy][cap] = max(pick, notPick)
    else:
        sell = prices[ind] + maxProfitMemo(ind + 1, 1, cap - 1, prices, n, k, dp)
        notSell = maxProfitMemo(ind + 1, 0, cap, prices, n, k, dp)
        dp[ind][canBuy][cap] = max(sell, notSell)

    return dp[ind][canBuy][cap]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * 2 * (k+1)) | Space: O(n * 2 * (k+1))

def maxProfitTabulation(prices, n, k):
    dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]

    # Base cases are already 0 (when ind == n or cap == 0)

    for ind in range(n - 1, -1, -1):
        for canBuy in range(2):
            for cap in range(1, k + 1):
                if canBuy:
                    pick = -prices[ind] + dp[ind + 1][0][cap]
                    notPick = dp[ind + 1][1][cap]
                    dp[ind][canBuy][cap] = max(pick, notPick)
                else:
                    sell = prices[ind] + dp[ind + 1][1][cap - 1]
                    notSell = dp[ind + 1][0][cap]
                    dp[ind][canBuy][cap] = max(sell, notSell)

    return dp[0][1][k]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n * 2 * (k+1)) | Space: O(k)

def maxProfitOptimized(prices, n, k):
    ahead = [[0] * (k + 1) for _ in range(2)]
    curr = [[0] * (k + 1) for _ in range(2)]

    for ind in range(n - 1, -1, -1):
        for canBuy in range(2):
            for cap in range(1, k + 1):
                if canBuy:
                    pick = -prices[ind] + ahead[0][cap]
                    notPick = ahead[1][cap]
                    curr[canBuy][cap] = max(pick, notPick)
                else:
                    sell = prices[ind] + ahead[1][cap - 1]
                    notSell = ahead[0][cap]
                    curr[canBuy][cap] = max(sell, notSell)

        ahead = [row[:] for row in curr]

    return ahead[1][k]


k = 2
prices = [3, 2, 6, 5, 0, 3]
n = len(prices)

# Memoization
dp = [[[-1] * (k + 1) for _ in range(2)] for _ in range(n)]
print(f"Memoization: {maxProfitMemo(0, 1, k, prices, n, k, dp)}")

# Tabulation
print(f"Tabulation: {maxProfitTabulation(prices, n, k)}")

# Space Optimized
print(f"Space Optimized: {maxProfitOptimized(prices, n, k)}")
