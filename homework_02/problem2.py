

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

#CREATE
    def append(self, value):
        new_Node = Node(value)

        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        
        self.count += 1


    def prepend(self, value):
        new_Node = Node(value)
        new_Node.next = self.head
        self.head = new_Node
        if self.count == 0:
            self.tail = new_Node
        self.count += 1


    def insert(self, index, value):
        # '>' and not '>=' because you can insert at end
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")
        
        new_Node = Node(value)

        #empty list, don't need to use count bc its accounted for in error check
        if index == 0:
            new_Node.next = self.head
            self.head = new_Node
            self.tail = new_Node
        else: #non-empty list, find node one before
            current = self.head

            for _ in range(index - 1):
                current = current.next
            new_Node.next = current.next
            current.next = new_Node

            #if insert at tail in non-empty list, update tail pointer
            if index == self.count:
                self.tail = new_Node

        self.count += 1
            

#READ
    def get(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next

        return current.value


    def find(self, value):
        if self.count == 0:
            return -1
        
        current = self.head
        position = 0
        for _ in range(self.count):
            if current.value == value:
                return position
            else:
                current = current.next
                position += 1
        return -1

    def __len__(self):
        return self.count

#UPDATE
    def update(self, index, value):
        #same '>=' as get() since we cannot go past last element
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

#DELETE
    def delete(self, value):
        #cases: deleting head, middle, tail, and deleting only node
        if self.count == 0:
            return False
        
        current = self.head
        previous = None

        while current is not None:
            if current.value == value: #found
                
                if previous is None and current.next is None: #only node
                    self.head = None
                    self.tail = None

                elif previous is None: #beginning
                    self.head = current.next

                else: #middle or tail
                    previous.next = current.next

                    if previous.next is None: #deleted tail
                        self.tail = previous

                current.next = None
                self.count -= 1
                return True
            else: 
                previous = current
                current = current.next

        return False


    def delete_at(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range or list is empty")

        current = self.head
        previous = None

        if index == 0: #at head
            self.head = current.next
            if current.next is None: #only node, set tail
                self.tail = None
            current.next = None
            self.count -= 1
            return current.value

        for _ in range(index): # iterate to node at index
            previous = current
            current = current.next

        previous.next = current.next #middle or tail
        if previous.next is None: #deleted tail
            self.tail = previous

        current.next = None
        self.count -= 1
        return current.value

#PRINT
    def print_list(self):
        if self.count == 0:
            print("empty")
            return

        current = self.head
        while current.next is not None:
            print(current.value, end=" -> ")
            current = current.next

        print(current.value)
            
