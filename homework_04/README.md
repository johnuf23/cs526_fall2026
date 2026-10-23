# Introduction:

\*All example execution screenshots are in the folder example_executions. For problem 2, there is one screenshot for the first two tests and 2 separate screenshots for the third test since its input is so long\*



## Problem 1:

This problem asks to find the sequence of nodes generated for each type of traversal of the given tree. The answers are in the markdown file problem1.md


## Problem 2:

This problem asks to compute the smallest number of elements from a given array whose sum is greater than the given target


## Problem 3:

This problem asks to find the number of unique right triangles that can be formed by choosing sets of three points from the given input.



# Algorithm:

## Problem 1:

Preorder Tree Traversal prints the root, then left, then right.

Breadth-First Tree Traversal prints each child from left to right at each level.

Post Tree Traversal prints each child before the root.

In-Order Tree Traversal visits left node first, then root, then right.



## Problem 2:

My algorithm first sorts the array from highest to lowest, then iterates through the array until the sum of those numbers is greater than the target.

Because the values at the beginning of the reverse sorted array are the largest values, it must be the case that they are the least amount of values that add up to a sum greater than the target.



## Problem 3:

My python program first adds all the coordinates to an array then calls the right_angles function which takes that array as an input and returns the counter of unique triangles.

My algorithm iterates through the coordinates array and for each point, considers it an origin and then performs logic on the remainder of the points.

For each point:
1. Sets it as an origin and gets the offset value to apply to the other points
2. Get the angle of every non-origin point using arctan (atan2 from import math), normalize it to 360 degrees and round to the nearest 5 decimals
3. Add that angle as a key to a dictionary with a frequency for its value
4. Separately iterate through the angles dictionary and check whether a key that is 90 degrees away exists, and if so, increment the counter by the product of the two angles' frequencies in the dictionary.

At the end of the right_angles function, I return the final counter and print in main()



# Interesting Aspects:

## Problem 1:

N/A


## Problem 2:

This problem is pretty straightforward since I can use a built-in sorting method to sort in descending order.


## Problem 3:

I used the suggested method from class to set each point to the origin and calculate each other point based off that. This method ends up working in just a couple seconds on the large set. The time complexity should be n * (n + n), so n squared, since inside each loop there are two separate loops.

It's very efficient to use a dictionary lookup to tell whether each angle has a right angle counterpart, and using the value as a frequency makes it easy to calculate how many unique triangles exist without duplicate values. 

One thing that was tricky was determining the angles. Since math.atan2 outputs an angle from -180 to 180, I wanted to normalize each angle to 360 by using the modulo operator. Furthermore, I decided to stick with floating values and simply rounding them to the nearest 5 decimals, which I felt would be precise enough to count as a right triangle.

# How to Run:

### Problem 1:

N/A


### Problem 2:

To run problem 2, ensure the homework\_04 folder is downloaded onto your machine, navigate to that directory in the command prompt, and run any of these commands:

python3 problem2.py < tests_p2\fewest_1.txt
python3 problem2.py < tests_p2\fewest_2.txt
python3 problem2.py < tests_p2\fewest_3.txt


### Problem 3:

To run problem 3, ensure the homework\_04 folder is downloaded onto your machine, navigate to that directory in the command prompt, and run any of these commands:

python3 problem3.py < tests_p3\rightangles_1.txt
python3 problem3.py < tests_p3\rightangles_2.txt
python3 problem3.py < tests_p3\rightangles_3.txt










