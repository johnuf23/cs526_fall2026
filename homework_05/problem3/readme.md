Introduction:

This problem is an implementation of an algorithm that finds the longest alternating increasing subsequence of two arrays, A and B where the values of the sequence must strictly increase, the elements must alternate between A and B, and each element must come from a position strictly after the previous element's position.

Algorithm:

Frontier Lists:
For each array I keep a frontier, made of three parallel lists: values (av, bv), lengths (al, bl), and node ids (ai, bi). The A frontier holds sequences that end in an element of A, and the B frontier holds sequences that end in an element of B, and each point means that a valid sequence of this length can end at this value. The values are sorted in increasing order and the lengths strictly increase along with them, so a point with a larger value is only kept if it is also longer. Any point that is both larger in value and not longer than another point can never give a better answer, so it gets thrown away. Each element gets a node id, where A[p] is p and B[p] is m + p.

The algorithm walks through the positions from left to right. At each position p, it finds the best sequence length ending at a[p] and the best sequence length ending at b[p]. Both of these are found before either one is inserted, since positions must strictly increase, so a[p] can't build on b[p] and vice versa.

To find the best sequence ending at a[p], I binary search the B frontier for the number of points with a value strictly less than a[p]. Because the lengths increase along the list, the last of those points has the longest length. The answer is that length plus 1, and that point's node id is saved in a prev array as the predecessor. If no points are smaller, the sequence is just a[p] by itself with a length of 1. The query for b[p] works the same way, but searches the A frontier. If the new length is better than the best so far, update best and best_node.

Once both queries are done, each new point is added to its own frontier, using binary search to find where it belongs. First check if an existing point already has a value less than or equal to the new value and a length at least as long. If so, the new point can't help and should be skipped. Otherwise we find the first point with a value greater than or equal to the new one and remove every point from there that is not longer than the new point, since the new point beats all of them. Then the new point is put in their place.

Lastly, to build the actual sequence, start at best_node and follow the prev links backward until -1 is reached, converting each node id back to its value. The values come out end to start, so I reverse the list before returning it.


Code & Interesting Aspects:

My first version of this problem used a 2D dynamic programming table with a third loop to look back at earlier positions, which seemed like it took too long on the large inputs so I rewrote it to use sorted frontier lists with binary search, which brings the time down. I did not use any modules other than os and sys, so the binary searches are written by hand instead of using bisect.

The main thing I had to be careful about was the position rule. The assignment's example shows that {1, 4, 7} is not valid because 4 and 1 are both at position 1, so querying both elements at a position before inserting either is what enforces this.



How to Run:

I set up my main function to not use the < argument in command prompt, so we can just run the relative file path as the argument at sys.argv[1] to get the file name for the output.
To run this program, download all the files from the problem3 folder into a directory of your choice, then run any of the following:

python3 problem3.py input_files/longest_seq1.txt
python3 problem3.py input_files/longest_seq2.txt
python3 problem3.py input_files/longest_seq3.txt
python3 problem3.py input_files/longest_seq4.txt
python3 problem3.py input_files/longest_seq5.txt
python3 problem3.py input_files/longest_seq6.txt
