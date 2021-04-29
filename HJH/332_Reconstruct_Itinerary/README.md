## 풀이

### 332_Reconstruct_Itinerary - 허재혁

> [https://leetcode.com/problems/reconstruct-itinerary](https://leetcode.com/problems/reconstruct-itinerary)

> [from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라. 여러 일정이 있는 경우 사전 어휘 순으로 방문한다.

**나의 풀이(실패)**
```python
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_dict = defaultdict(list)
        for idx, ticket in enumerate(sorted(tickets, key=lambda x: x)):
            start, dest = ticket
            tickets_dict[start].append(dest)

        answer = []

        def dfs(s):
            answer.append(s)
            destinations = tickets_dict[s]
            
            while destinations:
                first = destinations.pop(0)
                if first in tickets_dict:
                    dfs(first)
                else:
                    tickets_dict[first] = [first]

        dfs("JFK")

        for key in tickets_dict:
            if tickets_dict[key]:
                answer.append(tickets_dict[key][0])

        return answer
```
- 문제풀이전략
    1. 인접리스트를 dictionary, 그 중 저번시간에 살펴보았던 defaultdict(tickets_dict)로 구성한다.
    1. 여려 일정이 있는 경우, 사전순으로 구성해야 하므로 defaultdict를 구성할 때, 목적지 리스트를 사전 순으로 정렬하여 구성한다.
    1. JFK를 최초의 출발지로 설정하고 목적지를 다음 출발지로 갖는 항공표에 대해서 동일한 과정을 수행하는 dfs 함수를 구성한다.
    1. 목적지가 있는 동안 목적지 리스트(destinations)에서 앞에서 pop한 목적지가 tickets_dict에 키로 존재할 경우, 해당 목적지에 대해 dfs를 실행한다.
    1. key로 존재하지 않을 경우, 그것은 최종 목적지이므로 이를 tickets_dict에 {"key": ["key"]}로 추가한다.
    1. 마지막으로 tickets_dict에 아직 추가되지 않은 목적지(최종 목적지)를 answer에 마지막에 추가해준다.

- 실패케이스
```python
[["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
```

- 실패 원인
    - 5번에서 원인이 있다. 최종 목적지로 여러 개가 될 수 있는데 이에 대한 고려없이 마지막에서 순서대로 추가해주었다.
    
**솔루션(답)**
```python
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        return route[::-1]
```
- 분석
    1. 초기 구성의 로직은 유사하다. 그러나 graph를 구성하는 방식이 다르다. 위의 솔루션에서는 사전 어휘순 반대로 목적지 리스트를 구성한다.
    1. dfs 함수 안에서 while문 안은 같이 해보면서 분석해보면 좋을 듯 하다.
    
*Runtime 84 ms / Memory 14.8 MB*