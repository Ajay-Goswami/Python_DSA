# Deletion in Linked List -

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(30)
head.next.next = Node(90)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# Print Linked List
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


# Deletion at Start
def Deletion_at_Start(head):
    if head is None:
        print("Linked List is empty")
        return None
    return head.next

head = Deletion_at_Start(head)
print("After Deletion at Start", end=" ")
LinkedList_Traversal(head)


# Deletion at End
def Deletion_at_End(head):
    if head is None:
        print("Linked List is empty")
        return None
    if head.next is None:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

head = Deletion_at_End(head)
print("After Deletion at End", end=" ")
LinkedList_Traversal(head)

# Deletion at Index
def Deletion_at_Index(head, index):
    if head is None:
        print("Linked List is empty")
        return None
    if index < 0:
        print("Invalid index")
        return head
    if index == 0:
        return Deletion_at_Start(head)
    curr = head
    count = 0
    while curr and count < index - 1:
        curr = curr.next
        count += 1
    if curr is None or curr.next is None:
        print("Index out of range")
        return head
    curr.next = curr.next.next
    return head

head = Deletion_at_Index(head, 2)
print("After Deletion at Index", end=" ")
LinkedList_Traversal(head)