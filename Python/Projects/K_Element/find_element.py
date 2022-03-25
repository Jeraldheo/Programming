arr = [int(ele) for ele in input().split()]
k = int(input())

arr.sort(reverse=True)
print(arr[k-1])