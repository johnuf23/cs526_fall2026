'''

This file accepts a file from standard input with n lines and prints the lines to standard output

'''
import sys

#python helloworld.py < test.txt
def read_file():
    for line in sys.stdin:
        print(line, end="")

#python helloworld.py test.txt
def read_file_as_argument():
    with open(sys.argv[1]) as f:
        for line in f:
            print(line, end="")

def main():
    if len(sys.argv) >= 2:
            read_file_as_argument()
    else:
        read_file()
    

if __name__ == "__main__":
    main()