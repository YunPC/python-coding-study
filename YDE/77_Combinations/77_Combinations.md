# 문제 정의

전체 수 n을 입력받아 k개의 조합을 리턴하라

## itertools를 활용한 풀이

```python
# Runtime: 72 ms
# Memory Usage: 15.7 MB
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        return list(combinations([i for i in range(1, n+1)], k))
```

## DFS

1부터 순서대로 for문을 반복하되, 재귀호출에 조합에 올 수 있는 값을 넣고 재귀호출을 한다. 남아 있는 값끼리 나머지 조합을 수행하게 되며, k=0이 되면 결과에 삽입한다. 

```python
def combine(self, n:int, k:int) -> List[List[int]]:
    results = []

    def dfs(elements, start:int, k:int):
        if k == 0:
            results.append(elements[:])

        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()

    dfs([], 1, k)
```
