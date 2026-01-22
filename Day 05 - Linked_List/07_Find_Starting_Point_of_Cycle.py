# Leetcode 142
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next


def detectCycle(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head
    while fast and fast.next: # Phase 1: Detect cycle
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Phase 2: Find cycle entry
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow



print(detectCycle(head).val)
