'''
Problem 2: Implementation of Heap
'''
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Min_Heap:
    def __init__(self, verbose):
        self.root = None
        self.last = 0
        self.verbose = verbose #for print formatting


    def insert(self, value):
        if self.verbose:
            print(f"After insert({value}):")
        new_node = Node(value)

        if self.root is None:
            if self.verbose:
                print(value)
                print()
            self.root = new_node
            self.last = 1
            return

        #find parent and insert under
        parent, direction = self.find_last_open()

        new_node.parent = parent

        if direction == "0":
            parent.left = new_node
        else:
            parent.right = new_node

        self.last += 1

        self.heapify()
        if self.verbose:
            self.print_heap()


    def peek(self):
        if self.last == 0:
            raise IndexError("Heap is Empty")
        print("root", self.root.value)
        return self.root.value        

    
    def extract_min(self):
        if self.last == 0:
            raise IndexError("Heap is Empty")

        min_value = self.root.value
        last_node = self.find_last()

        # only one node in the heap
        if last_node is self.root:
            self.root = None
            self.last = 0
            return min_value

        # move the last node's value to the root, then detach the last node
        self.root.value = last_node.value
        if last_node.parent.right is last_node:
            last_node.parent.right = None
        else:
            last_node.parent.left = None
        last_node.parent = None
        self.last -= 1

        # sift down from the root until the heap is valid
        current = self.root
        while True:
            smallest = current

            if current.left and current.left.value < smallest.value:
                smallest = current.left
            if current.right and current.right.value < smallest.value:
                smallest = current.right

            if smallest is current:
                break

            current.value, smallest.value = smallest.value, current.value
            current = smallest

        return min_value


    def delete(self, value):
        if self.last == 0:
            print("False, value to delete not in heap")
            return False

        # find the target node (BFS, skipping subtrees whose root is
        # already bigger than value, since everything below it is bigger too)
        target = None
        queue = [self.root]
        while queue:
            node = queue.pop(0)

            if node.value == value:
                target = node
                break
            if node.value > value:
                continue

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if target is None:
            print("False, value to delete not in heap")
            return False

        last_node = self.find_last()

        # detach the last node from the tree
        if last_node is self.root:
            self.root = None
            self.last = 0
            print("True, deleted value: ", value)
            return True

        if last_node.parent.right is last_node:
            last_node.parent.right = None
        else:
            last_node.parent.left = None
        last_node.parent = None
        self.last -= 1

        # if the target was the last node, it's already gone
        if target is last_node:
            print("True, deleted value: ", value)
            return True

        # put the last node's value where the target was
        target.value = last_node.value

        # sift down
        current = target
        while True:
            smallest = current

            if current.left and current.left.value < smallest.value:
                smallest = current.left
            if current.right and current.right.value < smallest.value:
                smallest = current.right

            if smallest is current:
                break

            current.value, smallest.value = smallest.value, current.value
            current = smallest

        # sift up (needed when the target was in the middle of the tree and
        # the last node's value is smaller than the target's parent)
        current = target
        while current.parent and current.value < current.parent.value:
            current.value, current.parent.value = current.parent.value, current.value
            current = current.parent

        print("True, deleted value: ", value)
        return True


    def build(self, values):
        if self.verbose:
            print("Input values: ", values)
            print()
        for value in values:
            self.insert(value)


    def heap_sort(self):
        if self.last == 0:
            print("Heap Empty")
            return

        # collect all values in level order
        arr = []
        current_level = [self.root]
        while current_level:
            next_level = []
            for node in current_level:
                arr.append(node.value)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level

        # repeatedly remove the min from the copy
        res = []
        n = len(arr)
        while n > 0:
            res.append(arr[0])

            # move the last element to the front and shrink the array
            arr[0] = arr[n - 1]
            n -= 1

            # sift down from the front
            i = 0
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i

                if left < n and arr[left] < arr[smallest]:
                    smallest = left
                if right < n and arr[right] < arr[smallest]:
                    smallest = right

                if smallest == i:
                    break

                arr[i], arr[smallest] = arr[smallest], arr[i]
                i = smallest

        print(res)
        return res
        

    def is_empty(self):
        res = self.last == 0
        print(res)
        return res


    def length(self):
        print(self.last, " values")
        return self.last


    '''
    HELPER FUNCTIONS
    '''
    def heapify(self):
            current = self.find_last()
    
            while current.parent and current.value <= current.parent.value:
                #swap values
                current.value, current.parent.value = (
                    current.parent.value,
                    current.value
                )
                #set current to up-swapped node
                current = current.parent


    def find_last(self):
        if self.last == 1:
            return self.root
        
        bits = bin(self.last)[2:]
        node = self.root

        for bit in bits[1:]:
            if bit == "1":
                node = node.right
            else:
                node = node.left

            if node is None:
                return None

        #print(node.value)
        return node


    def find_last_open(self):
        next_index = self.last + 1
        bits = bin(next_index)[2:]

        parent_node = self.root

        #go to parent, skip first bc its the root
        #skip the last bit bc its the direction of insert
        for bit in bits[1:-1]:
            if bit == "1":
                parent_node = parent_node.right
            else:
                parent_node = parent_node.left

        #returns the parent, direction of insert
        return parent_node, bits[-1]


    def print_heap(self):
        if self.root is None:
            print("(empty heap)")
            return

        # nodes grouped by depth
        levels = []
        current = [self.root]
        while current:
            levels.append(current)
            current = [c for n in current for c in (n.left, n.right) if c]
        height = len(levels)

        # widest label
        w = max(len(str(n.value)) for level in levels for n in level)

        # d[L] = horizontal distance from a parent at depth L to each child
        # (d[L] - 1 slash rows are drawn between depth L and depth L + 1)
        # contour[node] = list of (min_x, max_x) per depth of that node's subtree,
        # relative to the node itself
        d = [2] * height
        contour = {}

        for L in range(height - 1, -1, -1):
            # tightest spacing that keeps sibling subtrees from touching
            need = 2
            for n in levels[L]:
                if n.left and n.right:
                    lc, rc = contour[n.left], contour[n.right]
                    for i in range(min(len(lc), len(rc))):
                        gap = w + 1 + lc[i][1] - rc[i][0]
                        need = max(need, (gap + 1) // 2)
            d[L] = need

            # build each node's contour from its children's contours
            for n in levels[L]:
                c = [(0, 0)]
                for child, sign in ((n.left, -1), (n.right, 1)):
                    if child:
                        for i, (lo, hi) in enumerate(contour[child]):
                            lo += sign * need
                            hi += sign * need
                            if i + 1 < len(c):
                                c[i + 1] = (min(c[i + 1][0], lo), max(c[i + 1][1], hi))
                            else:
                                c.append((lo, hi))
                contour[n] = c

        # absolute x position of every node (root at 0)
        pos = {self.root: 0}
        for L in range(height - 1):
            for n in levels[L]:
                if n.left:
                    pos[n.left] = pos[n] - d[L]
                if n.right:
                    pos[n.right] = pos[n] + d[L]

        shift = -min(pos.values()) + w // 2
        total_width = max(pos.values()) + shift + w + 1

        lines = []
        for L, level in enumerate(levels):
            # row of labels
            row = [" "] * total_width
            for n in level:
                s = str(n.value)
                start = pos[n] + shift - len(s) // 2
                row[start:start + len(s)] = s
            lines.append("".join(row).rstrip())

            if L == height - 1:
                break

            # slashes walk diagonally from each parent toward its children
            for k in range(1, d[L]):
                crow = [" "] * total_width
                for n in level:
                    x = pos[n] + shift
                    if n.left:
                        crow[x - k] = "/"
                    if n.right:
                        crow[x + k] = "\\"
                lines.append("".join(crow).rstrip())

        print("\n".join(lines))
        print()




def main():
    data = sys.stdin.read()
    cleaned = data.replace("[", " ").replace("]", " ").replace(",", " ")
    values = [int(x) for x in cleaned.split()]

    heap = Min_Heap(verbose=True)
    heap.build(values)

    heap.length()
    heap.peek()

if __name__ == "__main__":
    main()
            

