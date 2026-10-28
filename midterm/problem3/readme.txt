Problem 3


Algorithm:

My algorithm uses three separate recursive functions to check for each condition,
since each is independent of each other. If any one of the recursive functions returns
a False, we can return "Invalid". Recursion is easy here because the sub problem decreases
in size each time until we run out of sub problems to check.

For the row and column recursive checks, we start at (0,0) and check that character. If it's
a '.', we can ignore and move on. Otherwise, if that character has already been seen in that
row/column, we return False. If the character was not already seen but it is indeed a 
character in the symbols hash set, we can add that to the array of characters we have seen.
If there are more spaces in the row/column to explore, we call the function again on the
next one. If we are at the end of the row/column, we reset the set of seen characters and
call the function on the next row/column.

The sub-board recursive check works in a similar but slightly different way. We must receive
the size of the total board as an input so that we can calculate the size of each sub-board.
Then for simplicity I created two loops to iterate through each space in the sub-board,
with the top left space as the origin, using similar character checking as the row/column
recursive checks. 


Code & Interesting Aspects:

Before the validity check, I first add all the symbols to a hash set for quick lookup and
then add all the characters and their coordinates to a board dictionary, where the 
coordinate is the key and the character is the value.

I created hash sets for each row/column/sub-board's currently seen characters, so we can
easily check for duplicates. With this method, the sets must be cleared each time we move
onto a new sub problem.

I put all three recursive checks into the is_valid function, with the absolute top left
space as the initial input.


How to Run:

Download all files in the problem1 folder onto your machine, navigate to that location in 
your working directory in terminal or command prompt, then run any of these commands:

    python3 midterm_3.py < puzzle_game_input1.txt
    python3 midterm_3.py < puzzle_game_input2.txt
    python3 midterm_3.py < puzzle_game_input3.txt

example executions can be found in the example_execution_3 png
