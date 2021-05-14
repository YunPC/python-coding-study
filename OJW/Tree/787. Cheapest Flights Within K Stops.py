class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        q = [(src, 0, -1)]
        ans = inf
        cost = [inf]*n
        cost[src] = 0

        while len(q) > 0:
            u = q.pop(0)

            if u[0] == dst and u[2] <= k:
                ans = min(ans, u[1])

            if u[2] < k:
                for v in graph[u[0]]:
                    if cost[v[0]] > u[1] + v[1]:
                        cost[v[0]] = u[1] + v[1]
                        q.append((v[0], cost[v[0]], u[2] + 1))

        if ans == inf:
            return -1

        return ans
