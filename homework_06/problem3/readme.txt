Introduction:

This problem finds the running median of a stream of sale amounts, printing the median after each new sale. It uses the min heap I built in problem2 as the only data structure holding the sales.


Algorithm:

How the Heap Is Used:
- My heap from problem2 is a min heap, so I use two instances of it. The upper heap is a regular min heap that holds the larger half of the sales, 
so its root is the smallest of the large values. The lower heap holds the smaller half of the sales and needs to be a max heap, 
so I store the negative of each value in it. The smallest negative number is the largest real value, so its root is the largest of the small values.
- This means the two roots are the two values that sit in the middle of all the sales so far. 
I only use the heap's insert and extract_min methods, plus reading the root of each heap, so the problem2 class
 is not modified or replaced.

What Must Stay True After Each Sale:
- Two invariants have to hold after every sale for the median to be available in O(1) time.
- First, every value in the lower heap is less than or equal to every value in the upper heap. This is what makes the two roots the middle values.
- Second, the sizes are balanced: the lower heap has either the same number of values as the upper heap, or exactly one more.
- If both hold, the median is just a read of the roots. If the lower heap is larger, the count is odd and the median is the lower root. 
If the sizes are equal, the count is even and the median is the average of the two roots. No searching or sorting is needed.

Overall Approach:
- For each new sale, first place it in the correct half. If it is less than or equal to the lower heap's top (or the lower heap is empty), 
it goes into the lower heap. Otherwise it goes into the upper heap. This keeps the first invariant true.
- Then rebalance to restore the second invariant. Adding one value can only throw the sizes off by one, 
so at most one move is needed. If the lower heap has two more values than the upper heap, I extract its 
top and insert it into the upper heap. If the upper heap has more values than the lower heap, I extract its 
top and insert it into the lower heap. Moving a root from one heap to the other keeps the first invariant true, 
because that root is the largest of the lower half or the smallest of the upper half.
- Finally, I read the median from the roots as described above and append it to the output list.
- Each sale costs a constant number of inserts and extracts, each O(log n), and reading the median is O(1), so the whole stream takes O(n log n).


Code & Interesting Aspects:

To get a max heap out of a min heap without changing the class, I negate values on the way into the lower heap and negate them again 
whenever I read from it or move a value to the upper heap.

I read the roots directly instead of calling peek, since my peek method prints every time it is called.


How to Run:

To run this program, download all the files from the homework_06 into the same directory, then from inside the problem3 folder in command prompt run any of the following:

python3 problem3.py < input_files/median_input1.txt
python3 problem3.py < input_files/median_input2.txt
python3 problem3.py < input_files/median_input3.txt
python3 problem3.py < input_files/median_input4.txt
python3 problem3.py < input_files/median_input5.txt
python3 problem3.py < input_files/median_input6.txt
python3 problem3.py < input_files/median_input7.txt
python3 problem3.py < input_files/median_input8.txt
python3 problem3.py < input_files/median_input9.txt
python3 problem3.py < input_files/median_input10.txt
python3 problem3.py < input_files/median_input11.txt


