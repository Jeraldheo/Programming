import math
from queue import Empty, Queue
from turtle import right


def reflexion(binary_tree, node):
    node_height = math.floor(math.log2(node + 1))
    return binary_tree[int(3*(2**node_height - 1) - node)]

def right_child(parent):
    return 2*parent + 2

def left_child(parent):
    return 2*parent + 1

def check_symmetry(binary_tree):
    if len(binary_tree) == 1:
        return True
    buffer = Queue()
    buffer.put(1)
    while not buffer.empty():
        node = buffer.get()

        if binary_tree[node] != reflexion(binary_tree, node):
            return False
        
        right = right_child(node)
        left = left_child(node)

        if right<len(binary_tree):
            buffer.put(right)

        if left<len(binary_tree):
            buffer.put(left)
    return True

data = [int(ele) for ele in input().split()]
print(check_symmetry(data))