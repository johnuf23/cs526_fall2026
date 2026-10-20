import sys

def main():
    n = int(sys.stdin.readline().strip())
    target = int(sys.stdin.readline().strip())
    arr = []

    for line in sys.stdin:
        arr.extend(map(int, line.split()))

    rev_sorted = sorted(arr, reverse=True)

    sum = 0
    answer = 0

    for i, value in enumerate(rev_sorted):
        sum += value
        if sum > target:
            answer = i + 1
            break
    print("Input: ", arr, "Target: ", target, "Answer: ", answer)
    return
    



if __name__ == "__main__":
    main()

