import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse_binary_tree(binary_tree, root):
    buffer = queue.Queue()
    array_tree = []
    buffer.put(root)
    while not buffer.empty():
        node = buffer.get()
        array_tree.append(node)
        if node in binary_tree:
            buffer.put(binary_tree[node][0])
            buffer.put(binary_tree[node][1])

    end = len(array_tree)-1
    while array_tree[end] == 'null':
        array_tree.pop()
        end = len(array_tree)-1

    return array_tree


def create_binary_tree(description):
    
    parent_kids = dict()
    kids = set()
    end = len(description)
    for i in range(end):
        node = description[i]
        parent = node[0]
        if parent in parent_kids:
            if node[2] == 1:
                parent_kids[parent][0] = node[1]
            else:
                parent_kids[parent][1] = node[1]
        else:
            if node[2] == 1:
                parent_kids[parent] = [node[1], "null"]
            else:
                parent_kids[parent] = ["null", node[1]]
        kids.add(node[1])
    
    parents = set(list(parent_kids.keys()))
    root = list((parents - kids))[0]
    return traverse_binary_tree(parent_kids, root)

    

data = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
print(create_binary_tree(data))