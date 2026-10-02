

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value):
        new_Node = Node(value)
        
        self.tail = new_Node
        self.count += 1
        