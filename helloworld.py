'''

This file accepts a file from standard input with n lines and prints the lines to standard output

'''

import sys

filename = sys.argv[1]

try:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
except UnicodeDecodeError:
    print("Error: file is not a text file.", file=sys.stderr)
