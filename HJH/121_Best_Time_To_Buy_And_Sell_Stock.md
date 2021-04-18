## 풀이

### 121_best_time_to_buy_and_sell_stock(p. 195)  - 허재혁

> [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
> 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

**접근**
브루트 포스로 모든 경우의 수를 계산하면 쉽게 풀릴 문제이지만 좀만 생각하면 더 좋은 성능으로 풀 수 있는 문제였다.
```python
def maxProfit(prices):
    profit = 0
    min_price = float("inf")

    for p in prices:
        min_price = min(p, min_price)
        profit = max(profit, p - min_price)

    return profit
```
문제 풀이 전략은 다음과 같다.
1. 현재 최소 가격(min_price)을 먼저 무한으로 설정한다.
1. prices에 대하여 for 문을 돌며 min_price를 현재 가격(p)과 비교하여 최소값으로 재할당한다.
1. 이 때 발생하는 이익을 계속 최대값으로 갱신한다.

어렵지 않게 풀 수 있는 문제였다.