# Linked List - A linear data structure that consists of a series of connected nodes.
# Each node contains a value and a reference to the next node in the list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10) # O(1)
head.next = Node(20) # O(1)
head.next.next = Node(30) # O(1)

print(head.data)
print(head.next.data)
print(head.next.next.data)

def LinkedList_Traversal(head): # O(n)
    while head:
        print(head.data)
        head = head.next

LinkedList_Traversal(head)