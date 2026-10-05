#C:\Users\jfice\Desktop\Education\BU\Coursework\526 DSA\Repository\homework_02

class Node:
    def __init__(self, value=0):
        self.value = value
        self.prev = None
        self.next = None

class SortedDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, value):
        new_Node = Node(value)

        #if empty
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
            self.count += 1
            return
        #value inserted at head
        elif value <= self.head.value:
            new_Node.next = self.head
            self.head.prev = new_Node
            self.head = new_Node
            self.count += 1
            return

        #find middle or tail, insert before if next is equal
        current = self.head
        while current.next is not None and current.next.value < value:
            current = current.next

        #insert between current and next
        new_Node.next = current.next
        new_Node.prev = current

        #middle or tail
        if current.next is not None:
            current.next.prev = new_Node
        else:
            self.tail = new_Node

        current.next = new_Node
        self.count += 1


    def delete(self, value):
        if self.head is None:
            print("False (empty list)")
            return
        
        current = self.exists_helper(self.head, value)

        if current:
            #deleted only node
            if current.prev is None and current.next is None:
                self.head = None
                self.tail = None
            #deleted head
            elif current.prev is None:
                self.head = current.next
                self.head.prev = None
            #deleted tail
            elif current.next is None:
                self.tail = current.prev
                self.tail.next = None
            #middle
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

            current.prev = None
            current.next = None
            self.count -= 1
            print("True")
            return
        else:
            print("False")
            return

    def exists(self, value):
        #returns bool
        if self.exists_helper(self.head, value):
            print("True")
            return
        else:
            print("False")
            return

    def exists_helper(self, current, target):
        if current.value == target:
            return current
        elif current.next is not None:
            return self.exists_helper(current.next, target)
        return False



    def print_list(self):
        if self.count == 0:
            print("empty")
            return

        self.print_helper(self.head)
        #new line
        print()

    def print_helper(self, current):
        print(current.value, end="")

        if current.next is not None:
            print(" <-> ", end="")
            self.print_helper(current.next)
    
            