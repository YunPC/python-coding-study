# 242. Valid Anagram
## 문제

- 애너그램이 되는지 찾는 문제이다. 주어진 문자열로 같은 문자를 만들 수 있는지 찾는다.

## 코드

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```
## 풀이

- 만약 처음 문자열로 만들 수 있는 단어라면, 같은 알파벳과 개수를 가지고 있지 않을까? 하는 생각에서 시작된 풀이이다. 정렬하고 비교만 해주면 될 것이다라고 생각했고 됬다.

# 147. Insertion Sort List
## 문제
- 단일 연결리스트에서 삽입 정렬을 구현하는 문제다.

## 코드
```python
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(None)
        
        while head:

            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next
            
            cur = parent
            
        return cur.next
```

## 풀이

- 그림을 그리면서 풀이를 따라가 보도록 하자!