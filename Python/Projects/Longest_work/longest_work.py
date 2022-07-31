def findLongestSingleSlot(leaveTimes):
    # Write your code here
    ids = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num_nurses = len(ids)
    identification = dict()
    for i in range(0, num_nurses):
        identification[i] = ids[i]
    
    nurse = 0
    max_shift = leaveTimes[0][1]-leaveTimes[0][0]
    num_shifts = len(leaveTimes)
    for i in range(0, num_shifts):
        shift = leaveTimes[i][1] - leaveTimes[i-1][1]
        if shift>max_shift:
            max_shift = shift
            nurse = leaveTimes[i][0]

    return identification[nurse]

print(findLongestSingleSlot([[0,3], [2,5], [0,9], [1,15]]))