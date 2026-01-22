# Reverse a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(30)
head.next.next = Node(90)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


def reverse(head):
    if head is None:
        return None
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def LinkedList_Traversal(head):
    if head is None:
        print("Linked List is empty")
        return
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

LinkedList_Traversal(head)
head = reverse(head)
LinkedList_Traversal(head)