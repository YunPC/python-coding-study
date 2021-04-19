## 225. Implement Stack using Queues

큐를 이용해서 스택을 만드는 기능을 구현해야 하는데, 문제에서는 언어별로 구현되어있는 Queue 자료구조를 활용하라고 한다. 파이썬에서는 deque로 구현을 하면 되는건가 싶어서 아래와 같이 코드를 만들었다

```python
from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)


    def pop(self) -> int:
        return self.queue.pop()


    def top(self) -> int:
        return self.queue[-1]


    def empty(self) -> bool:
        return len(self.queue) < 1
```

어.. 뭔가 너무 간단하긴 하지만 일단 파이썬에서는 이렇게 하게 된다. 테스트도 통과는 된다.
