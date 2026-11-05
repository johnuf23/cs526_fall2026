'''
Problem 1: Implementation of a Binary Tree
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        


    def add_node(self, root, value):
        if root is None:
            return Node(value) #create node at that location
        if root.value == value:
            return root
        if root.value < value:
            root.right = self.add_node(root.right, value)
        else:
            root.left = self.add_node(root.left, value)
        return root

    def print_tree(self, root):
        if root:
            print(root.value, end=" ")
            self.print_tree(root.left)
            self.print_tree(root.right)

def main():
    r = int(input("Insert integer for root value: "))

    root = Node(r)
    bst = BinarySearchTree(root)
    bst.add_node(root, 15)
    bst.add_node(root, 12)
    bst.print_tree(root)

if __name__ == "__main__":
    main()