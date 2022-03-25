def find_duplicate(nums):
    end = len(nums)
    j = 0
    for i in range(end):
        j = nums[j]
    
    cycle_element = j
    cycle_size = 1

    for i in range(end):
        if nums[j] == cycle_element:
            break
        cycle_size = cycle_size + 1
        j = nums[j]
    
    k = 0
    for i in range(cycle_size):
        k = nums[k]
    
    tortois = 0
    hare =  k
    while tortois!=hare:
        tortois = nums[tortois]
        hare = nums[hare]
    
    return hare

print(find_duplicate([3,1,3,4,2]))
