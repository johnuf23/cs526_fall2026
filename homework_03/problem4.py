import sys
from fractions import Fraction

def main():
    n = None
    pairs = []

    for line in sys.stdin:
        # Remove leading and trailing blank spaces.
        line = line.strip()

        # Skip blank lines and comments.
        if not line or line.startswith("#"):
            continue

        # The first valid line contains the number of ghosts
        if n is None:
            n = int(line)
            continue

        #B x y G x y
        parts = line.split()

        buster_x = int(parts[1])
        buster_y = int(parts[2])
        ghost_x = int(parts[4])
        ghost_y = int(parts[5])

        pairs.append([buster_x, buster_y, ghost_x, ghost_y])

        # Stop reading after all n pairs have been collected
        if len(pairs) == n:
            break


    if eliminated(pairs):
        print("All Ghosts: were eliminated")
    else:
        print("All Ghosts: were not eliminated")


def eliminated(pairs):
    #For True, these must be true
    #   1) all slopes are equal
    #   2) no points lie on the same line

    # for 1), can just check first slope each time (or any slope). if ever false, return early
    # for 2) no two lines can have the same y intercept, add to hash set for each and check if in set
    # account for vertical lines

    #one y intercept per line
    seen = set()
    shared_slope = None

    for i in pairs:
        #change in y over change in x
        dx = i[2] - i[0]
        dy = i[3] - i[1]

        #vertical   
        if dx == 0:
            slope = "vertical"
            intercept = i[0]
        else:
            slope = Fraction(dy,dx)
            intercept = i[1] - slope * i[0]
            #y = mx + b
            #b = y - mx

        #check if same slope
        if shared_slope is None:
            shared_slope = slope
        elif slope != shared_slope:
            return False

        if intercept in seen:
            return False
        seen.add(intercept)

    return True

if __name__ == "__main__":
    main()
