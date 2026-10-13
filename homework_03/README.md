# Introduction:

\*All example execution screenshots are in the folder example\_executions\*



## Problem 1:

This problem asks to determines whether each string in a list of strings is a palindrome. My code goes through each line, ensures that one line is one string, then runs a checkPalindrome method.



## Problem 2:

This problem asks to find and count each unique substring within a string using a recursive function.

My code goes through each index of the input string and iterates between the starting index and the last index, adding each substring not seen into a hash set. It sorts the set for easier checking and outputs each unique substring, followed at the end by the number of unique substrings.



## Problem 3:

This problem asks to reverse the contents of each implementation of a stack in-place, with an Array Stack, Singly Linked List Stack, and Sorted Doubly Linked List Stack. My code imports my custom implementation of the SinglyLinkedList and SortedDoublyLinkedList from the previous homework\_02. Therefore, you must run as a module when testing.



I needed to first provide implementations for each of the types of Stacks. Then I created methods to turn them into strings, and an additional method to insert\_at\_bottom, which the recursive reverse\_stack method calls. Then I made each stack automatically fill with ints from 1 to 10, then print. My main function calls print on each type of stack, taking the stack as a parameter.



## Problem 4:

This problem asks to find whether a series of Ghostbusters will cross firing lines when shooting at their assigned Ghost. My code checks each firing line's slope and y intercept and makes a determination based off them. It outputs "All Ghosts: were eliminated" if the firing lines never cross and "All Ghosts: were not eliminated" if so.



# Algorithm:

## Problem 1:

The checkPalindrome method uses two pointers, one at the first index of the string and one at the last index. It performs a while loop, while p1 < p2, and gets the ASCII numeric values for each character, since each character is determined ahead of time to be an uppercase or lowercase English letter. So it just compares the values of the characters at each pointer, and if they are ever not equal, it can exit early. Once they're determined to be equivalent, we increment p1 and decrement p2. Since I want to account for spaces or any invalid characters, I quickly check if the ASCII value is within 65 and 122, the values for the letters according to the ASCII chart. Once it goes through the whole string, it returns True.



Main calls this method for each line in the text file. After True is returned for that string, it prints True and updates a counter, which is printed at the end for each valid palindrome.



## Problem 2:

The heart of my recursive function performs as follows:

* receive input of: original input string, a starting index, and an ending index

  * \*start and end both 0 at first, to check a single character in that iteration
* join the characters within a given range into a new substring
* check if that substring is already in the "seen" hashset, and if not, add it
* call the recursive function again, but with the end index one greater



* Base case: if the end index is outside the index range of the string (length of string), return



The recursive function is only concerned with a static starting index, and my main function calls the recursive function again, but with the next index of the string.

In other words, the recursive function does not go through the entire original input string; only the series of substrings beginning with a given starting index



## Problem 3:

Problem 3:

All three stacks have the same four methods: push, pop, peek, and is\_empty.



StackArray stores its values in a fixed-size list created with a given capacity and tracks the index of the top element in self.top, which starts at -1 for an empty stack. Push increments top and stores the value there, and pop reads the value at top, clears the slot, and decrements top.



StackLinkedList wraps the SinglyLinkedList from homework\_02\\problem2.py. The head of the list is the top of the stack, so push calls prepend, pop calls delete\_at(0), and peek calls get(0).



StackSortedDoublyLinkedList wraps the SortedDoublyLinkedList from homework\_02\\problem4.py. Its add method inserts values in sorted order, which would break the last-in-first-out behavior, so push builds a new node and links it in front of the head manually, updating head, tail (if the list was empty), and size. Pop unlinks the head node in the same way.



The reversal uses two recursive functions that only call the stack methods. Insert\_at\_bottom has a base case of an empty stack, in which case we push the input value. If not empty, we pop the top value, set it equal to the top\_value, inserts that value at the bottom, then pushes the top value.



Reverse\_stack has a base case of an empty stack. First, it pops the top value and sets it equal to top\_value, calls itself, then inserts the top\_value at the bottom. After the stack is empty, we have successfully reversed the stack without making a new stack in memory.



## Problem 4:

After getting the coordinates from the input file and appending them to a pairs array, my code first checks if the slope of each pair is unique. If any pair's slope is unique, return False early. This is true because each line extends infinitely in both directions, so they all must be parallel to each other by definition.



However, a second case to consider is the case where two lines have the same slope but exist on the same line. In other words, if two lines have the same y intercept, then they are not valid. My code gets the intercept for each valid pair, checks if it is in a hashset of already seen intercepts, and returns False if there are any matches.



One additional consideration is if the slope is vertical, which would return a ValueError because the slope would then be undefined. For this case, I set the slope for that pair to be a string: "vertical". I can check for equivalence similarly in that case as well. The intercept in that case would just be any x value.



After iterating through the entire pairs array for each pair, if False has not been called, we can return True.





# Interesting Aspects:

## Problem 1:

Since "g e e k" counts the same as "geek", this necessitates the check for spaces in between the characters. Since in main I use the strip() method, I don't have to account for leading or following spaces, so the first check of p1 and p2 in my while loop does not have to include the check for valid characters. I also assume the first and last characters are not invalid in the text file.





## Problem 2:

Why I decided to design my program as such:



I wanted to break the heart of the recursive function down into a relatively simple process, so I thought that it should not be concerned with traversing the string then moving its start index and traversing again and again. Rather, I figured that it could focus on traversing just once with a given starting point and instead make main call the function on each index of the original string.



I suppose I could have made the recursive function do everything if at the "if end >= len(string)" check in the base case I instead incremented the starting index, set the end to the start, and then called, the function again. I could have then added another base case check if the start index is out of range.



Designing my program in my chosen way adds conceptual simplicity, although had I designed it such that the main function just calls the recursive function once, it would be cleaner.



One more note is that in the middle of my recursive function, in order to actually get the substring I added a new list called chars and used the built-in python method to join those chars in that range into a new substring. This uses a little more memory but I'm unsure of a better alternative that doesn't overcomplicate the algorithm.



## Problem 3:

Filling and printing are recursive as well. fill\_stack(stack, value=1) pushes the value and calls itself with value + 1, and its base case is value > 10. The linked list stacks print with recursive helpers (linked\_list\_string and doubly\_list\_string) that build the string for the rest of the list first and then append the current node's value.



Since reverse\_stack and insert\_at\_bottom only use push, pop, and is\_empty, I never had to write a separate reversal for each data structure. The same two functions work on all three stacks, so the stack behaves the same way regardless of what is underneath it.



The doubly linked list was the awkward one, because the class from homework\_02 is a sorted list and its only way to add a value is a sorted insert. Using it would have put the values in numeric order instead of the order they were pushed. My push therefore changes the list's head, tail, and size directly from outside the class. This works, but it breaks encapsulation. A cleaner design would add a push\_front method to the original class, but I wanted to leave my homework\_02 code unchanged.



## Problem 4:

One roadblock I ran into was checking for equivalence of slopes with a floating number. In Python, this can sometimes be problematic so my solution was to import Fraction from fractions.



To get the intercept of each slope, I just used the classic y = mx + b and turned it into b = y - mx



At first I misread the question and thought that the lines only fired in one direction infinitely, so I was trying to account for the additional case in which the lines had the same slope and same intercept but fired in opposite directions. After rereading the question more carefully, I saved myself a lot more time :)





# How to Run:

## Problem 1:

To run problem 1, download the homework\_03 folder onto your machine, navigate to that directory in the command prompt, and run this command:

&#x09;python3 palindrome.py < tests\_p1\\<name of test text file>

&#x09;example:

&#x09;python3 palindrome.py < tests\_p1\\palendrome\_0.txt



### Problem 2:

To run problem 2, download the homework\_03 folder onto your machine, navigate to that directory in the command prompt, and run this command:

&#x09;python3 problem2.py < tests\\unique\_substrings\_input\_0.txt



## Problem 3:

DIFFERENT FROM OTHER PROBLEMS:

To run problem 3, the homework\_02 folder must also be downloaded onto your machine, as a sibling to homework\_03. Navigate to that PARENT FOLDER, then run this command:

&#x09;python -m homework\_03.problem3





## Problem 4:

To run problem 4, download the homework\_03 folder onto your machine, navigate to that directory in the command prompt, and run this command:

&#x09;python3 problem4.py < tests\_p4\\ghostbusters\_input\_0.txt





