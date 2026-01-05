# Find the Middle of the Linked List - 
# Given a linked list, return the middle node of the linked list.
# If the number of nodes in the linked list is even, return the second middle node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(30)
head.next.next = Node(90)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)


# Tortoise and Hare Algorithm
def middleNode(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
    return slow

middle = middleNode(head)
print(middle.data)