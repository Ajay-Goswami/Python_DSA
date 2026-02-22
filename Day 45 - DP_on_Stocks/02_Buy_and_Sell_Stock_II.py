# 02. Buy and Sell Stock II
# Dynamic Programming - DP on Stocks

# Problem: You are given an array 'prices' where prices[i] is the price of a
# given stock on the ith day. You may complete as many transactions as you like
# (buy and sell multiple times). However, you can only hold one share at a time
# (must sell before buying again). Return the maximum profit.

# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 7

# Explanation: Buy on day 2 (price = 1), sell on day 3 (price = 5), profit = 4.
# Buy on day 4 (price = 3), sell on day 5 (price = 6), profit = 3.
# Total profit = 4 + 3 = 7.

# Time Complexity: O(n * 2) | Space Complexity: O(1)


# ---- Approach 1: Recursion + Memoization (Top-Down) ----
# Time: O(n * 2) | Space: O(n * 2) for dp + O(n) recursion stack

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
        sell = prices[ind] + maxProfitMemo(ind + 1, 1, prices, n, dp)
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
                sell = prices[ind] + dp[ind + 1][1]
                notSell = dp[ind + 1][0]
                dp[ind][canBuy] = max(sell, notSell)

    return dp[0][1]


# ---- Approach 3: Space Optimized (Best) ----
# Time: O(n) | Space: O(1)

def maxProfitOptimized(prices, n):
    aheadNotBuy = 0  # ahead[0]
    aheadBuy = 0     # ahead[1]

    for ind in range(n - 1, -1, -1):
        currNotBuy = max(prices[ind] + aheadBuy, aheadNotBuy)
        currBuy = max(-prices[ind] + aheadNotBuy, aheadBuy)

        aheadNotBuy = currNotBuy
        aheadBuy = currBuy

    return aheadBuy


prices = [7, 1, 5, 3, 6, 4]
n = len(prices)

# Memoization
dp = [[-1] * 2 for _ in range(n)]
print(f"Memoization: {maxProfitMemo(0, 1, prices, n, dp)}")

# Tabulation
print(f"Tabulation: {maxProfitTabulation(prices, n)}")

# Space Optimized
print(f"Space Optimized: {maxProfitOptimized(prices, n)}")
