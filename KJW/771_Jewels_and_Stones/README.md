# 보석과 돌

> 보석 배열과 돌 배열을 문자열로 받아서 돌 안에 보석이 몇 개 포함되어 있는지 반환한다

파이썬의 Set을 사용해 보석 문자열을 set으로 변환 한 뒤 stones 문자열을 순회하여 jewels set 안에 요소와 몇 번 중복되는지 확인하면 된다.

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        result = 0
        for stone in stones:
            if stone in jewels_set:
                result += 1
        return result
```

문제가 쉽기도 해서 딱히 어려움 없이 풀었다. 시간복잡도는 O(N)으로 풀 수 있다.
