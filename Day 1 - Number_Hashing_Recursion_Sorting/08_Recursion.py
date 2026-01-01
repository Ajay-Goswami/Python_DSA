# Recursion - AA recursive function is a function that solves a problem by calling itself on smaller subproblems until a base condition is met.
# Stack Memory - Stack memory stores function calls, local variables, parameters, and return addresses during program execution. 
# Stack overflow in recursion - A stack overflow occurs when the recursion depth exceeds the limit of the stack.

# Recursion types - 
# 1. Tail recursion - A recursive function where the recursive call is the last operation in the function.
# 2. Non-tail recursion - A recursive function where some work is done after the recursive call returns.


# Ques - Factorial - The factorial of a number is the product of all positive integers less than or equal to that number.
#Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

# Tail recursion - time complexity O(n)
# Space complexity O(n) (because Python has no tail-call optimization)
def tail_fact(n, acc=1):
    if n == 0 or n == 1:
        return acc
    return tail_fact(n-1, acc*n) # why - Recursive call is the last statement

print(tail_fact(5))

# Non-tail recursion - time complexity O(n)
def non_tail_fact(n):
    if n == 0 or n == 1:
        return 1
    return n * non_tail_fact(n-1) # why - After the recursive call returns, we still do n * result

print(non_tail_fact(5))





# Fibonacci series - The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding numbers.
# input : 8
# output : 0 1 1 2 3 5 8 13 = 13


# Tail recursion - time complexity O(n)
def fibonacci_tail(n, a=0, b=1):
    if n == 0:
        return a
    return fibonacci_tail(n - 1, b, a + b) # why - Recursive call is the last statement
print(fibonacci_tail(8))


# Non-tail recursion - time complexity O(2^n)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) # why - Addition happens after recursion returns
print(fibonacci(8))


# Best Approach - Iterative approach - time complexity O(n)
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(fibonacci_iter(8))