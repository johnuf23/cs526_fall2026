# Homework2 ReadMe:



## Problem 1:



An advantage of using a tail pointer in a linked list is that you can easily find the last node in constant time.



\- If you want to append to the linked list, you can do so using the tail pointer instead of having to traverse every node.

\- If you want to merge two linked lists back to back, you can get the tail pointer of the first one and the head of the second one and connect them.

\- If you wanted to make the linked list circular, you can just point the tail node to the head





## Introduction:

This homework asks to implement a custom version of a singly-linked list and a sorted doubly-linked list (problems 2 and 4 respectively). Question 3 asks to create a recursive solution to finding the number of ways there are to climb to the stop of a set of stairs when the possible steps to take are 1, 2, and 3.



Problems 2 and 4 each have standard Create Read Update and Delete methods and each implement their own version of a Node. Each of these problems can be executed using the driver files, which will have instructions for use in the "How to run" section below.



The problem2Resources folder has all the test files from Blackboard



Open the OutputExample\_AllCommands.png to see an example of my output code with a custom text file that has all the methods from problem 4



## Algorithm:

### Problem 2:

* append() adds a node to the end of the list. It first checks if the head is None, in which case it will set both the head and tail of the list to that Node, and if not the it will just update the tail.
* prepend() operates similarly to append() but will automatically set itself to the head by definition. If the head is the only node, it also sets the tail to the new Node.
* insert(index, value) inserts a new node at a specific index. It first checks that the index is valid. Since you can insert a new node at the end of the list, the index can be equal to the current count, but cannot be greater than it. If the index is 0, it inserts the node at the head. Otherwise, it traverses the list to find the node immediately before the desired index and connects the new node between the previous node and the node currently at that index. If the new node is being inserted at the end, the tail is updated to point to the new node.
* get(index) returns the value of the node at a specific index. It first checks that the index is valid, then starts at the head and traverses the list until it reaches the requested index. It then returns the value stored in that node.
* find(value) searches the list for a specific value. It starts at the head and checks each node while keeping track of its position. If it finds the value, it returns the index of that node. If the value is not found, it returns -1.
* \_\_len\_\_() allows the list to be used with Python's built-in len() function. It simply returns the current count of nodes in the list.
* update(index, value) changes the value stored at a specific index. It first checks that the index is valid, then traverses the list until it reaches that index and replaces the node's current value with the new value.
* delete(value) searches for the first node containing the specified value and removes it from the list. It keeps track of both the current node and the previous node so that it can reconnect the list after removing the current node. It handles deleting the only node, the head, a middle node, and the tail. If the value is found, it decreases the count and returns True. If the value is not found or the list is empty, it returns False.
* delete\_at(index) removes the node at a specific index. It first checks that the index is valid. If the index is 0, it removes the head and updates the tail if it was the only node. Otherwise, it traverses to the requested index while keeping track of the previous node. It then connects the previous node to the node after the one being deleted. If the deleted node was the tail, it updates the tail pointer. Finally, it decreases the count and returns the value that was deleted.
* print\_list() prints the values of the nodes in order. If the list is empty, it prints "empty". Otherwise, it starts at the head and traverses the list, printing each value followed by " -> " until it reaches the last node.



### Problem 3:

* This recursive function begins from the top of the stairs and counts the number of ways to reach the top from the previous steps, if there are any. The base case is that there is one way to get to the top if you are already standing on the top step (by doing nothing). If there is only one step total, the n-1 step will have one way. For a staircase of n=2 steps, you can take one step to the n-1 step or take two steps, for a total of 2 ways. The important things to note is that while standing on the n-1 step (if calculating staircase of n > 1 steps), we have already calculated the ways to get to the top, so we can just add that value to the new ways. Therefore, a staircase of three steps will have four ways (1 + 1 + 2). We can then see that the pattern is that the ways = the ways(n-1) + ways(n-2) + ways(n-3).



### Problem 4:

* Problem 4 uses recursive helpers with my methods.
* add(value) adds a new node to the list while keeping the values in ascending order. If the list is empty, the new node becomes both the head and tail. If the value is less than or equal to the current head, the new node is inserted before the head and becomes the new head. Otherwise, the method traverses the list until it finds the correct position. It then connects the new node to both the previous and next nodes using the prev and next pointers. If the node is added to the end of the list, the tail is updated.
* delete(value) searches for the first node containing the specified value and removes it from the list. It uses exists\_helper() to find the node. Once the node is found, it handles four cases: deleting the only node, deleting the head, deleting the tail, or deleting a node from the middle. Both the prev and next pointers need to be updated when deleting a middle node. After removing the node, its pointers are set to None, the size is decreased, and True is printed. If the value is not found, False is printed.
* exists(value) checks whether a value exists in the list. It calls exists\_helper() to search through the nodes. If the helper finds the value, it returns the node and exists() prints True. Otherwise, it prints False.
* exists\_helper(current, target) recursively searches through the list for a node containing the target value. It first checks the current node. If the value matches, it returns the current node. If it does not match and there is another node, it recursively checks the next node. If it reaches the end without finding the target, it returns False.
* total() calculates and prints the sum of all the values in the list. If the list is empty, it prints 0. Otherwise, it calls sum\_helper() starting at the head of the list.
* sum\_helper(current) recursively calculates the sum of the values in the list. When it reaches the last node, it returns that node's value. Otherwise, it recursively calculates the sum of the remaining nodes and adds the current node's value to the result.
* sum\_middle\_three() calculates and prints the sum of the three middle nodes. It first checks that the list contains at least three nodes. It uses integer division to find the middle position and traverses to that position. If the list has an even number of nodes, it adds the current node and the two nodes before it. If the list has an odd number of nodes, it adds the current node, the node before it, and the node after it.
* median() calculates and prints the median value of the sorted list. If the list is empty, it raises an error. If there is only one node, that node's value is the median. Otherwise, it traverses to the middle of the list. If the list has an odd number of nodes, it prints the middle value. If the list has an even number of nodes, it takes the two middle values and calculates their average.
* count(value) counts how many nodes contain a specified value. If the list is empty, it prints "empty". Otherwise, it calls count\_helper() starting at the head and prints the number returned by the helper.
* count\_helper(current, value) recursively checks each node to see if its value matches the specified value. If current is None, it has reached the end of the list and returns 0. If the current node contains the target value, it recursively checks the rest of the list and adds 1 to the result. If it does not match, it simply returns the count from the remaining nodes.
* print\_list() prints the values in the list from the head to the tail. If the list is empty, it prints "empty". Otherwise, it calls print\_helper() starting at the head and then prints a new line after all the nodes have been printed.
* print\_helper(current) recursively prints each node's value. If there is another node after the current one, it prints " <-> " and recursively moves to the next node. This produces the doubly-linked list format showing the connection between each node.



## Interesting Aspects:

* For the driver for problem 2, I wanted to account for the case where the command had an unexpected number of arguments, so I created a dictionary with each command's name and how many arguments it should expect. That way I could not only check for arguments but also if the command was a valid command in the first place, after splitting the text line with parts = line.split(). The command should be the part at index 0 and the arguments should be everything after, denoted by parts\[1:]
* My stair climbing recursive function does not necessarily account for stairs of negative numbers, but it will just return 1 in those cases. I think this theoretically works, although perhaps not useful in this universe
* For problem 4, I had to change self.count to self.size because the assignment called for creating a count method. For the driver, I realized I had to account for floating values as input because otherwise it wouldn't work with sdll.add(int(args\[0])). So I created a new helper method for parsing the number and returning an int or a float.
* In problem 4, I decided to reuse recursive helper methods that could do similar things for different methods. I used the exists\_helper to parse for the exists method and the delete method, since they both use the same type of parsing. I originally made the exists\_helper just return a bool always, but in order to get it to work with both methods I had it return the current node. delete could use the node to check the previous and next nodes while exists could just do if(value) for a simple "True" return.



## How To Run:

* Download all files in homework\_02 to a directory of your choice on your machine. Open command prompt, navigate to the directory that homework\_02 exists in, and use the following examples:

  * python3 problem2\_driver.py < problem2Resources/problem2\_basic.txt
  * python3 problem4\_driver.py < problem2Resources/problem4\_simple.txt
* For problem3, you can just run the file directly without a driver:

  * python3 problem3.py

