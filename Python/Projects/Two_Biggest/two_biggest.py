def two_biggest(nums):
    size = len(nums)
    max_index = 0
    for i in range(1, size):
        if nums[max_index]<nums[i]:
            max_index = i
    if max_index == size-1:
        print(nums[max_index])
        return
    top = -1
    for i in range(size):
        if top<nums[i] and i!=max_index:
            top = nums[i]
    print(nums[max_index])
    print(top)

two_biggest([5,2,2,4,6,0])