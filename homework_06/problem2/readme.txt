Introduction:

This problem is an implementation of a min heap using a binary tree of linked nodes, with methods to insert, extract the minimum, delete, peek, sort, and print the heap.


Algorithm:

Insert Method:
- The heap is always a complete binary tree, so a new node always goes in the next open spot on the bottom level. If the heap is empty, the new node becomes the root. 
Otherwise, I find the parent of the open spot and attach the new node as its left or right child. Then I swap the new value up the tree with its parent until the parent is smaller, 
which restores the heap order.

Peek Method:
- Simply returns the root and raises an error if the heap is empty

Extract Min Method:
- The minimum is always the root. To remove it, I take the value of the last node in the tree and put it in the root, then detach that last node, which keeps the tree complete. 
The new root might be too big, so I swap it down with its smaller child until neither child is smaller than it.

Delete Method:
- This method deletes any value in the heap. It first searches level by level for a node with that value, skipping any subtree whose root is already larger than the target, 
since everything below it must be larger too. If the value isn't found, it returns False.
- Once found, it works like extract min: the last node's value replaces the target's value and the last node is detached. The moved value then gets swapped down if it's too big. 
It also has to be able to swap up, since the last node can come from a different branch and be smaller than the target's parent.

Build Method:
- This method just takes each input value and calls insert() on each

Heap Sort Method:
- To print the values in order without changing the heap, I read the nodes level by level into a temporary array, which gives the standard array layout of a heap. 
Then I repeatedly take the first element, move the last element to the front, and sift it down in the array. The values come out in sorted order, and the real tree is never touched. 


Code & Interesting Aspects:

The heap takes a verbose option. When it is on, every insert prints the heap afterward, which I used to check the tree while building it. Problems 1 and 3 turn it off.
I decided not to use the is_empty() function on methods that check first if the heap is empty, since
I wanted the is_empty() function its own to be able to print out True or False, and I didn't
want a bunch of unnecessary True and Falses in my outputs

How to Run:

To run this program, download all the files from the homework_06 into the same directory, then from inside the problem2 folder in command prompt run any of the following:

python3 problem2.py < input_files/heap_input1.txt
python3 problem2.py < input_files/heap_input2.txt
python3 problem2.py < input_files/heap_input3.txt
python3 problem2.py < input_files/heap_input4.txt
python3 problem2.py < input_files/heap_input5.txt
python3 problem2.py < input_files/heap_input6.txt
python3 problem2.py < input_files/heap_input7.txt
python3 problem2.py < input_files/heap_input8.txt
python3 problem2.py < input_files/heap_input9.txt
python3 problem2.py < input_files/heap_input10.txt
