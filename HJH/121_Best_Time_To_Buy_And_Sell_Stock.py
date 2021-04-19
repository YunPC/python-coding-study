def maxProfit(prices):
    profit = 0
    min_price = float("inf")

    for p in prices:
        min_price = min(p, min_price)
        profit = max(profit, p - min_price)

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([2, 4, 1]))
