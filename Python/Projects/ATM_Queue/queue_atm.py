import math

def getFinalOrder(k, amount):
    # Write your code here
    timesQ = dict()
    n = len(amount)
    for i in range(n):
        times = math.ceil(amount[i]/k)
        if times in timesQ:
            timesQ[times].append(i+1)
        else:
            timesQ[times]=[i+1]
    keys = list(timesQ.keys())
    keys.sort()
    result = []
    for key in keys:
        result = result + timesQ[key]

    return result

n = int(input())
data = [int(data) for data in input().split()]
getFinalOrder(n, data)

