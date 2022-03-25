def topmost_kmoves(nums, k):
    if k == 0:
        return nums[0]
    
    size = len(nums)

    if size ==1 and k%2!=0:
        return -1
    
    if size <k:
        return max(nums)
        
    if size == k:
        max_index = 0
        for i in range(1, size):
            if nums[max_index]<nums[i]:
                max_index = i
        if max_index!=size-1:
            return nums[max_index]
        
        top = -1
        for i in range(size):
            if top <nums[i] and i!=max_index:
                top = nums[i]
        return top
    
    if size > k:
        if k == 1:
            return nums[1]
        
        max_pop = max(nums[:k-1])
        return max(max_pop, nums[k])

print(topmost_kmoves([2], 1))