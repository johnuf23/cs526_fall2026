'''
Problem 2: Implementation of Heap
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Min_Heap:
    def __init__(self):
        self.root = None
        self.last = 0


    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            self.last = 1
            return

        parent, direction = self.find_last_open()

        new_node.parent = parent

        if direction == "0":
            parent.left = new_node
        else:
            parent.right = new_node

        self.last += 1

        #heapify
        current = new_node

        while current.parent and current.value < current.parent.value:
            #swap values
            current.value, current.parent.value = (
                current.parent.value,
                current.value
            )
            #set current to up-swapped node
            current = current.parent


    def find_last(self, node):

        bits = bin(self.last)[2:]

        for bit in bits[1:]:
            if bit == "1":
                node = node.right
            else:
                node = node.left

            if node is None:
                return None

        return node


    def find_last_open(self):
        next_index = self.last + 1
        bits = bin(next_index)[2:]

        node = self.root

        #go to parent, skip first bc its the root
        #skip the last bit bc its the direction of insert
        for bit in bits[1:-1]:
            if bit == "1":
                node = node.right
            else:
                node = node.left

        #returns the parent, direction of insert
        return node, bits[-1]
            


        

