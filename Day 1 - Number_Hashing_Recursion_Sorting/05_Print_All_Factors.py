# Factors - A factor is a number that divides another without a remainder.
# input : 10
# output : 1 2 5 10

# Brute Force - time complexity O(n)
n = int(input("Enter a number : "))
res = []
for i in range(1, n//2):
    if n % i == 0:
        res.append(i)
res.append(n)
print(res)

# Optimized - time complexity O(sqrt(n))
from math import sqrt
num = int(input("Enter a number : "))
result = []
for i in range(1, int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        if i != num//i:
            result.append(num//i)
result.sort() # Optional increase time complexity by O(nlogn)
print(result)

# Optimised Explanation
# num = 36
# 1 - 36
# 2 - 18
# 3 - 12
# 4 - 9
# 6 - 6
# if divide by 1 we get 36, if by 2 we get 18 and so on, until sqrt(num)