Problem 2


Algorithm & Code:

Since we can exit the algorithm once the infection is no longer growing, I created
a trigger "growing" that checks if the infected array has grown since the "day" has been run,
and if so, we perform a final check on if there are any healthy counties left, and then
return the result.

To simulate each day with simulate_day(), I used two loops, one for each row and column. Once I found an uninfected
county, I ran a check of its neighbors with a different function. If that function returned
a valid result (>= 2), I added that county to a temporary array as a newly infected county.
After every space was checked, I added all those counties from the temp array into the 
official infected array. I used a temp array because according to the problem, each county
gets infected simultaneously each day, so if I just added them immediately upon successful 
check, it would return unexpected results.

To check each neighbor with check_neighbors(), I determined its left, right, up, and down tiles 
based on coordinates and added them to an array. Then I looped through that array, checked 
if the neighbor was a valid tile on the map, and if the neighbor was infected, incremented a count. 
After each neighbor was checked, the function returns a count, which the day simulation receives 
as previously mentioned.

Finally, the final check for healthy counties again uses two loops to check each county
individually, and if any are not in the infected array then there are healthy counties left.

In summary, my algorithm is made up of separate loops that run in succession. 
The day simulation is an n squared algorithm that includes a neighbor check of
constant time, and the final healthy check is also n squared.


How to Run:

Download all files in the problem1 folder onto your machine, navigate to that location in 
your working directory in terminal or command prompt, then run any of these commands:

    python3 midterm_2.py < pandemic_input1.txt
    python3 midterm_2.py < pandemic_input2.txt


example executions can be found in the example_execution_2a, 2b, and 2c pngs