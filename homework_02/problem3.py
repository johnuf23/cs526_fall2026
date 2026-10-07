# a) I am working from the top down, so the base case is that I am already standing
#  at the top step, in which case the ways to get there equal zero.
# If I am one step below the top step, there is also only one way to get to the top
# If I am two steps below the top, I can go straight to the top, or go to the n-1 step, which has already been calculated.
# A staircase of 0 has 1 way, staircase of 1 has 1, and staircase of 2 has 2
# Anything n < 2 has ways(n-1) + ways(n-2) + ways(n-3) because they have been already calculated by the time you get to the bottom
#
# b) We can see that the pattern is that ways(n) is the previous three combined, because
# the problem states that we can take 1, 2, or 3 steps at a time
# But if we can only take 2 steps at a time, then it's the same as the Fibonacci Sequence

def climb(n: int) -> int:
    #work backward from top
    #if standing at top step, there is one way
    #if standing n-1 step, also just one way
    if (n < 2):
        return 1
    elif (n == 2):
        return 2
    else:
        return climb(n-1) + climb(n-2) + climb(n-3)

        
def main():
    n = int(input("Enter number of stairs: "))
    print(climb(n))

if __name__ == "__main__":
    main()