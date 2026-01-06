# Reverse Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

head = Node(10)
head.next = Node(20)
head.next.prev = head
head.next.next = Node(30)
head.next.next.prev = head.next
head.next.next.next = Node(40)
head.next.next.next.prev = head.next.next

def reverse(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        curr.prev = next
        prev = curr
        curr = next
    return prev

def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

printList(head)
head = reverse(head)
printList(head)