# 문제 정의

연결 리스트를 뒤집는 문제이다.

## 풀이1

반복 구조를 이용하여 뒤집기

1. 모든 연결리스트의 값을 리스트에 저장한다.
2. 리스트에 저장한 값을 역순으로 접근하여 새로운 연결리스트를 생성한다.

```python
# Runtime: 36 ms, Memory Usage: 16.3 MB
def solution1(head):
    if head.val is None:
            return ListNode('')
        
    values = []

    while head:
        values.append(head.val)
        head = head.next
        
    list_node = ListNode()    
    start = list_node
    
    for v in values[::-1]:
        start.next = ListNode(v)
        start = start.next
        
    return list_node.next
```

## 풀이2

재귀로 뒤집기

1. 다음 노드와 현재 노드를 파라미터로 하는 재귀함수를 생성한다.
2. node.next에 이전 prev리스트를 연결하면서 node가 None이 될 때까지 재귀호출을 한다.

```python
# Runtime: 28ms, Memory Usage: 20.5MB
def solution2(head):
    def reverse(node, prev=None):
        if not node:
            return prev

        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)
```