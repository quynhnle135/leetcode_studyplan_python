def maxProfit(prices):
    min = 10000
    max = 0
    for i in range(0, len(prices)):
        if prices[i] < min:
            min = prices[i]
        current = prices[i] - min
        if current > max:
            max = current
    return max


prices = [7, 1, 6, 4, 3, 1]
print(maxProfit(prices))