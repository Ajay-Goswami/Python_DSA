# Insertion in Linked List

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


# Insertion in Start
def Insertion_at_Start(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode

head = Insertion_at_Start(head, 20)
print("After Insertion at Start", end=" ")
LinkedList_Traversal(head)


# Insertion at End
def Insertion_at_End(head, data):
    newNode = Node(data)
    if head is None:
        return newNode
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = newNode
    return head

head = Insertion_at_End(head, 100)
print("After Insertion at End", end=" ")
LinkedList_Traversal(head)

# Insertion at Index
def Insertion_at_Index(head, index, data):
    if index < 0:
        print("Invalid index")
        return head
    if index == 0:
        return Insertion_at_Start(head, data)
    curr = head
    count = 0
    while curr and count < index - 1:
        curr = curr.next
        count += 1
    if curr is None:
        print("Index out of range")
        return head
    newNode = Node(data)
    newNode.next = curr.next
    curr.next = newNode
    return head


head = Insertion_at_Index(head, 3, 60)
print("After Insertion at Index", end=" ")
LinkedList_Traversal(head)