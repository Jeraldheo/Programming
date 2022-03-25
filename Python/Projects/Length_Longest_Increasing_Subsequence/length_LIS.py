from math import floor

def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left != right:
        i = floor((left + right)/2)
        top = len(arr[i])-1
        if arr[i][top] == target:
            return i
        else:
            if arr[i][top]<target:
                left = i + 1
            else:
                right = i-1

    top = len(arr[left]) - 1
    if arr[left][top] == target:
            return left
    else:
        if arr[left][top] < target:
            return left + 1
        else:
            return left 

def length_LIS(seq):
    piles = [[seq[0]]]
    size = len(seq)
    for i in range(1, size):
        if seq[i] == piles[0][0]:
            piles[0][0] = seq[i]
        else:
            if seq[i]>piles[len(piles)-1][len(piles[len(piles)-1])-1]:
                piles.append(piles[len(piles)-1][:])
                piles[len(piles)-1].append(seq[i])   
            else:
                pile_i = binary_search(piles,seq[i])
                top = len(piles[pile_i])-1
                piles[pile_i][top] = seq[i]

    last_pile = len(piles) - 1
    
    return len(piles[last_pile])



data = [int(ele) for ele in input().split()]
print(length_LIS(data))
