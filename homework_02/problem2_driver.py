import sys
from problem2 import SinglyLinkedList

def main():
    ll = SinglyLinkedList()

    expected_args = {
        "append" : 1,
        "prepend": 1,
        "insert": 2,
        "get": 1,
        "find": 1,
        "len": 0,
        "update": 2,
        "delete": 1,
        "delete_at": 1,
        "print_list": 0
    }

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
        if command == "append":
            ll.append(int(args[0]))

        elif command == "prepend":
            ll.prepend(int(args[0]))

        elif command == "insert":
            ll.insert(int(args[0]), int(args[1]))

        elif command == "get":
            print(ll.get(int(args[0])))

        elif command == "find":
            print(ll.find(int(args[0])))

        elif command == "len":
            print(ll.__len__())

        elif command == "update":
            ll.update(int(args[0]), int(args[1]))

        elif command == "delete":
            ll.delete(int(args[0]))

        elif command == "delete_at":
            ll.delete_at(int(args[0]))

        elif command == "print_list":
            ll.print_list()

if __name__ == "__main__":
    main()