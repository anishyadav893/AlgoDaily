# This is my solution for AlgoDaily problem Stock Buy and Sell Optimization
# Located at https://algodaily.com/challenges/stock-buy-and-sell-optimization

def stockOptimizer(prices):
    maxPrice = prices[-1]
    maxProfit = 0
    
    for i in range(len(prices) - 1, -1, -1):
        temp = prices[i]
        if temp > maxPrice:
            maxPrice = temp
        
        profit = maxPrice - temp
        
        if profit > maxProfit:
            maxProfit = profit
    return maxProfit