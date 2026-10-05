import sys
from problem4 import SortedDoublyLinkedList

def main():
    sdll = SortedDoublyLinkedList()

    expected_args = {
        "add" : 1,
        "print_list" : 0,
        "delete" : 1,
        "exists" : 1,
        "total" : 0,
        "sum_middle_three" : 0,
        "median" : 0,
        "count" : 1
    }

    def parse_number(value):
        try:
            return int(value)
        except ValueError:
            return float(value)

    for line in sys.stdin:
        #remove leading and trailing blank spaces
        line = line.strip()

        #check if entire line is blank or startswith #
        if not line or line.startswith("#"):
            continue

        #separate each line into commands and arguments
        parts = line.split()
        command = parts[0]
        args = parts[1:]

        if command not in expected_args:
            print(f"Command not recognized: {command}")
            continue
        if len(args) != expected_args[command]:
            print(f'Invalid number of arguments for command: {command}. Expected: {expected_args[command]}')
            continue

        #methods
        if command == "add":
            sdll.add(parse_number(args[0]))

        elif command == "delete":
             sdll.delete(parse_number(args[0]))

        elif command == "print_list":
            sdll.print_list()

        elif command == "exists":
            sdll.exists(parse_number(args[0]))

        elif command == "total":
            sdll.total()

        elif command == "sum_middle_three":
            sdll.sum_middle_three()

        elif command == "median":
            sdll.median()

        elif command == "count":
            sdll.count(parse_number(args[0]))

if __name__ == "__main__":
    main()