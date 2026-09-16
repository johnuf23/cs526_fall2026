This is a step by step set of instructions on how to successfully run helloworld.py from the command line and how the program 
was implemented.

RUNNING THE PROGRAM FROM COMMAND LINE:

1. Ensure you have python3 downloaded on your machine
2. Download the raw file helloworld.py from this repository.
3. Save the helloworld.py file to a folder
4. Open up your command prompt and change your working directory to the location of that folder
    For example, cd C:\Users\jfice\Desktop\TestFolder
5. Create a text file in that same folder which will be the file you input into the program
6. Run this command in the command line, where 'file.txt' is the name of your text file, including the .txt extension:
    python helloworld.py < file.txt
7. You should see the lines of that file in the standard output!

Error cases:
    If you do not see the expected output:
    - You may not have the text file in the same folder as your working directory. Ensure the .txt file is in the same folder
    as the helloworld.py file
    - The text file may not be a text file. This program currently only works with text files. The extension must be .txt


IMPLEMENTATION EXPLANATION:

The first step in solving this problem is to account for accepting input. Through reading the python documentation for the sys module,
we can learn that Standard Input (stdin) allows us to read input from the standard input stream one line at a time. Our goal
for the program is to be able to input the file name after 'python program.py < '. 

The next consideration we will note is the error case of the input not being a .txt file. Therefore, we will use the try/except clause
in Python. Within the scope of try, we will place the logic for the main purpose of the program, and under except we will handle
this error case.

Assuming the user has inputted a .txt file, under try we now need to iterate through each line of the standard input and print.
We can accomplish this by a loop: for line in sys.stdin:

There is one expression in the loop, just print(line, end=""). For each line that exists in input file, the command line will
output the line as a string, go to the next line without creating additional lines, and then go through the loop again. Once
the input file is out of lines, the program ends. Without the end="", the print function in Python automatically adds a
n additional \n, resulting in additional lines.