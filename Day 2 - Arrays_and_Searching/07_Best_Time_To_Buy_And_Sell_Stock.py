# Best time to buy and sell stock -
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,2,1,5,6,4,8]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 5), profit = 5-2 = 3.
# Then buy on day 4 (price = 6) and sell on day 6 (price = 8), profit = 8-6 = 2.

prices = [7, 2, 1, 5, 6, 4, 8]
# prices = [9, 8, 6, 4, 3, 2, 1]

max_profit = 0
min_price = prices[0]

for i in range(1, len(prices)):
    max_profit = max(max_profit, prices[i] - min_price)
    min_price = min(min_price, prices[i])

print(max_profit)