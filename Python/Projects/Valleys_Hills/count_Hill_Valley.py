def neighbor(data, key):
        end = len(data)
        for i in range(end):
            if data[i] !=key:
                return data[i]
        return False
    
def countHillValley(nums):
        end = len(nums)
        result = 0
        for i in range(1, end):
            if nums[i]!=nums[i-1]:
                left_array = nums[:i]
                left_array.reverse()
                left = neighbor(left_array,nums[i])
                right =  neighbor(nums[i+1:],nums[i])
                if left == False or right == False:
                    continue
                
                if left<nums[i] and right<nums[i]:
                    result = result + 1
                
                if left>nums[i] and right>nums[i]:
                    result = result + 1
        return result


print(countHillValley([8,2,5,7,7,2,10,3,6,2]))