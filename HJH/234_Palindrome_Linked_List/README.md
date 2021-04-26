## 풀이

## 234_Palindrome_Linked_List(p.201, [링크](https://leetcode.com/problems/palindrome-linked-list/)) - 허재혁

> 연결 리스트가 팰린드롬 구조인지 판별하라.


### naive 풀이
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return self.__solution1__(head)

    @staticmethod
    def __solution1__(head: ListNode):
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        if len(nodes) % 2 != 0:
            nodes.pop(len(nodes) // 2)

        while nodes:
            first, last = nodes.pop(0), nodes.pop()
            if first.val != last.val:
                return False

        return True
```
- 알고리즘 수업시간에 구현해보았던 링크드리스트 구조라서 눈에 익었다.
- 문제의 조건에 따르면 Singly Linked List로 ListNode가 구현되어 있으므로 링크드리스트를 순회하며 팰린드롬 여부를 파악하려면 시간복잡도가 크다.
- 따라서, 인덱싱이 가능한 일반 리스트에 노드의 정보를 추가하여 문제를 풀었다.
- 배열의 길이가 홀수인 경우, 중앙 인덱스의 값을 제거하여 짝수의 경우로 치환한 뒤, 팰린드롬 여부를 파악할 수 있다.
- *결과*: Runtime 1352 ms / Memory 47.2 MB

### deque 구조를 이용한 풀이
> 파이썬의 데크(deque)는 이중 연결 리스트 구조로 양쪽 방향을 추출하는 데 시간복잡도가 O(1)이다. 단일 연결 리스트 구조 순회 시 발생할 수 있는 문제를 해결할 수 있다.

```python
from typing import Deque
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return self.__solution2__(head)

    # Runtime 772 ms / Memory 47.4 MB
    @staticmethod
    def __solution2__(head: ListNode):
        nodes: Deque = collections.deque()
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        while len(nodes) > 1:
            first, last = nodes.popleft(), nodes.pop()

            if first.val != last.val:
                return False

        return True
```
- 문제풀이 구조는 위와 거의 유사하다. 다른 점은 데크의 길이가 홀수/짝수 구분없이 순회하지만 길이가 1보다 큰 경우에만 deque와 pop했다는 점이 눈여겨 볼만 하다.
- *결과*: Runtime 772 ms / Memory 47.7 MB