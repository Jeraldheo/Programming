#complexity O(n)
def best_time_buy_sell(data):
    profit = 0
    my_stock = data[0]
    end = len(data)
    for i in range(1,end):
        temp_profit = data[i] - my_stock
        if temp_profit>0:
            if temp_profit> profit:
                profit = temp_profit
        else:
            my_stock = data[i]
    
    return profit


data = [7,6,4,3,1]
print(best_time_buy_sell(data))

