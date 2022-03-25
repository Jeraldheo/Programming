def findKDistantIndices(nums, key, k) :
        end = len(nums)
        keys = []
        result = []
        for i in range(end):
            if nums[i]==key:
                keys.append(i)
        
        end_keys = len(keys)
        for i in range(end):
            for j in range(end_keys):
                if abs(i-keys[j])<=k:
                    result.append(i)
                    break
        result.sort()
        return result

data = [2,2,2,2,2]

print(findKDistantIndices(data, 2, 2))