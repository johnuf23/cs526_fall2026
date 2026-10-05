

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