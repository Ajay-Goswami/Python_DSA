# Find Length of Loop in LinkedList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

def Length_of_Loop(head):
    if head is None or head.next is None:
        return 0
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            curr = slow.next
            while curr != slow:
                count += 1
                curr = curr.next
            return count
    return 0  

print(Length_of_Loop(head))