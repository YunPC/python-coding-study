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
