#C:\Users\jfice\Desktop\Education\BU\Coursework\526 DSA\Repository\homework_02

#had to change self.count to self.size because of the count method

class Node:
    def __init__(self, value=0):
        self.value = value
        self.prev = None
        self.next = None

class SortedDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        new_Node = Node(value)

        #if empty
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
            self.size += 1
            return
        #value inserted at head
        elif value <= self.head.value:
            new_Node.next = self.head
            self.head.prev = new_Node
            self.head = new_Node
            self.size += 1
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
        self.size += 1


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
            self.size -= 1
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

    def total(self):
        if self.head is None and self.tail is None:
            print(0)
            return
        sum = self.sum_helper(self.head)
        print(sum)

    def sum_helper(self, current):
        #end at last node
        if current.next is None:
            return current.value
            
        return self.sum_helper(current.next) + current.value

    def sum_middle_three(self):
        if self.size < 3:
            raise ValueError("List is fewer than three nodes")
        
        mid = self.size // 2
        current = self.head
        
        #get to mid
        for _ in range(mid):
            current = current.next

        #even/odd
        if self.size % 2 == 0:
            print(current.prev.prev.value + current.prev.value + current.value)
        else:
            print(current.prev.value + current.value + current.next.value)

        return


    def median(self):
        if self.head is None:
            raise ValueError("list is empty")

        if self.size == 1:
            print(self.head.value)
            return

        mid = self.size // 2
        current = self.head

        #get to mid
        for _ in range(mid):
            current = current.next

        #even/odd
        if self.size % 2 == 0:
            print(float((current.value + current.prev.value) / 2))
        else:
            print(current.value)

        return

    def count(self, value):
        if self.size == 0:
            print("empty list")

        c = self.count_helper(self.head, value)
        print(c)
        return
    
    def count_helper(self, current, value):
        if current is None:
            return 0

        #check node
        if current.value == value:
            return self.count_helper(current.next, value) + 1
        else:
            return self.count_helper(current.next, value)

        


        

    def print_list(self):
        if self.head is None and self.tail is None:
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
    
            