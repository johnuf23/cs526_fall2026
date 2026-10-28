'''
Problem 3: Puzzle
'''
import sys
import math

n = int(sys.stdin.readline()) #first line

symbols = set()
board = {}

row_seen = set()
col_seen = set()
sub_seen = set()


def main():
    line2 = sys.stdin.readline().strip().split(",")
    for char in line2:
        symbols.add(char)

    print("Symbols: ", symbols)
    print()

    #add to board dictionary with coordinates as the key and char as value
    row = 0
    for line in sys.stdin:
        line = line.strip().split(",")
        print("row: ", row, line)
        for col in range(n):
            board[(row, col)] = line[col]
        row+=1
    print()

    #call all recursive checks beginning on top left space
    is_valid(0,0)


def is_valid(row, col):
    start = (row, col)
    
    if (not row_recurse(start) 
        or not col_recurse(start) 
        or not subboard_recurse(start, n)): #need n for size of sub-boards
        print("The board is invalid")
    else:
        print("The board is valid")
        

def row_recurse(coord):
    row, col = coord

    if row >= n:
        return True

    char = board[(row, col)]
    
    if char == '.':
        pass
    elif char in row_seen:
        print("Non-Unique Row: ", char, coord)
        return False
    elif char in symbols: #but not in row_seen
        row_seen.add(char)

    if col + 1 < n:
        return row_recurse((row, col+1))
    else:
        row_seen.clear()
        return row_recurse((row + 1, 0))


def col_recurse(coord):
    row, col = coord

    if col >= n:
        return True

    char = board[(row, col)]
    if char == '.':
        pass
    elif char in col_seen:
        print("Non-Unique Column: ", char, coord)
        return False
    elif char in symbols: #but not in col_seen
        col_seen.add(char)
    

    if row + 1 < n:
        return col_recurse((row + 1, col))
    else:
        col_seen.clear()
        return col_recurse((0, col + 1))


def subboard_recurse(coord, n):
    #different from others, coord is top left coord of sub-board
    row, col = coord
    size = int(math.sqrt(n))

    if row >= n:
        return True

    #two loops to check each space in sub-board
    for r in range(row, row + size):
        for c in range(col, col + size):
            char = board[(r, c)]
            if char != '.':
                pass
            elif char in sub_seen:
                print("Non-Unique Sub-Board: ", char, (r,c))
                return False
            elif char in symbols:
                sub_seen.add(char)

    sub_seen.clear()

    #if we are not at the right-most sub-board:
    if col + size < n:
        #move to the top left space of sub-board to the right
        return subboard_recurse((row, col + size), n)
    else:
        #move down one sub-board and start at top left space
        return subboard_recurse((row + size, 0), n)

    


if __name__ == "__main__":
    main()