# Tree

## 1. 104. Maximum Depth of Binary Tree

### 문제 설명

- 이진 트리의 최대 깊이를 찾는 문제.

### 코드

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        answer = -1

        def recur(node, depth):
            nonlocal answer

            if node is None:
                answer = max(answer, depth)
                return

            recur(node.left, depth + 1)
            recur(node.right, depth + 1)

        recur(root, 0)

        return answer

```

### 풀이

#### 1. 개수로 계산하기

- Input 이 배열 형태로 들어온다면, 배열의 개수를 통해 깊이를 알 수 있다. 1,3,7,15,31 순으로 증가하므로 공차가 2n 인 등차수열로 볼 수 있다. 이를 통해 계산하면 1일때 깊이 1, 3까지 깊이 2, 7까지 깊이 3을 계산하면 깊이 구하기가 가능하다.
- 입력 형식이 배열이 아니기 때문에 불가능한 풀이였다.

#### 2. 순회하기

- 재귀 형식으로 순회하면서 최대 깊이를 찾는다. 이 때 인자에 depth 를 넣어주었는데 만약 기존에 선언한 배열에 값을 더하는 방식을 사용하면 계속해서 depth 가 변경되기 때문에 파라미터에서 +1을 한 값을 넘겨주는것이 좋다.