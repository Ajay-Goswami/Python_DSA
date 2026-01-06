# Find Pairs With Given Sum in Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next
head.next.next.next = Node(5)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(6)
head.next.next.next.next.prev = head.next.next.next
head.next.next.next.next.next = Node(8)
head.next.next.next.next.next.prev = head.next.next.next.next

def find_pairs(head, target):
    if head is None:
        return []

    left = head
    right = head
    while right.next:
        right = right.next
    pairs = []

    while left != right and right.next != left:
        curr_sum = left.data + right.data
        if curr_sum == target:
            pairs.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif curr_sum < target:
            left = left.next
        else:
            right = right.prev
    return pairs


def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


print_list(head)
print(find_pairs(head, 10))