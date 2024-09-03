def maxProfit(prices: list[int]) -> int:
    min_so_far = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        min_so_far = min(min_so_far, prices[i])
        profit = prices[i] - min_so_far
        max_profit = max(profit, max_profit)
    return max_profit

arr = [7,1,5,3,6,4]
print(maxProfit(arr))