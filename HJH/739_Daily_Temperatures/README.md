## 풀이

## 739_Daily_Temperatures(p.252, [링크](https://leetcode.com/problems/daily-temperatures/)) - 허재혁

> 매일의 화씨 온도 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

### naive 풀이
```python
from typing import List
import collections


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        return self.__solve_with_stack(T)
        pass

    # Time Limit Exceeded
    @staticmethod
    def __solve_with_queue(T):
        queue: collections.deque = collections.deque()
        answer = []

        for temperature in T:
            queue.append(temperature)

        while queue:
            popped = queue.popleft()
            interval = 1
            warmer = False

            for rest_temperature in queue:
                if popped < rest_temperature:
                    warmer = True
                    break
                interval += 1

            if warmer:
                answer.append(interval)
            else:
                answer.append(0)

        return answer
```
- 리스트의 엘리먼트를 deque 구조에 담아 하나씩 빼고 그 뒤에 값 중에서 deque에서 뺀 값과 비교해가는 방식으로 접근하였다.
- deque의 popleft 메소드는 시간복잡도로 O(1)로 속도가 빨라 통과할 것이라고 생각했으나 **시간초과**로 통과하지 못했다.


### stack을 이용한 풀이
```python
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        return self.__solve_with_stack(T)
        pass

    # Runtime 516 ms / Memory 19 MB
    @staticmethod
    def __solve_with_stack(T):
        answer = [0] * len(T)
        stack = []

        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] > T[stack[-1]]:
                stack.pop()
            if stack:
                answer[i] = stack[-1] - i
            stack.append(i)
        return answer
```
- 답지를 슬며시 보았다.
- 현재의 인덱스를 스택에 쌓아두는데 만약 현재 인덱스의 온도가 스택의 마지막 인덱스의 온도가 높다면(더 따뜻한 날씨인 경우 -> 조건 충족) 스택이 비거나 현재 인덱스의 온도가 스택의 마지막 인덱스의 온도보다 크지 않을때까지 pop()을 반복한다.
- 만약, 스택이 비어있지 않다면(현재 인덱스의 온도가 스택의 마지막 인덱스의 온도보다 낮을 경우) 현재 남아있는 스택의 마지막 요소에서 현재의 인덱스를 뺀 값을 answer에 저장한다.

1. i == 7

| list | elements |
| ---- | ---- |
| answer | 0 0 0 0 0 0 0 |
| stack | 7 |
   
2. i == 6

| list | elements |
| ---- | ---- |
| answer | 0 0 0 0 0 0 0 |
| stack | ~~7~~ 6 |

3. i == 5

| list | elements |
| ---- | ---- |
| answer | 0 0 0 0 1 0 0 |
| stack | ~~7~~ 6 5 |

4. i == 4

| list | elements |
| ---- | ---- |
| answer | 0 0 0 1 1 0 0 |
| stack | 6 5 4 |

