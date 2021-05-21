# 풀이

## [56_Merge-Intervals](https://leetcode.com/problems/merge-intervals/) - 허재혁

### naive

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        curr = 0
        while True:
            if curr >= len(intervals) - 1:
                return intervals
            if intervals[curr][1] >= intervals[curr + 1][0]:
                popped = intervals.pop(curr + 1)
                if intervals[curr][1] < popped[1]:
                    intervals[curr][1] = popped[1]
            else:
                curr += 1
```

- 먼저, interval의 start가 작은 순으로 정렬한다.
- while문 안에서 List intervals의 요소를 앞뒤로 비교한다.
- 만약, 앞 쪽의 end가 뒤 쪽의 start보다 클 경우 병합이 가능하다.
- 병합 과정에서 앞 쪽의 end와 뒷 쪽의 end가 큰 요소를 end에 할당해준다.
- 위 과정을 마지막 index 전까지 반복한다.
- Runtime 96ms / Memory 16.2MB
