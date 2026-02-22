# 03. Buy and Sell Stocks III
# Dynamic Programming - DP on Stocks

# Problem: You are given an array 'prices' where prices[i] is the price of a
# given stock on the ith day. Find the maximum profit you can achieve. You may
# complete at most 2 transactions. You must sell the stock before you buy again.

# Input: prices = [3, 3, 5, 0, 0, 3, 1, 4]
# Output: 6

# Explanation: Buy on day 4 (price = 0), sell on day 6 (price = 3), profit = 3.
# Buy on day 7 (price = 1), sell on day 8 (price = 4), profit = 3.
# Total profit = 3 + 3 = 6.

# Time Complexity: O(n * 2 * 3) | Space Complexity: O(1)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * 2 * 3) | Space: O(n * 2 * 3) for dp + O(n) recursion stack
# State: (index, canBuy, transactionsLeft)

def maxProfitMemo(ind, canBuy, cap, prices, n, dp):
    if ind == n or cap == 0:
        return 0
    if dp[ind][canBuy][cap] != -1:
        return dp[ind][canBuy][cap]

    if canBuy:
        pick = -prices[ind] + maxProfitMemo(ind + 1, 0, cap, prices, n, dp)
        notPick = maxProfitMemo(ind + 1, 1, cap, prices, n, dp)
        dp[ind][canBuy][cap] = max(pick, notPick)
    else:
        sell = prices[ind] + maxProfitMemo(ind + 1, 1, cap - 1, prices, n, dp)
        notSell = maxProfitMemo(ind + 1, 0, cap, prices, n, dp)
        dp[ind][canBuy][cap] = max(sell, notSell)

    return dp[ind][canBuy][cap]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * 2 * 3) | Space: O(n * 2 * 3)

def maxProfitTabulation(prices, n):
    dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

    # Base cases are already 0 (when ind == n or cap == 0)

    for ind in range(n - 1, -1, -1):
        for canBuy in range(2):
            for cap in range(1, 3):
                if canBuy:
                    pick = -prices[ind] + dp[ind + 1][0][cap]
                    notPick = dp[ind + 1][1][cap]
                    dp[ind][canBuy][cap] = max(pick, notPick)
                else:
                    sell = prices[ind] + dp[ind + 1][1][cap - 1]
                    notSell = dp[ind + 1][0][cap]
                    dp[ind][canBuy][cap] = max(sell, notSell)

    return dp[0][1][2]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n * 2 * 3) | Space: O(1)

def maxProfitOptimized(prices, n):
    ahead = [[0] * 3 for _ in range(2)]
    curr = [[0] * 3 for _ in range(2)]

    for ind in range(n - 1, -1, -1):
        for canBuy in range(2):
            for cap in range(1, 3):
                if canBuy:
                    pick = -prices[ind] + ahead[0][cap]
                    notPick = ahead[1][cap]
                    curr[canBuy][cap] = max(pick, notPick)
                else:
                    sell = prices[ind] + ahead[1][cap - 1]
                    notSell = ahead[0][cap]
                    curr[canBuy][cap] = max(sell, notSell)

        ahead = [row[:] for row in curr]

    return ahead[1][2]


prices = [3, 3, 5, 0, 0, 3, 1, 4]
n = len(prices)

# Memoization
dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]
print(f"Memoization: {maxProfitMemo(0, 1, 2, prices, n, dp)}")

# Tabulation
print(f"Tabulation: {maxProfitTabulation(prices, n)}")

# Space Optimized
print(f"Space Optimized: {maxProfitOptimized(prices, n)}")
