# Leetcode - 19

# Input : 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 , n=2
# Output : 1 -> 2 -> 3 -> 4 -> 6 -> 7

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)

def removeNthFromEnd(head, n):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head
    for _ in range(n):
        fast = fast.next
    if fast is None:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head


removeNthFromEnd(head, 2)
