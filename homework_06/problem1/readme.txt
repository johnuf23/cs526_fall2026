Introduction:

This problem merges k sorted lists of sale times into a single sorted log of (time, register) pairs, using the min heap from problem2 as a priority queue.


Algorithm:

Merge Logs Method:
- This method takes the list of registers' logs. First, it seeds the heap with the first sale from each non-empty register. Each entry is a tuple of (time, register number, index in that register's log). 
Since tuples compare element by element, two sales with the same time are automatically ordered by register number, so the lower register comes first.
- Then, while the heap isn't empty, we extract the minimum entry and add its (time, register) to the merged list. After that, we look at the register that entry came from, and if it has another sale, 
we insert that next sale into the heap.
- Because we always extract one entry before inserting the next one from the same register, the heap holds at most one entry per register, so it never has more than k entries. Empty logs just never get added to the heap.


Code & Interesting Aspects:

The heap is imported from the problem2 folder by adding it to the system path, and it is created with verbose turned off so none of the heap's debug printing shows up in the output.


How to Run:

To run this program, download all the files from the homework_06 into the same directory, then from inside the problem1 folder in command prompt run any of the following:

python3 problem1.py < input_files/merge_input1.txt
python3 problem1.py < input_files/merge_input2.txt
python3 problem1.py < input_files/merge_input3.txt
python3 problem1.py < input_files/merge_input5.txt
python3 problem1.py < input_files/merge_input6.txt
python3 problem1.py < input_files/merge_input7.txt
python3 problem1.py < input_files/merge_input8.txt
python3 problem1.py < input_files/merge_input9.txt
