> 다은님의 이상한 취미..

# 문제 풀이

노드를 생성하고 노드를 생성하는 함수를 반복 호출한다. 노드의 값으로는 생성되는 시점과 늦게 분열하는 아메바인지 체크하는 불리언을 갖는다.

```python
class Node():
    def __init__(self, time, is_slow) -> None:
        self.time = time
        self.is_slow = is_slow
        self.left = None
        self.right = None

def solution(N):
    root = Node(0, False)

    def count_node(node):
        if node.time > N:
            return 0

        add_time = node.time+(2 if node.is_slow else 1)
        node.left = Node(add_time, False)
        node.right = Node(add_time, True)

        return count_node(node.left) + count_node(node.right) + 1

    return count_node(root)
```
