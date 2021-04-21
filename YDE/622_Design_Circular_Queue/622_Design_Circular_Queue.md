# 문제 정의

원형 큐를 디자인하는 문제이다.

## 풀이

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