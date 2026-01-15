# Deque in python

from collections import deque

# Creating a deque
my_deque = deque()

# Adding elements to the deque
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

# Removing elements from the deque
print(my_deque.popleft())  # Output: 1
print(my_deque.popleft())  # Output: 2
print(my_deque)            # Output: deque([3])

# Adding elements to both ends
my_deque.appendleft(0)
my_deque.append(4)
print(my_deque)            # Output: deque([0, 3, 4])

print("Front element is:", my_deque[0])  # Accessing front element
print("Rear element is:", my_deque[-1])  # Accessing rear element

# Displaying all elements
print("Deque elements:", list(my_deque))  # Output: [0, 3, 4]
