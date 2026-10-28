Problem 1


Algorithm:

The algorithm I chose is the sliding window of constant size, which checks the difference in the 
value at the end and the beginning of the window and compares that to half of the total
(the value of the last element in the array) each iteration. The checks run in a while loop that
terminates once the end of the window is out of range of the array.


Code & Interesting Aspects:

In my check_snowfall function, I first set the default solution to 'NO', then checked for an
early exit condition, where the size of the array is less than 3. Another early exit condition
I chose was where the value at the 3rd element is a valid amount, since the snowfall on day 0
is 0. I didn't include this in the sliding window since the beginning of that window would have been
out of range of the array. Then I started the checks at the 4th element, with the beginning at the
1st element.

The reason I chose a window and not two pointers is because the window size is constant. This way,
I don't have to increment both ends of the window each iteration, and can just increment the end.


How to Run:

Download all files in the problem1 folder onto your machine, navigate to that location in 
your working directory in terminal or command prompt, then run any of these commands:

    python3 midterm_1.py < snowfall_input1.txt
    python3 midterm_1.py < snowfall_input2.txt
    python3 midterm_1.py < snowfall_input3.txt
    python3 midterm_1.py < snowfall_input4.txt
    python3 midterm_1.py < snowfall_input5.txt


example executions can be found in the example_execution_1.png