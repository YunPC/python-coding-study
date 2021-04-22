## 풀이

## 232_Implement_Queue_Using_Stacks(p. 257, [링크](https://leetcode.com/problems/implement-queue-using-stacks/)) - 허재혁

> 스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
> - push(x): 요소 x를 큐 마지막에 삽입한다.
> - pop(): 큐 처음에 있는 요소를 제거한다.
> - peek(): 큐 처음에 있는 요소를 조회한다.
> - empty(): 큐가 비어 있는지 여부를 리턴한다.

### 나의 풀이
```python
class MyQueue:

    def __init__(self):
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.peek():
            return self.stack1.pop(0)
        return None

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[0]
        return None

    def empty(self) -> bool:
        return len(self.stack1) == 0
```
- 파이썬 리스트 자료구조에서 문제의 기능을 제공하고 있으므로 기본 리스트를 이용하여 구현하였다.
- *결과*: Runtime 36 ms / Memory 14.2 MB

## 스택 2개를 사용한 풀이
```python
class MyQueue2:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if self.peek():
            return self.output.pop()
        return None

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0
```
- 파이썬 리스트를 입력을 받는 리스트, 출력하는 리스트 두 개를 선언하여 구현하였다.
- push()의 경우, input 리스트에 추가한다.
- peek()의 경우, 출력하는 리스트(output 리스트)가 비어있을 경우, input 리스트에 있는 입력받은 값들을 output 리스트로 옮겨주고 마지막 요소를 반환한다.
- pop()은 peek()이 반환하는 True는 output 큐가 비어있지 않았음을 의미하므로 output에서 pop()한다.
- empty()의 경우, input 리스트와 output 리스트 모두가 비어있는지 확인하여 그 결과를 반환한다.
- *결과*: Runtime 32 ms / Memory 14.2 MB

## 결론 및 의문점
- 두번째 풀이가 4 ms가 빠르지만 굳이 이렇게까지 하여 구현할 필요가 있는지 궁금하다.
- 스택을 이용하여 큐를 구현해볼 수 있다는 점이 흥미로웠다. 큐와 스택은 전혀 다른 개념인 듯 하지만 긴밀히 연관된 개념임을 알 수 있었다.