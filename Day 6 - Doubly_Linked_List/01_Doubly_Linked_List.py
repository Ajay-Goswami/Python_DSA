# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Traverse (Forward)
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Insert at Start
    def insert_at_start(self, data):
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    # Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at Any Index (0-based)
    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 0

        while temp and count < index - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Index out of range")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # Delete at Start
    def delete_at_start(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Delete at End
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # Delete at Any Index (0-based)
    def delete_at_index(self, index):
        if self.head is None:
            print("List is empty")
            return

        if index == 0:
            self.delete_at_start()
            return

        temp = self.head
        count = 0

        while temp and count < index:
            temp = temp.next
            count += 1

        if temp is None:
            print("Index out of range")
            return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next


# Testing the Doubly Linked List
dll = DoublyLinkedList()

print("Insert at start:")
dll.insert_at_start(10)
dll.insert_at_start(5)
dll.traverse()

print("\nInsert at end:")
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.traverse()

print("\nInsert at index 2:")
dll.insert_at_index(2, 15)
dll.traverse()

print("\nDelete at start:")
dll.delete_at_start()
dll.traverse()

print("\nDelete at end:")
dll.delete_at_end()
dll.traverse()

print("\nDelete at index 1:")
dll.delete_at_index(1)
dll.traverse()

    
