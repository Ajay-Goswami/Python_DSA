# Floyd's Cycle Detection - 
# Leetcode 141
# Given a linked list, return true if the linked list contains a cycle, else return false. 
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
# Do not modify the linked list.
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next


def hasCycle(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


print(hasCycle(head))