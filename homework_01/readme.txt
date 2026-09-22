This is a write up of how my helloworld.py program works and why each step was chosen

First, we define what our constraints are with what the user inputs. The helloworld.py file will handle different types of user input:
	1) The user inputs a command that names a file as an argument
	2) The user uses a redirect syntax such as < and then the name of a file
	3) Any other case, such as empty

In the main function, first we want to check if the user inputted the first case, where they just typed the name of the file 'python helloworld.py test.txt'. If so, then the length
of the argv will be greater than or equal to two. Therefore, we should go to the argument at index 1
and treat it as a file. We should open the file, iterate through each line, and print with end="" to
begin new lines. 

If the second case is true, we can use sys.stdin.isatty() to check for redirects like <. If that's the case, we don't need to 'with open as f' and instead iterate through the file with a for loop and do the same printing logic as before.

In any other case, we can print an error.


