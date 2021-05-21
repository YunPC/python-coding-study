# 풀이

## [215_Kth-Largest-Element-In-An-Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) - 허재혁

### Naive

```python
import heapq
from typing import List

class Solution:
    def naive(self, nums: List[int], k: int) -> int:
        heap = []

        while nums:
            num = nums.pop()
            heapq.heappush(heap, (-1 * num, num))

        cnt = 0
        while True:
            cnt += 1
            popped = heapq.heappop(heap)
            if cnt == k:
                return popped[1]
```

- `nums`를 오름/내림차순하여 충분히 풀 수 있는 문제이나 힙을 이용한 우선순위 큐를 이용하여 풀어보았다.
- heapq.heappush 메서드는 기본적으로 min_heap을 기반으로 하므로 max_heap으로 구현하기 위해서는 num에 -1을 곱한 값을 가중치로 줘 heapq.heappush()한다.
- 이 후, k번째 수까지 heapq.heappop()한다.
- Runtime 76ms / Memory 15.2MB

### Solution

```python
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
```

- heapq.heapify 메서드를 이용하면 이터러블 객체를 min_heap 구조로 초기화해준다....
- 나머지 로직은 동일하다.
- Runtime 52ms / Memory 14.9MB
