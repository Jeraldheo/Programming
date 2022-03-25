#O(n^2)
def two_sum(nums, target):
    end = len(nums)
    for i in range(end-1):
        for j in range(1,end):
            if (nums[i] + nums[j])==target:
                return [i, j]


print(two_sum([2,7,11,15], 9))