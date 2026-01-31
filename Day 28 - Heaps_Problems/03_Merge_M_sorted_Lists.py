# Merge M Sorted Lists
# Leetcode - 23
# Given an array of m sorted linked lists, merge them into one sorted linked list.

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper function to convert Python list to Linked List
def build_linked_list(arr):
    dummy = ListNode(-1)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


# Helper function to convert Linked List to Python list
def linked_list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


lists = [
    build_linked_list([1, 4, 5]),
    build_linked_list([1, 3, 4]),
    build_linked_list([2, 6])
]


import heapq

# Optimized Solution Using Min Heap
# Time Complexity -> O(N log M)
# Space Complexity -> O(M)
# N = total number of nodes, M = number of lists
def merge_m_sorted_lists(lists):
    min_heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i].val, i, lists[i]))

    dummy = ListNode(-1)
    curr = dummy

    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next


merged_head = merge_m_sorted_lists(lists)
print("Merged Sorted List ->", linked_list_to_array(merged_head))