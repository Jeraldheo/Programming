def number_binary_search_trees(n):
    nodes  = list(range(1, n+1))
    
    num_trees = [1]
    for i in range(n):
        count = 0
        for j in range(i+1):
            back = j
            front = (i + 1) - (j+1)
            count = count + num_trees[back]*num_trees[front]
        num_trees.append(count)
    
    return num_trees[len(num_trees)-1]

n = int(input())
print(number_binary_search_trees(n))