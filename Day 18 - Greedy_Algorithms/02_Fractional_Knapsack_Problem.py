# Fractional Knapsack Problem using Greedy Algorithm

# Given two arrays, val[] and wt[] , representing the values and weights of items, and an integer capacity representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.
# Return the maximum value as a double, rounded to 6 decimal places.

# Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
# Output: 240.000000
# Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. Hence total price will be 60+100+(2/3)(120) = 240

def fractionalKnapsack(val: list[int], wt: list[int], capacity: int) -> float:
    items = []
    
    for i in range(len(val)):
        items.append((val[i] / wt[i], val[i], wt[i]))
    
    items.sort(reverse=True) # Sort by value/weight ratio (descending)
    max_value = 0.0
    
    for ratio, value, weight in items:
        if capacity == 0:
            break
        if weight <= capacity:
            max_value += value
            capacity -= weight
        else:
            max_value += ratio * capacity
            capacity = 0
    return round(max_value, 6)

val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
print(fractionalKnapsack(val, wt, capacity))