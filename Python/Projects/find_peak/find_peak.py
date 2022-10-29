from turtle import right


def findPeakElement(nums):  
    end = len(nums)-1
    start = 0
    while start<end:
        pointer = (start + end)//2
        left = pointer - 1
        if left>=start and nums[pointer]<nums[left]:
            end = left
            continue
        right = pointer + 1
        if right<=end and nums[pointer]<nums[right]:
            start = right
            continue
        return pointer
    return start

print(findPeakElement([4]))