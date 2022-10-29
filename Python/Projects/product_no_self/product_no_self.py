def productExceptSelf(nums):
    num_zeros = nums.count(0)
    non_zero_product = 1
    size = len(nums)
    answer = [0]*size
    if num_zeros>1:
        return answer
    for num in nums:
        if num!=0:
            non_zero_product*=num

    if num_zeros == 1:
        for i in range(size):
            if nums[i] == 0:
                answer[i] = non_zero_product
                continue
            answer[i] = 0
        return answer
    else:
        for i in range(size):
            answer[i] = non_zero_product//nums[i]
        return answer

            

print(productExceptSelf([-1,1,0,-3,3]))