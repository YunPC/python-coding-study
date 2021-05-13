## 풀이

### 49_Network_Delay_Time - 허재혁

> [https://leetcode.com/problems/network-delay-time/](https://leetcode.com/problems/network-delay-time/)

> k부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다. 입력값 (u, v, w)는 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.

```python
from collections import defaultdict
from typing import *
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = defaultdict(list)
        for time in times:
            u, v, w = time
            network[u - 1].append((w, v - 1))

        def dijkstra(start):
            distances = [float("inf")] * n
            heap = []
            heapq.heappush(heap, (0, start))
            distances[start] = 0

            while heap:
                dist, node = heapq.heappop(heap)
                adj_vs = network[node]

                if dist > distances[node]:
                    continue

                for distance, adj_v in adj_vs:
                    new_distance = dist + distance
                    if distances[adj_v] > new_distance:
                        distances[adj_v] = new_distance
                        heapq.heappush(heap, (new_distance, adj_v))

            return distances

        result = dijkstra(k - 1)
        max_value = max(result)
        if max_value == float("inf"):
            return -1
        return max_value
```
- k에서 출발하여 모든 노드까지 도달하는 최소 시간을 구하는 다익스트라 그 자체다.
- 위의 코드에서 참고할 만한 포인트는 defalutdict를 이용한 부분이다.
- 도달할 수 없는 경우는 노드의 dijkstra 메소드 안의 distances의 값 중 `float("inf")`가 포함돼있는 경우다. 이를 이용하여 도달 불가능한 경우를 스크린할 수 있다.