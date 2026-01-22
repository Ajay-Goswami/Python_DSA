# Delete all occurance of a key in Doubly Linked List

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
head.next.next.next.next = Node(30)
head.next.next.next.next.prev = head.next.next.next
head.next.next.next.next.next = Node(60)
head.next.next.next.next.next.prev = head.next.next.next.next

def delete_all_occurrence(head, key):
    curr = head

    while curr:
        # Case 1: Node to delete is head
        if curr.data == key:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                head = curr.next  # move head

            if curr.next:
                curr.next.prev = curr.prev

            curr = curr.next  # move forward safely

        else:
            curr = curr.next

    return head


def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

printList(head)
head = delete_all_occurrence(head, 30)
printList(head)