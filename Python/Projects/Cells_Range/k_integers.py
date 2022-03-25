def minimalKsum(nums, k):
    nums.sort()
    count = k
    result = 0
    

    if 1 not in nums:
        missing = nums[0] - 1
        if missing>count:
            result = ((count)*(count + 1 ))//2
            count = 0
        else:
            result = ((nums[0])*(nums[0]-1))//2
            count = count-missing
    
    i = 0
    while count>0 and i<len(nums)-1:
        missing = nums[i+1] - nums[i] - 1
        if missing>count:
            result = result + ((nums[i]+count)*(nums[i] + count +1))//2 - ((nums[i])*(nums[i]+1))//2
            count = 0
        else:
            if missing >0:
                result = result + ((nums[i+1])*(nums[i+1]+1))//2 - (((nums[i])*(nums[i]+1))//2 + nums[i+1])
                count =  count - missing
            i = i + 1
   
    j = 0
    if count>0:
        result = result + ((nums[len(nums)-1] + count)*(nums[len(nums)-1] +count + 1 ))//2 - ((nums[len(nums)-1])*(nums[len(nums)-1] + 1 ))//2
        count = 0

    
    return result

data = [int(ele) for ele in input().split()]
k = int(input())
print(minimalKsum(data, k))


