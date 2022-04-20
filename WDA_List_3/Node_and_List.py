class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = Node()

    def appending(self, data):
        next_node = Node(data)
        if self.head.data is None:
            self.head = next_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = next_node

    def show(self):
        current_node = self.head
        print(current_node.data)
        while current_node.next is not None:
            print(current_node.next.data)
            current_node = current_node.next

    def first_item(self):
        current_node = self.head
        if current_node is None:
            return
        return current_node.data

    def correct_type(self, item):
        current_node = self.head
        index = 0

        if current_node is None:
            return None
        while True:

            test = current_node.data
            if item == test[0]:
                return test[1], index

            else:
                if current_node.next is not None:
                    current_node = current_node.next
                    index += 1
                else:
                    return None

    def length(self):
        current_node = self.head
        if self.head is None:
            return 0
        index = 1
        while current_node.next is not None:
            current_node = current_node.next
            index += 1
        return index

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


