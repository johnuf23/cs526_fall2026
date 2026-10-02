Question 1:

An advantage of using a tail pointer in a linked list is that you can easily find the last node in constant time.

- If you want to append to the linked list, you can do so using the tail pointer instead of having to traverse every node.
- If you want to merge two linked lists back to back, you can get the tail pointer of the first one and the head of the second one and connect them. 
- If you wanted to make the linked list circular, you can just point the tail node to the head