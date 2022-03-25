#O(n)
def two_sum(nums, target):
    end = len(nums)
    second = dict()
    for i in range(end):
        if nums[i] in second:
            second[nums[i]].append(i)
            return second[nums[i]]
        second[target-nums[i]] = [i]

print(two_sum([2,7,11,15], 9))