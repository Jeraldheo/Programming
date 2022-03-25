from math import floor

def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left < right:
        i = floor((left + right)/2)
        
        if arr[i] == target:
            return i
        else:
            if arr[i]<target:
                left = i + 1
            else:
                right = i-1

    
    if arr[left] == target:
            return left
    else:
        if arr[left] < target:
            return left + 1
        else:
            return left 

def length_LIS(seq):
    piles = [seq[0]]
    size = len(seq)
    for i in range(1, size):
        if seq[i] == piles[0]:
            piles[0] = seq[i]
        else:
            if seq[i]>piles[len(piles)-1]:
                piles.append(seq[i])
            else:
                pile_i = binary_search(piles,seq[i])
                piles[pile_i] = seq[i]
    
    return len(piles)



data = [int(ele) for ele in input().split()]
print(length_LIS(data))
