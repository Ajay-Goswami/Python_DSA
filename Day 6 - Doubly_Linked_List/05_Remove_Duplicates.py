# Remove Duplicates from Unsorted Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Create DLL: 10 <-> 20 <-> 10 <-> 30 <-> 20 <-> 40
head = Node(10)
head.next = Node(20)
head.next.prev = head
head.next.next = Node(10)
head.next.next.prev = head.next
head.next.next.next = Node(30)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(20)
head.next.next.next.next.prev = head.next.next.next
head.next.next.next.next.next = Node(40)
head.next.next.next.next.next.prev = head.next.next.next.next

def remove_duplicates(head):
    if head is None:
        return None
    seen = set()
    curr = head
    while curr:
        if curr.data in seen:
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            curr = curr.next
        else:
            seen.add(curr.data)
            curr = curr.next
    return head

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

print_list(head)
head = remove_duplicates(head)
print_list(head)
