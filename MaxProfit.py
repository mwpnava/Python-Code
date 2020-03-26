'''
You are given an array of historical stock prices per day, for example:
[ 6 ,13 , 2, 10 , 3, 5]
Write an algorithm that figures out what days (index of array)
you could buy and sell the stock for maximum profit.
'''

def maxProfit(stock_prices):


    min_value = stock_prices[0]
    max_profit = 0
    current_profit = 0

    for s in stock_prices:

        min_value = min(min_value,s)
        current_profit = s - min_value
        max_profit = max(max_profit,current_profit)

    return max_profit


x = maxProfit([3,10,2,1,2,10])
print(x)
