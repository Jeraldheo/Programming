def brokenCalc(startValue, target):
    if startValue == target:
        return 0
    else:
        if target < startValue:
            return startValue - target
        else:
            curr_t = target
            num_steps = 0
            while curr_t!=startValue:
                num_steps+=1
                if curr_t%2==0:
                    temp = int(curr_t/2)
                    if temp<startValue:
                        num_steps = num_steps + (startValue-temp)
                        curr_t = startValue
                    else:
                        curr_t = temp
                else:
                    curr_t = curr_t + 1
        
            return num_steps



    
print(brokenCalc(1,1))
