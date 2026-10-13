'''

'''
from homework_02.problem2 import SinglyLinkedList
from homework_02.problem4 import SortedDoublyLinkedList, Node as DoublyNode

#custom implementation of Stack of Array
class StackArray:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def push(self, value):
        if self.top >= self.capacity:
            raise ValueError("Stack reached capacity")
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if (self.is_empty()):
            raise ValueError("Stack empty")
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack empty")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def __str__(self):
        return ", ".join(str(x) for x in self.stack[:self.top + 1])

#borrows implementation from homework_02\problem2.py
class StackLinkedList:
    def __init__(self):
        self.stack = SinglyLinkedList()

    def push(self, value):
        self.stack.prepend(value)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack empty")
        return self.stack.delete_at(0)

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack empty")
        return self.stack.get(0)

    def is_empty(self):
        return self.stack.count == 0

    def __str__(self):
        return linked_list_string(self.stack.head)

#borrows implementation from homework_02\problem4.py
class StackSortedDoublyLinkedList():
    def __init__(self):
        self.stack = SortedDoublyLinkedList()

    def push(self, value):
        new_node = DoublyNode(value)
        new_node.next = self.stack.head

        if self.stack.head is not None:
            self.stack.head.prev = new_node
        else:
            self.stack.tail = new_node

        self.stack.head = new_node
        self.stack.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack empty")

        value = self.stack.head.value
        old_head = self.stack.head
        self.stack.head = old_head.next

        if self.stack.head is not None:
            self.stack.head.prev = None
        else:
            self.stack.tail = None

        old_head.next = None
        self.stack.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack empty")
        return self.stack.head.value

    def is_empty(self):
        return self.stack.size == 0

    def __str__(self):
        return doubly_list_string(self.stack.tail)


#concatenate strings for printing
def linked_list_string(node):
    if node is None:
        return ""
    rest = linked_list_string(node.next)
    if rest == "":
        return str(node.value)
    return rest + ", " + str(node.value)


def doubly_list_string(node):
    if node is None:
        return ""
    rest = doubly_list_string(node.prev)
    if rest == "":
        return str(node.value)
    return rest + ", " + str(node.value)


def insert_at_bottom(stack, value):
    if stack.is_empty():
        stack.push(value)
        return

    top_value = stack.pop()
    insert_at_bottom(stack, value)
    stack.push(top_value)


def reverse_stack(stack):
    if stack.is_empty():
        return

    top_value = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top_value)


def fill_stack(stack, value=1):
    if value > 10:
        return

    stack.push(value)
    fill_stack(stack, value + 1)


def print_stack(name, stack):
    fill_stack(stack)

    print(f"\n{name}")
    print(f"Before: {stack}")

    reverse_stack(stack)

    print(f"After:  {stack}")


def main():
    print_stack("Array Stack", StackArray(10))
    print_stack("Singly Linked List Stack", StackLinkedList())
    print_stack("Doubly Linked List Stack", StackSortedDoublyLinkedList())
    

if __name__ == "__main__":
    main()