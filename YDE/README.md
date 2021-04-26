# 파이썬 알고리즘 인터뷰

## 리트코드 문제 풀이 폴더

### 2021.04.21(Linked List, Queue)



### 문제 정의

정렬되어 있는 두 연결리스트를 합치는 문제이다.


#### 풀이1

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

#### 풀이2

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

#### 풀이3

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

### 문제 정의

연결 리스트를 뒤집는 문제이다.

#### 풀이1

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

#### 풀이2

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

### 문제 정의

원형 큐를 디자인하는 문제이다.

#### 풀이

코드는 아래와 같다.

```python
# Runtime: 64 ms Memory Usage: 15 MB
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.full = False
        self.front = 0
        self.rear = 0
    
    def enQueue(self, value: int) -> bool:
        if self.front == self.rear and self.full:
            return False
        
        self.q[self.rear] = value
        self.rear = (self.rear+1) % len(self.q)
        
        if self.rear == self.front:
            self.full = True
            
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        value = self.q[self.front]
        self.front = (self.front+1) % len(self.q)
        
        self.full = False
        
        return True
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.q[(self.rear-1)%len(self.q)]

    def isEmpty(self) -> bool:
        return self.front == self.rear and not self.full

    def isFull(self) -> bool:
        return self.full
```

초기값으로는 큐의 `front`와 `rear`그리고 리스트 `q`를 선언하였다. 그리고 큐가 비어있는지 가득차있는지 쉽게 알기 위해 `full`변수를 추가하였다.

`full`변수를 사용하면 `front`와 `rear`가 같은 곳을 가리킬 때, 이것이 비어있는 것인지 아닌지 알 수 있다.

`enQueue`함수에선 `rear`에 값을 추가하고 1을 증가하였다. 여기서는 원형큐이기 때문에 나머지 연산을 해주어야 한다. 만약 값을 넣고 난 뒤, `front`와 `rear`가 만났다면, 이 큐는 가득찬 것이므로 `full`을 `True`로 지정한다.

`deQueue`함수의 경우 `front`에 `enQueue`의 `rear`에 했던 것과 동일한 연산을 한다. 여기서는 큐가 꽉찰 수가 없으므로 무조건 `full`변수를 `False`로 한다.

`isEmpty`함수의 경우 `front`와 `rear`값이 같으면서 `full`값이 `False`이면 큐가 비어있는 것이다.