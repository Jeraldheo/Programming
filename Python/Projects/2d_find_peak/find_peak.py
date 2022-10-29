def find_max(array):
    max_element_index = 0
    size = len(array)
    for i in range(size):
        if array[i]>array[max_element_index]:
            max_element_index = i
    return max_element_index
    
def findPeakElement(mat): 
    num_rows = len(mat) 
    end = len(mat[0])-1
    start = 0
    row_index = 0
    while start<=end:
        col_index = (start + end)//2
        half_column = [mat[i][col_index] for i in range(num_rows)]
        row_index = find_max(half_column)

        left = col_index - 1
        if left>=start and mat[row_index][left]> mat[row_index][col_index]:
            end = left
            continue

        right = col_index + 1
        if right<=end and mat[row_index][col_index]<mat[row_index][right]:
            start = right
            continue

        return [row_index, col_index]

    return [row_index, start]

print(findPeakElement([[1,2,6],[3,4,5]]))