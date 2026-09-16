'''

This file accepts a file from standard input with n lines and prints the lines to standard output

'''

import sys

try:
    for line in sys.stdin:
        print(line, end="")
except UnicodeDecodeError:
    print("Error: file is not a text file. Please only input a file with the .txt extension", file=sys.stderr)