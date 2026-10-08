# Introduction:



## Problem 1:



## Problem 2:

This problem asks to find and count each unique substring within a string using a recursive function.

My code goes through each index of the input string and iterates between the starting index and the last index, adding each substring not seen into a hash set. It sorts the set for easier checking and outputs each unique substring, followed at the end by the number of unique substrings.



# Algorithm:

## Problem 1:



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





# Interesting Aspects:

## Problem 1:



## Problem 2:

Why I decided to design my program as such:



I wanted to break the heart of the recursive function down into a relatively simple process, so I thought that it should not be concerned with traversing the string then moving its start index and traversing again and again. Rather, I figured that it could focus on traversing just once with a given starting point and instead make main call the function on each index of the original string.



I suppose I could have made the recursive function do everything if at the "if end >= len(string)" check in the base case I instead incremented the starting index, set the end to the start, and then called, the function again. I could have then added another base case check if the start index is out of range.



Designing my program in my chosen way adds conceptual simplicity, although had I designed it such that the main function just calls the recursive function once, it would be cleaner.



One more note is that in the middle of my recursive function, in order to actually get the substring I added a new list called chars and used the built-in python method to join those chars in that range into a new substring. This uses a little more memory but I'm unsure of a better alternative that doesn't overcomplicate the algorithm.





# How to Run:

## Problem 1:



### Problem 2:

To run problem 2, download the homework\_03 folder onto your machine, navigate to that directory in the command prompt, and run this command:

&#x09;python3 problem2.py < tests\\unique\_substrings\_input\_0.txt

