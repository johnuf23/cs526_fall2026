'''
Problem 1: Snowfall
'''
import sys


def main():
    array = []

    n = int(sys.stdin.readline()) #first line = n
    days = sys.stdin.readline().split()

    for day in days:
        array.append(int(day))

    print(*array, "solution: ", check_snowfall(array, n))


def check_snowfall(A, n):
    solution = 'NO'

    #early check for validity
    if n < 3:
        return solution

    total = A[n-1]
    half = total / 2

    #check value at i = 2 first, day 0 has 0 snowfall
    if A[2] > half:
        solution = 'YES'
        return solution

    #sliding window of size 3
    day3 = 3
    window = 3

    while day3 < n:
        snowfall = A[day3] - A[day3 - window]

        if snowfall > half:
            solution = 'YES'
            break

        day3+=1

    return solution


if __name__ == "__main__":
    main()