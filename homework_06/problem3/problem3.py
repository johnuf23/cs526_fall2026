'''
Problem 3: Running Median Using Heap
'''

import sys
import os

# make problem2/problem2.py importable (sibling folder)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "problem2"))

from problem2 import Min_Heap


def parse_sales(data):
    cleaned = data.replace("[", " ").replace("]", " ").replace(",", " ")
    return [int(x) for x in cleaned.split()]


def running_medians(sales):
    # low holds the smaller half as a max-heap. Your Min_Heap is reused by
    # storing negated values, so the smallest negative is the largest real value.
    # high holds the larger half as a normal min-heap.
    low = Min_Heap(verbose=False)
    high = Min_Heap(verbose=False)
    medians = []

    for x in sales:
        # place the new sale in the correct half
        if low.last == 0 or x <= -low.root.value:
            low.insert(-x)
        else:
            high.insert(x)

        # rebalance so low has the same number of values as high, or one more
        if low.last > high.last + 1:
            high.insert(-low.extract_min())
        elif high.last > low.last:
            low.insert(-high.extract_min())

        # the median comes from the tops of the two heaps
        if low.last > high.last:
            medians.append(float(-low.root.value))
        else:
            medians.append((-low.root.value + high.root.value) / 2)

    return medians


def main():
    sales = parse_sales(sys.stdin.read())
    print(running_medians(sales))


if __name__ == "__main__":
    main()