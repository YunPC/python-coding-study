# 347. Top K Frequent Elements

## 문제 풀이

- counters 내부에서 정렬 사용이 안되는것 같았다. 우선순위큐(heapq) 를 사용하면 간단하게 풀이 가능하다는 생각도 들었지만, 나이브하게 정렬후 뒤에서 k 만큼 출력하는 것도 틀리지는 않을 것 같다.

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        answer = []

        # max heap 할려면 손이 더 가요.
        for num in count:
            heapq.heappush(heap, (-count[num], num))

        # hiphop
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])

        return answer

```
