
'''
Problem 3: Longest Alternating Increasing Subsequence
'''
import os
import sys

def main():

    filename = sys.argv[1]

    with open(filename, "r") as file:
        size_a = int(file.readline().strip())
        size_b = int(file.readline().strip())

        a = list(map(int, file.readline().strip().split()))
        b = list(map(int, file.readline().strip().split()))


    if len(a) != size_a or len(b) != size_b:
        print("Error: Array sizes do not match the input.")
        return

    result = longest_alternating_sequence(a, b)

    print(f"File Input: {os.path.basename(filename)}")
    print(f"Longest Sequence: {len(result)}")


def longest_alternating_sequence(a, b):
    m, n = len(a), len(b)
    if m == 0 and n == 0:
        return []

    # Compress values to ranks 1..size for use as Fenwick tree indices.
    rank = {v: r for r, v in enumerate(sorted(set(a) | set(b)), 1)}
    size = len(rank)

    # Fenwick trees (prefix maximum) over value rank.
    # len_x[r] = best length of a valid sequence ending in an element of X
    # whose value rank is covered by node r; id_x[r] = that sequence's end node.
    # Node ids: A[p] -> p, B[p] -> m + p.
    len_a = [0] * (size + 1)
    id_a = [-1] * (size + 1)
    len_b = [0] * (size + 1)
    id_b = [-1] * (size + 1)

    prev = [-1] * (m + n)   # predecessor node, for reconstruction
    best = 0
    best_node = -1

    # Walk positions left to right. Both elements at position p are queried
    # before either is inserted, since positions must strictly increase.
    for p in range(max(m, n)):
        fa = fb = 0

        if p < m:
            ra = rank[a[p]]
            i = ra - 1
            q = 0
            qid = -1
            while i > 0:
                if len_b[i] > q:
                    q = len_b[i]
                    qid = id_b[i]
                i &= i - 1
            fa = q + 1
            prev[p] = qid
            if fa > best:
                best = fa
                best_node = p

        if p < n:
            rb = rank[b[p]]
            i = rb - 1
            q = 0
            qid = -1
            while i > 0:
                if len_a[i] > q:
                    q = len_a[i]
                    qid = id_a[i]
                i &= i - 1
            fb = q + 1
            prev[m + p] = qid
            if fb > best:
                best = fb
                best_node = m + p

        if fa:
            i = ra
            while i <= size:
                if len_a[i] < fa:
                    len_a[i] = fa
                    id_a[i] = p
                i += i & -i
        if fb:
            i = rb
            while i <= size:
                if len_b[i] < fb:
                    len_b[i] = fb
                    id_b[i] = m + p
                i += i & -i

    # Reconstruct the sequence by following predecessor links.
    result = []
    node = best_node
    while node != -1:
        result.append(a[node] if node < m else b[node - m])
        node = prev[node]
    result.reverse()

    return result

if __name__ == "__main__":
    main()
