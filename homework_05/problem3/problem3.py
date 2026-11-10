
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

    result = longest_alternating_sequence(size_a, size_b, a, b)

    print(f"File Input: {os.path.basename(filename)}")
    print(f"Longest Sequence: {len(result)}")


#BINARY INDEX TREES
def longest_alternating_sequence(size_a, size_b, a, b):
    m, n = size_a, size_b
    if m == 0 and n == 0:
        return []
    
    av, al, ai = [], [], []
    bv, bl, bi = [], [], []

    # predecessor node, for reconstruction
    prev = [-1] * (m + n)
    best = 0
    best_node = -1

    for p in range(max(m, n)):
        fa = fb = 0

        #query both arrays before any insert
        if p < m:
            x = a[p]
            lo, hi = 0, len(bv)
            # count of B-points with value < x
            while lo < hi:                    
                mid = (lo + hi) >> 1
                if bv[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            if lo:
                fa = bl[lo - 1] + 1
                prev[p] = bi[lo - 1]
            else:
                fa = 1
            if fa > best:
                best = fa
                best_node = p

        if p < n:
            y = b[p]
            lo, hi = 0, len(av)
            # count of A-points with value < y
            while lo < hi:                    
                mid = (lo + hi) >> 1
                if av[mid] < y:
                    lo = mid + 1
                else:
                    hi = mid
            if lo:
                fb = al[lo - 1] + 1
                prev[m + p] = ai[lo - 1]
            else:
                fb = 1
            if fb > best:
                best = fb
                best_node = m + p

        #inserts
        if fa:
            # r = count of A-points with value <= x
            lo, hi = 0, len(av)
            while lo < hi:
                mid = (lo + hi) >> 1
                if av[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            # Skip if an existing point is at least as small and at least as long.
            if not (lo and al[lo - 1] >= fa):
                # s = count of A-points with value < x
                s, hi = 0, lo
                while s < hi:
                    mid = (s + hi) >> 1
                    if av[mid] < x:
                        s = mid + 1
                    else:
                        hi = mid
                # Remove points the new one dominates (value >= x, length <= fa).
                e = s
                size = len(av)
                while e < size and al[e] <= fa:
                    e += 1
                av[s:e] = [x]
                al[s:e] = [fa]
                ai[s:e] = [p]

        if fb:
            lo, hi = 0, len(bv)
            while lo < hi:
                mid = (lo + hi) >> 1
                if bv[mid] <= y:
                    lo = mid + 1
                else:
                    hi = mid
            if not (lo and bl[lo - 1] >= fb):
                s, hi = 0, lo
                while s < hi:
                    mid = (s + hi) >> 1
                    if bv[mid] < y:
                        s = mid + 1
                    else:
                        hi = mid
                e = s
                size = len(bv)
                while e < size and bl[e] <= fb:
                    e += 1
                bv[s:e] = [y]
                bl[s:e] = [fb]
                bi[s:e] = [m + p]

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
