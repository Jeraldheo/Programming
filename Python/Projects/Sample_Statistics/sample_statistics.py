from math import ceil

def sampleStats(count):
    n = len(count)
    minimum = 0
    for i in range(n):
        if count[i]!=0:
            minimum = i
            break
    
    maximum = 0
    for j in range(n):
        if count[j]!=0:
            maximum = j

    total_sum = 0
    num_ele = 0
    mean = 0
    for k in range(n):
        if count[k]!=0:
            total_sum += count[k]*k
            num_ele += count[k]

    mean = total_sum/num_ele      
    
    
    half = ceil(num_ele/2)
    curr_count = 0
    temp_median = 0
    for t in range(n):
        curr_count+=count[t]
        if curr_count>=half:
            temp_median = t
            break                        
    
    if num_ele%2 ==0:
        if curr_count==half:
            second_med = 0
            for r in range(temp_median + 1, n):
                if count[r]!=0:
                    second_med = r
                    break
            median = (temp_median + second_med)/2
        else:
            median = temp_median
    else:
        median = temp_median
    
    max_apperance = 1
    mode  = 0
    for s in range(n):
        if count[s]>max_apperance:
            max_apperance = count[s]
            mode =s

    return [minimum, maximum, round(mean, 3), round(median, 3), mode]

print(sampleStats([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))

