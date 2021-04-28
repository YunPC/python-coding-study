# 문제 정의

정렬되어 있는 두 연결리스트를 합치는 문제이다.

## 풀이

### 풀이1

1. 모든 리스트의 값을 하나의 리스트에 받은 뒤, 리스트를 정렬한다.
2. 정렬한 리스트를 연결리스트로 변환한다.

```python
# Runtime: 40 ms, Memory Usage: 14.4 MB
def solution1(l1, l2):
    nodes = []
        
    node = l1
    
    while node is not None:
        nodes.append(node.val)
        node = node.next
        
    node = l2
    
    while node is not None:
        nodes.append(node.val)
        node = node.next
        
    if len(nodes) == 0:
        return ListNode('')
    
    nodes.sort()
    
    list_node = ListNode(nodes[0])
    
    head = list_node
    
    for i in range(1, len(nodes)):
        head.next = ListNode(nodes[i])
        head = head.next
        
    return list_node
```

## 풀이2

1. 합병정렬에서 아이디어를 얻어 두 연결리스트 중 작은 값을 가져와 새로운 연결리스트에 연결한다.

2. 만약 기존의 두 연결리스트 중 하나가 먼저 끝에 도달했을 경우, 나머지 리스트의 값을 더한다.

```python
# Runtime: 60 ms, Memory Usage: 14.4 MB
def solution2(l1, l2):

    if l1.val == '' and l2.val == '':
            return ListNode('')
    
    list_node = ListNode('')

    head = list_node

    while l1 or l2:
        
        if l1 is None:
            
            if head.val == '':
                head.val = l2.val
            else:
                head.next = ListNode(l2.val)
                head = head.next
            
            l2 = l2.next
            
        elif l2 is None:
            
            if head.val == '':
                head.val = l1.val
            else:
                head.next = ListNode(l1.val)
                head = head.next
            
            l1 = l1.next
            
        else:
            if l1.val <= l2.val:
                
                if head.val == '':
                    head.val = l1.val
                else:
                    head.next = ListNode(l1.val)
                    head = head.next
                    
                l1 = l1.next
                
            else:
                if head.val == '':
                    head.val = l2.val
                else:
                    head.next = ListNode(l2.val)
                    head = head.next
                    
                l2 = l2.next
                    
    return list_node
```

## 풀이3

풀이2를 재귀형태로 변환한다. 주어진 두 리스트 중 작은 값이 왼쪽에 오게 하고, next는 그 다음 값이 엮이도록 한다.

```python
# Runtime: 56 ms, Memory Usage: 14.4 MB
def solution3(l1, l2):

    if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
            
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
        
    return l1
```