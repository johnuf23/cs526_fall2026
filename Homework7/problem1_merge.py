'''
Problem 1: Merge Sort, Quick Sort, and Insertion Sort
'''

import sys

numbers = []

for line in sys.stdin:
    numbers.append(int(line.strip()))


def merge_sort(a):
    #base case subarray length 0 or 1
    if len(a) <=1:
        return a

    #split into two halves
    mid = len(a) // 2

    #call recursively on both halves
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    #merge together
    return merge(left, right)


def merge(left, right):
    output = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i])
            i+=1
        else:
            output.append(right[j])
            j+=1
    #either i or j are out of range, append rest of either side to output
    output.extend(right[j:])
    output.extend(left[i:])
    return output

print("Original Input: ", numbers)
print("Merge-Sorted Output: ", merge_sort(numbers))
