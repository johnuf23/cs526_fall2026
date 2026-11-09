Introduction:

This problem states to find the possible number of combinations of vowels in a sequence of morse code without spaces, using A, E, I, O, and U as the possible vowels.


Algorithm:

Count Vowel Sequences Method:
- This method uses dynamic programming and a 2D state table to keep track of the number of possible vowel sequences at each position in the Morse code input.
The algorithm loops through every position in the Morse code sequence using an offset variable. At each position, it checks whether the symbols ending at that position match a valid vowel.
If a valid vowel is found, the algorithm looks at the previous position in the state table to determine how many valid sequences could have come before it. It adds the values from that previous row to get the total number of possible sequences.
If the vowel begins at the very beginning of the Morse code sequence, its corresponding table entry is set to 1, since there is one way to create that initial vowel.
This process is repeated for vowels of lengths 1, 2, and 3. If the symbols do not match a valid vowel, the corresponding table entry remains 0.
Once the entire Morse code sequence has been processed, the algorithm adds the three values in the final row of the state table. This gives the total number of possible vowel sequences that use the entire input.

Vowel Checking Methods:

- I created three helper methods to check whether a valid vowel can be formed at a particular position.
The vowel_at_position_with_len_1 method checks whether the current symbol is a dot (.), which represents the vowel E.
The vowel_at_position_with_len_2 method checks the current symbol and the symbol immediately before it. It returns True if the combination is either .. (I) or .- (A).
The vowel_at_position_with_len_3 method checks the current symbol and the two symbols before it. It returns True if the combination is either ..- (U) or --- (O).


Code & Interesting Aspects:

- One interesting aspect of this algorithm is that it uses previously calculated results instead of recalculating every possible combination of vowels. This allows the algorithm to build on smaller solutions to solve the larger problem, so the final input file with 100 characters and a result of 193050000 still takes very little time.


How to Run:
Download all the files from the problem2 folder into a directory of your choice, then run any of the following:

python3 problem2.py < input_files/vowel_input1.txt
python3 problem2.py < input_files/vowel_input2.txt
python3 problem2.py < input_files/vowel_input3.txt
python3 problem2.py < input_files/vowel_input4.txt