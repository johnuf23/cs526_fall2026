'''
takes file with single string and returns each unique substring on its own line, in alphabetical order, followed by the count

'''
import sys

seen = []

def main():

    counter = 0

    for line in sys.stdin:
        line = line.rstrip("\n") #get rid of line break from rear of line
        for i in range(len(line)):
           substring_check(line, i, i)   #returns substrings, beginning at each character of string

    sorted_seen = sorted(seen)

    for substring in sorted_seen:
        print(substring)
        counter += 1
    print(counter)

#recursive function
def substring_check(string, start, end):
    #start and end both on same index at first
    if end >= len(string):
        return
    
    chars = []
    for i in range(start, end + 1):
        chars.append(string[i])
    substring = "".join(chars)
    if (substring not in seen):
        seen.append(substring)

    substring_check(string, start, end + 1)

    
if __name__ == "__main__":
    main()

#recursive function heart:
#check substring from start and end index if it's in seen[]