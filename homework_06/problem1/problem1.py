'''
Problem 1: Merge k Sorted Lists using a Priority Queue
'''

import sys
import os

# make problem2/problem2.py importable
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "problem2"))

from problem2 import Min_Heap


def parse_log(line):
    cleaned = line.replace("[", " ").replace("]", " ").replace(",", " ")
    return [int(x) for x in cleaned.split()]


def merge_logs(logs):
    heap = Min_Heap(verbose=False)
    merged = []

    # seed with the first sale of each non-empty register
    # entries are (time, register, index): ties on time fall to the lower register
    for r, log in enumerate(logs, start=1):
        if log:
            heap.insert((log[0], r, 0))

    while heap.last > 0:
        time, r, i = heap.extract_min()
        merged.append((time, r))

        # refill from the same register; the heap never exceeds k entries
        if i + 1 < len(logs[r - 1]):
            heap.insert((logs[r - 1][i + 1], r, i + 1))

    return merged


def main():
    logs = []
    for line in sys.stdin:
        if line.strip() == "":
            continue
        logs.append(parse_log(line))

    merged = merge_logs(logs)

    print("Registers:", len(logs))
    print("Total sales:", len(merged))
    print("Merged log:", merged)


if __name__ == "__main__":
    main()