import queue

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
    
    print(array_tree)

data = {20: [15, 17], 50: [20, 80], 80: [19, 'null']}
traverse_binary_tree(data,50)
    
