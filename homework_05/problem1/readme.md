Introduction:

This problem is an implementation of a binary tree with methods to add, delete, find, and print the nodes


Algorithm:

Add Node Method:
- This method in the BinarySearchTree class works recursively. It takes the root of the BST and a value as parameters and its base case is when the root is none. Then it checks if the root's value is the one we're looking for, in which case it will return the root. Otherwise, we check if the root's value is greater than or less than the target, and recurse appropriately.

Delete Node Method:
- This method takes the same parameters as add_node and also has a base case of when the root is None. It uses the same logic as the add_node to recursively find the value in question. Once the target is found, there are three cases to take into consideration:
- First: the node to delete has no children. In this case its simple, and we can just delete that node (return None)
- Second: if there's only one child, we can remove the node and assign its child to the node's parent.
- Third: if there are two children, we need to get the successor of the node. In my algorithm, I chose to find the least value on the right subtree of the node, using the find_successor helper method to get the smallest value. Once we get that node, we swap it with the node, and the tree will maintain the binary search tree order.

Find Node Method:
- This method works similarly to the others, where the base case check is if the root is None, then we check if the current root is equal to the target value, and if not, continue recursively down the tree.

Print Tree Method:
- I decided to print In Order, so while the root exists, we recursively print the left child, then the root value, then recursively print the right child. This will correctly print the nodes in numerical order.


Code & Interesting Aspects:

I used a populate_tree helper method to make the initial tree with a random size by passing in a random.randint value to the add_node function inside of a while loop that will end once add_node has been called that many times.

In my main function, I decided to generate the root separately from the populate_tree function just so I could see which one is the original root. The assignment says to make a tree between 5 and 50 values, so after I generated the root, I used a random value between 4 and 50, since the size at this point is 1.


How to Run:

To run this program, download all the files from the problem1 folder into a directory of your choice, then simply run

python3 problem1.py
