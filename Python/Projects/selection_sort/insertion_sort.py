def insertion_sort(data):
    n = len(data)
    for i in range(1,n):
        current_element = data[i]
        j = i-1
        while current_element<data[j] and j>=0:
            data[j + 1] = data[j]
            data[j] = current_element
            j = j-1

    print(data)


insertion_sort([1,2,3])