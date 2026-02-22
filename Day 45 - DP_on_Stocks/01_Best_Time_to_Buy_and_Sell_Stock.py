# 01. Best Time to Buy and Sell Stock
# Dynamic Programming - DP on Stocks

# Problem: You are given an array 'prices' where prices[i] is the price of a
# given stock on the ith day. You want to maximize your profit by choosing a
# single day to buy and a single day to sell. You can only hold one share at a
# time and must buy before selling. Return the maximum profit. If no profit
# is possible, return 0.

# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5

# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6).
# Profit = 6 - 1 = 5.

# Time Complexity: O(n) | Space Complexity: O(1)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * 2) | Space: O(n * 2) for dp + O(n) recursion stack
# State: (index, canBuy) where canBuy = 1 means we can buy, 0 means we must sell
# Only 1 transaction allowed, so once we sell, we stop.

def maxProfitMemo(ind, canBuy, prices, n, dp):
    if ind == n:
        return 0
    if dp[ind][canBuy] != -1:
        return dp[ind][canBuy]

    if canBuy:
        pick = -prices[ind] + maxProfitMemo(ind + 1, 0, prices, n, dp)
        notPick = maxProfitMemo(ind + 1, 1, prices, n, dp)
        dp[ind][canBuy] = max(pick, notPick)
    else:
        sell = prices[ind]  # Sell and stop (only 1 transaction)
        notSell = maxProfitMemo(ind + 1, 0, prices, n, dp)
        dp[ind][canBuy] = max(sell, notSell)

    return dp[ind][canBuy]


# ---- Approach 2: Tabulation (Bottom-Up) ----
# Time: O(n * 2) | Space: O(n * 2)

def maxProfitTabulation(prices, n):
    dp = [[0] * 2 for _ in range(n + 1)]

    # Base case: dp[n][0] = 0, dp[n][1] = 0 (already initialized)

    for ind in range(n - 1, -1, -1):
        for canBuy in range(2):
            if canBuy:
                pick = -prices[ind] + dp[ind + 1][0]
                notPick = dp[ind + 1][1]
                dp[ind][canBuy] = max(pick, notPick)
            else:
                sell = prices[ind]  # Sell and stop
                notSell = dp[ind + 1][0]
                dp[ind][canBuy] = max(sell, notSell)

    return dp[0][1]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n) | Space: O(1)
# Simple greedy: track the minimum price seen so far and compute max profit.

def maxProfitOptimized(prices, n):
    minPrice = float('inf')
    maxProfit = 0

    for i in range(n):
        minPrice = min(minPrice, prices[i])
        maxProfit = max(maxProfit, prices[i] - minPrice)

    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
n = len(prices)

# Memoization
dp = [[-1] * 2 for _ in range(n)]
print(f"Memoization: {maxProfitMemo(0, 1, prices, n, dp)}")

# Tabulation
print(f"Tabulation: {maxProfitTabulation(prices, n)}")

# Space Optimized
print(f"Space Optimized: {maxProfitOptimized(prices, n)}")
