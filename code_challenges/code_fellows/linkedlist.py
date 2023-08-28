class LinkedList():
    def __init__(self, values=None):
        self.head = None
        if values:
            for value in values:
                value = Node(value, self.head)


class Node():
    def __init__(self, value, next):
        self.next = next
        self.value = value

