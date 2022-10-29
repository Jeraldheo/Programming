def max_prod_no_zero_odd(array, last_negative):
    if len(array)==1:
        return array[0]
    left_right_prod = 1
    element = 0
    while element<last_negative:
        left_right_prod = left_right_prod*array[element]
        element+=1
    return left_right_prod

def max_prod_no_zero_even(array):
    max_product = 1
    for element in array:
        max_product*=element
    return max_product

def count_negatives(array):
    num_negatives = 0
    for element in array:
        if element<0:
            num_negatives+=1
    return num_negatives

def max_prod_no_zero(array):
    num_negatives = count_negatives(array)
    if num_negatives%2==0:
        return max_prod_no_zero_even(array)
    
    last_negative = -1
    last_negative_reverse = -1
    for i in range(len(array)):
        if array[i]<0:
            last_negative = i
            if last_negative_reverse == -1:
                last_negative_reverse = i

    last_negative_reverse = len(array)-last_negative_reverse -1
    data_reverse = array[::-1]
    max_prod_left_right = max_prod_no_zero_odd(array,last_negative)
    max_prod_right_left = max_prod_no_zero_odd(data_reverse,last_negative_reverse)

    return max(max_prod_left_right, max_prod_right_left )


A = [3,-1,4]
size = len(A)
max_prod = 0
start = 0
while start < size:
    if A[start] == 0:
        start+=1
        continue
    end = start
    while end + 1<size and A[end + 1]!=0:
        end+=1
    non_zero = A[start: end + 1]
    max_prod = max(max_prod, max_prod_no_zero(non_zero))
    start = end +1

print(max_prod)
