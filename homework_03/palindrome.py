'''
Takes input from standard input a list of strings and determines which is a palindrome
Because it uses ASCII values to determine validity, only uppercase and lowercase english letters are considered
'''
import sys

def main():
    counter = 0
    for line in sys.stdin:
        #remove leading and following whitespace
        line = line.strip()
        if checkPalindrome(line):
            print("True")
            counter += 1
        else:
            print("False")

    print(counter)

def checkPalindrome(string):
    #beginning and end should already not be whitespace from .strip()
    p1 = 0
    p2 = len(string) - 1

    while p1 < p2:
        #get ascii values
        if ord(string[p1]) != ord(string[p2]):
            return False

        #they are equal and now find next char from front and rear
        p1 += 1
        p2 -= 1
        #checks if char is whitespace or non-letter
        while ord(string[p1]) < 65 or ord(string[p1]) > 122:
            p1 += 1
        while ord(string[p2]) < 65 or ord(string[p2]) > 122:
            p2 -=1
    return True

if __name__ == "__main__":
    main()