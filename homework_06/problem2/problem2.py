'''
Problem 2: Implementation of Heap
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Min_Heap:
    def __init__(self):
        self.root = None
        self.last = 0


    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
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


    def peek(self):
        return self.root.value        


    def build(self, values):
        for value in values:
            self.insert(value)


    def delete(self, value):
        return True


    def heap_sort(self):
        if self.is_empty():
            print("Heap Empty")
            return

        levels = len(bin(self.last)[2:])
        current_level = [self.root]

        res = []

        for i in range(levels):
            res += current_level
            
            next_level = []

            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level

        res1 = sorted([node.value for node in res])
        print(res1)
        return res1
        

    def is_empty(self):
        res = self.last == 0
        print(res)
        return res


    def length(self):
        print(self.last)
        return self.last


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

        print(node.value)
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

    
    


def main():
    values = [1, 10, 9, 8, 5, 3, 2, 4, 5, 5]
    heap = Min_Heap()

    heap.build(values)
    heap.print_heap()    
    heap.is_empty()
    heap.length()
    heap.find_last()
    heap.heap_sort()


if __name__ == "__main__":
    main()
            

