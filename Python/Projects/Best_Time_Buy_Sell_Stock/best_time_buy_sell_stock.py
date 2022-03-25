#complexity O(n^2)
def best_time_buy_sell(data):
    profit = 0
    end = len(data)
    for i in range(end):
        for j in range(i+1, end):
            temp_profit = data[j] - data[i]
            if temp_profit> profit:
                profit = temp_profit
    
    return profit


data = [7,1,5,3,6,4]
print(best_time_buy_sell(data))

