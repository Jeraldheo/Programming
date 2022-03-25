from array import array


def first_last(target, arr):
    i = 0
    result = []
    for index in range(len(arr)):
        if arr[index] == target:
            result.append(index)

    if len(result)!=0:
        return [min(result), max(result)]
    return [-1,-1]





arr = [int(ele) for ele in input().split()]
target = int(input())
print(first_last(target, arr))