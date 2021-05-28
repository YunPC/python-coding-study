# 파이썬 알고리즘 인터뷰

## 리트코드 문제 풀이 폴더

### 2021.05.18(Sort)


### 문제 정의

연결 리스트를 O(nlogn)에 정렬하라


#### 풀이1

1. 모든 리스트의 값을 하나의 리스트에 받은 뒤, 리스트를 정렬한다.
2. 정렬한 리스트를 연결리스트로 변환한다.

```python
# Runtime: 220 ms, Memory Usage: 38.1 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        values = list()
        
        node = head
        
        while node:
            values.append(node.val)
            node = node.next
            
        values.sort()
        
        sorted_head = ListNode(values[0], None)
        sorted_node = sorted_head
        
        for i in range(1, len(values)):
            sorted_node.next = ListNode(values[i], None)
            sorted_node = sorted_node.next
            
        return sorted_head
```

### 문제정의 

평면상의 points 목록이 있을 때, 원점(0,0)에서 k번째 가까운 점 목록을 순서대로 출력하라. 평면 상 두 점의 거리는 유클리드 거리로 한다.

```python
# Runtime: 1032 ms, Memory Usage: 19.7 MB
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = list()
        
        for point in points:
            distance = point[0]**2 + point[1]**2
            distances.append((distance, point))
            
        distances.sort()
        
        l = len(distances)
        res = []
        
        for _, point in distances[:k]:
            res.append(point)
            
        return res
```

1. 점들을 입력받아 유클리드 거리의 제곱과 좌표를 튜플로 묶어서 리스트에 저장한다.
2. 리스트를 정렬한다.
3. 리스트에서 앞에서 k번째 좌표를 받아 리턴한다.
