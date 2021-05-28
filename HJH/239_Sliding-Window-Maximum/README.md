# 풀이

## ![https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/) - 허재혁

### 나의 풀이

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        start = 0

        while start + k <= len(nums):

            res.append(max(nums[start:start+k]))
            start += 1

        return res
```

- Runtime N/A / Memory N/A

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        window = deque()
        current_max = float('-inf')

        for i in range(len(nums)):
            window.append(nums[i])
            if i < k - 1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif nums[i] > current_max:
                current_max = nums[i]

            res.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')

        return res
```

- Runtime N/A / Memory N/A
