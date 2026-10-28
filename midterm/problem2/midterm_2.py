'''
Problem 2: Pandemic
'''
import sys

infected = []
n = int(sys.stdin.readline()) #only first line

def main():

    #initial infected counties, starting on line 2 of input
    for line in sys.stdin: 
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        infected.append((x, y))
    #print initial state
    print_helper(infected)

    growing = True

    while growing:
        last_total = len(infected)
        simulate_day()
        if len(infected) == last_total:
            growing = False

    #check for final output only after no growth occurs
    if any_healthy(infected):
        print("There are healthy counties left")
    else:
        print("There are no healthy counties left")
    

def simulate_day():
    #temp[] is necessary since infection happens simultaneously, so
    #don't update infected array until all cells have been checked
    temp = []

    #for each healthy county, then check if it has two or more infected neighbors
    for i in range(n):
        for j in range(n):
            if (i, j) not in infected:
                if check_neighbors(i,j) >= 2:
                    temp.append((i,j))
                    print("newly infected: ", (i,j))

    for item in temp:
        infected.append(item)
    temp.clear()
    #print current state
    print_helper(infected)
    

def check_neighbors(i, j):
    count = 0
    #left, down, right, up
    neighbors = [(i,j-1), (i+1, j), (i, j+1), (i-1, j)]

    #if both i and j are part of the map, in
    for neighbor in neighbors:
        if (neighbor[0] in range(n)
            and neighbor[1] in range(n)
            and neighbor in infected):
                count+=1
    return count     


def any_healthy(array) -> bool:
    for i in range(n):
        for j in range(n):
            if (i,j) not in array:
                return True
    return False
    

def print_helper(array):
    for i in range(n):
        for j in range(n):
            if (i,j) in array:
                print('X ', end='')
            else:
                print('. ', end='')
        if j == (n-1):
            print()
    print()
    
if __name__ == "__main__":
    main()