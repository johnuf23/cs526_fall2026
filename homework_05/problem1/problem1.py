'''
Problem 1: Implementation of a Binary Tree
'''
import random

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

    
    #3 Cases: root has no children, 1 child, or 2 children
    def delete_node(self, root, value):
        if root is None:
            print(f"{value} not deleted because {value} not in tree!")
            return None

        if root.value < value:
            root.right = self.delete_node(root.right, value)
        elif root.value > value:
            root.left = self.delete_node(root.left, value)
        #if node found, root is now the Target
        else:
            #0 children or 1 child:
            if root.left is None:
                print(f"deleting: {value}")
                return root.right
            elif root.right is None:
                print(f"deleting: {value}")
                return root.left
            #if both are none, will return None

            #two children
            successor = self.find_successor(root.right)
            root.value = successor.value
            root.right = self.delete_node(root.right, successor.value)

        return root
    
    #helper to find successor for delete_node, finds min value in right subtree
    #use on the right child of the root
    def find_successor(self, root):
        while root.left is not None:
            root = root.left
        return root            


    def find_node(self, root, value):
        if root is None:
            print(f"No node of value {value} found")
            return None
        if root.value == value:
            print(f"Node of value {value} found!")
            return root
        if root.value < value:
            return self.find_node(root.right, value)
        #else
        return self.find_node(root.left, value)
        

    #prints in order
    def print_tree(self, root):
        if root:
            self.print_tree(root.left)
            print(root.value, end=" ")
            self.print_tree(root.right)


    def populate_tree(self, value):
        print(f"Generating initial input set of size {value + 1}...")
        iteration = 0
        while iteration <= value:
            self.add_node(self.root, random.randint(1,1000))
            iteration+=1

def main():
    r = random.randint(1, 1000)
    root = Node(r)
    bst = BinarySearchTree(root)
    print(f"Creating Binary Search Tree with original root of {r}")
    bst.populate_tree(random.randint(4,50)) #4 as min because root already 1

    bst.print_tree(bst.root)

    #generate new value to add
    n = 1001
    bst.add_node(bst.root, n)
    print()
    print("adding value: ", n)
    bst.print_tree(bst.root)
    print()

    bst.delete_node(bst.root, n)
    bst.print_tree(bst.root)
    print()

    find = random.randint(1, 1000)
    print("Generated random int: ", find)
    bst.find_node(bst.root, find)

    find2 = random.randint(1, 1000)
    print("Generated random int: ", find2)
    bst.find_node(bst.root, find2)
    


if __name__ == "__main__":
    main()