from math import floor



def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left != right:
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
            return left - 1


target = int(input())
data = [int(ele) for ele in input().split()]
print(binary_search(data, target))