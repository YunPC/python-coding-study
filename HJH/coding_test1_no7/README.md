# 7번 문항

## 1. 문제

상언이는 친구들을 속이는 재미를 뒤늦게 깨닫고, 거짓말을 하기로 하였다.
상언이는 단 한번의 거짓말로 모든 친구들을 속이고자 한다. 한 친구가
거짓말을 믿게 되면, 친한 친구들은 일정 시간 후에 거짓말을 믿게 된다. 이 때,
모든 친구가 거짓말을 믿게 되는 데에 걸리는 시간을 계산하시오. 모든 친구가
거짓말을 믿을 수 있게 할 수 없으면 -1을 반환하시오.
단, 상언이는 항상 0번째 친구에게 거짓말을 하며, edges의 i번째 요소는 [친한
친구의 인덱스, 거짓말이 전해지는데 걸리는 시간]의 리스트로 이루어져 있다.
상언이의 친구는 총 N명이며, N은 0 < N <= 1000을 만족한다.

## 2. 입출력 예시

**#1**

| N | edges | 출력 |
| ---- | ---- | ---- |
| 5 | [[(2, 4), (3, 1)], [(4, 2), (0, 4)], [(1, 4)], [(4, 1)], [(3, 7)]] | 8 |

**#2**

| N | edges | 출력 |
| ---- | ---- | ---- |
| 6 | [[(1, 3), (5, 1)], [(3, 5), (0, 2)], [(4, 3)], [(1, 1)], [(3, 6)], [(3, 2)]] | -1 |

- Dijkstra 알고리즘을 이용하여 시작점 0으로부터 다른 모든 노드까지의 경로의 최단거리를 계산하면 된다.
- 각 정점까지의 최단거리의 최대값이 모든 친구가 거짓말을 믿게 하는 데에 걸리는 최소 시간이다. 모든 정점의 거리를 infinity로 초기화하고 다익스트라 알고리즘을 거치고 난 뒤에도 infinity값이 있으면 비연결 그래프로 판별할 수 있다. 
- Minimum Spanning Tree로도 풀 수 있을 듯 하다.

**나의 풀이**

```python
import heapq


def dijkstra(N, graph):
    heap = []
    distances = [float("inf") for _ in range(N)]
    distances[0] = 0
    heapq.heappush(heap, (0, 0))

    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distances[node]:
            continue

        for adj_v_idx, distance in graph[node]:
            new_distance = distances[node] + distance
            if new_distance < distances[adj_v_idx]:
                distances[adj_v_idx] = new_distance
                heapq.heappush(heap, (new_distance, adj_v_idx))

    if float("inf") in distances:
        return -1

    return max(distances)
```