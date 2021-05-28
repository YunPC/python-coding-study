# 풀이

## [208_Implement-Trie(Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) - 허재혁

### naive

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()


class Trie:

    def __init__(self):
        self.head = Node(None)


    def insert(self, word: str) -> None:
        curr = self.head

        for c in word:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]

        curr.child['*'] = True


    def search(self, word: str) -> bool:
        curr = self.head

        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]

        return '*' in curr.child


    def startsWith(self, prefix: str) -> bool:
        curr = self.head

        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]

        return True
```

- 수업 중에 배웠던 트라이를 구현하여 풀 수 있다. 맨 처음에는 Node class를 구현해주어 풀었다.
- 마지막 임을 나타내는 anchor `'*'`를 이용하여야 search 메서드를 구현할 수 있다.
- Runtime 224ms / Memory 32.4MB

### 개선된 풀이

```python
class Trie:

    def __init__(self):
        self.trie = {}


    def insert(self, word: str) -> None:
        curr = self.trie

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

        curr['*'] = True


    def search(self, word: str) -> bool:
        curr = self.trie

        for c in word:
            if c not in curr:
                return False
            curr = curr[c]

        return '*' in curr


    def startsWith(self, prefix: str) -> bool:
        curr = self.trie

        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]

        return True
```

- 풀이 로직은 위와 동일하나 차이가 있다면 class를 이용하지 않고 일반 dictionary를 이용하여 구현했다는 점에 있다.
- Runtime 124ms / 27.8MB
- Runtime이 반으로 줄었다... 이를 통해 객체를 생성하고 접근하는 데에 로드가 많이 든다는 사실을 알 수 있다.
- 시간제한이 빡빡하다면 class를 통한 객체의 생성 방법을 dictionary로 구현해보는 것이 가독성 측면에서 떨어질 수 있으나 효과적이다.
