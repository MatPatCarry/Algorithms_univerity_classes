class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node()

    def appending(self, data):
        next_node = Node(data)
        if self.head is None:
            self.head = next_node
        elif self.head.data is None:
            self.head = next_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = next_node

    def show(self):
        current_node = self.head
        if current_node is None or current_node.data is None:
            return
        else:
            print(current_node.data)
        while current_node.next is not None:
            print(current_node.next.data)
            current_node = current_node.next

    def remove(self, i):
        if self.head is None:
            print("Empty list")
            return
        if i >= self.length() or i < 0:
            print("Incorrect index")
            return
        elif i == 0:
            self.head = self.head.next
            return
        current_node = self.head
        position = 1
        while current_node.next is not None:
            predecessor = current_node
            current_node = current_node.next
            if position == i:
                predecessor.next = current_node.next
                return
            position += 1

    def first_item(self):
        current_node = self.head
        if current_node is None:
            return
        self.remove(0)
        return current_node.data

    def length(self):
        current_node = self.head
        if self.head is None:
            return 0
        elif self.head.data is None:
            return 0
        index = 1
        while current_node.next is not None:
            current_node = current_node.next
            index += 1
        return index


class Knot:

    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data)

    def to_show(self):
        print(self.data)


class Stack:
    def __init__(self):
        self.head = Node()

    def length(self):
        current_node = self.head
        if self.head is None:
            return 0
        elif self.head.data is None:
            return 0
        index = 1
        while current_node.next is not None:
            current_node = current_node.next
            index += 1
        return index

    def insert(self, data):
        next_node = Node(data)
        if self.head is None:
            self.head = next_node
        elif self.head.data is None:
            self.head = next_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = next_node

    def show(self):
        current_node = self.head
        if current_node is None:
            return
        else:
            print(current_node.data)
        while current_node.next is not None:
            print(current_node.next.data)
            current_node = current_node.next

    def remove(self, i):
        if self.head is None:
            print("Empty list")
            return
        if i >= self.length() or i < 0:
            print("Incorrect index")
            return
        elif i == 0:
            self.head = self.head.next
            return
        current_node = self.head
        position = 1
        while current_node.next is not None:
            predecessor = current_node
            current_node = current_node.next
            if position == i:
                predecessor.next = current_node.next
                return
            position += 1

    def pop(self):
        current_node = self.head
        if current_node is None:
            return
        while current_node.next is not None:
            current_node = current_node.next
        self.remove(self.length()-1)
        return current_node.data



