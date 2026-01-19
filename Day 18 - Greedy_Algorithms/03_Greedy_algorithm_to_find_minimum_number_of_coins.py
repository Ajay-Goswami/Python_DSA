# Greedy Algorithm to Find Minimum Number of Coins

# Problem:
# You are given a value (amount) and an array of coin denominations. You need to find the minimum number of coins required to make that amount. You can use unlimited coins of each denomination.

# Note: This greedy approach works correctly when the coin system is canonical (like Indian or US currency).

# Input: coins = [1, 2, 5, 10, 20, 50, 100, 500]  amount = 93
# Output: Minimum coins required = 5
# Coins used = [50, 20, 20, 2, 1]

def minCoins(coins, amount):
    # Sort coins in descending order (greedy choice)
    coins.sort(reverse=True)
    
    used_coins = []
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            used_coins.append(coin)
    
    return len(used_coins), used_coins


coins = [1, 2, 5, 10, 20, 50, 100, 500]
amount = 93

count, used = minCoins(coins, amount)

print("Minimum coins required:", count)
print("Coins used:", used)
