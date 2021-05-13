> 값이 같은 노드를 잇는 가장 경로의 길이중 가장 긴 길이를 구하라

# 문제 풀이

세번의 풀이를 했으나 모두 실패했다..
첫 번째 시도는 문제를 잘못 파악해 접근부터 완전히 틀려먹었다.

긴 경로가 아니라 값이 같은 노드의 모든 간선을 계산해 버린 것

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def longestUnivaluePath(self, root: TreeNode) -> int:
        result = []
        def dfs(prev_val, idx, node):
            if node is None:
                return False
            if prev_val == node.val:
                result[idx] += 1
                dfs(node.val, idx, node.left)
                dfs(node.val, idx, node.right)
            else:
                result.append(0)
                dfs(node.val, len(result)-1, node.left)
                dfs(node.val, len(result)-1, node.right)
        dfs(None, 0, root)
        return max(result) if result else 0
```

다시 문제를 파악해서 시도해 봤지만 역시 풀리지 않았다.

```python
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        result = 0

        def recursive(node, path):
            nonlocal result
            if node is None:
                return path
            if node.left and node.right:
                if node.val == node.left.val == node.right.val:
                    if path == 0:
                        left = recursive(node.left, path+1)
                        right = recursive(node.right, path+1)
                        result = max(result, left + right)
                        return result
                    return max(recursive(node.left, path+1), recursive(node.right, path+1))
                if node.val == node.left.val:
                    return max(recursive(node.left, path+1), recursive(node.right, 0))
                if node.val == node.right.val:
                    return max(recursive(node.right, path+1), recursive(node.left, 0))
            if node.left:
                if node.val == node.left.val:
                    return max(recursive(node.left, path+1), recursive(node.left, 0))
                return recursive(node.left, 0)
            if node.right:
                if node.val == node.right.val:
                    return max(recursive(node.right, path+1), recursive(node.right, 0))
            return path

        result = recursive(root, 0)
        return result
```

코드를 쓰다보니 내가 코드를 너무 어거지로 쓰고있다는 걸 느껴서 처음부터 다시 짰다.

```python
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0

        def recursive(node, path):
            if node is None:
                return path
            if node.left and node.left.val == node.val:
                left_max = recursive(node.left, path+1)
            elif node.left:
                left_max = 0
                recursive(node.left, 0)

            if node.right and node.right.val == node.val:
                right_max = recursive(node.right, path+1)
            elif node.right:
                right_max = 0
                recursive(node.right, 0)

            self.result = max(self.result, (left_max + right_max))
            return max(left_max, right_max)
        recursive(root, 0)
        return self.result
```

나중에 정답을 보고나니 꽤나 근접했지만 역시 핵심적인 로직을 구현하지 못했다. 교재에 있는 정답은 아래와 같다

```python
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)
            return max(left, right)
        dfs(root)
        return self.result
```

처음 봤을때는 너무 간단해서 어이가 없었다. 하나씩 이해해 보자

```python
if node is None:
    return 0
```

재귀함수의 탈출 조건이다. 접근한 노드가 존재하지 않는다면 0을 리턴한다.

```python
left = dfs(node.left)
right = dfs(node.right)
```

그렇게 되면 잎새노드에서 left와 right는 0으로 초기화된다. 자식이 있다면, 아래 로직에 따라 알맞는 값으로 초기화 된다.

```python
if node.left and node.left.val == node.val:
    left += 1
else:
    left = 0
if node.right and node.right.val == node.val:
    right += 1
else:
    right = 0
```

잎새노드에서는 모든 조건에서 else문으로 가서 다시 0으로 할당된다 하지만 자식이 있는 노드라면, 자식과 자신의 값을 비교하여 값이 같다면 1씩 더해줄 수 있다.

```python
self.result = max(self.result, left + right)
return max(left, right)
```

중요한 부분이다. 만약 잎새노드가 아니라면 그 노드를 기준으로 이어진 노드들의 길이로 최대길이를 갱신한다 그리고 자식 노드의 길이중 긴 쪽으로 선택하여 반환하여 부모노드에 거리를 더해 줄 수 있다.

최대값을 찾아주기만 하면 되기때문에 max함수를 사용해 매 연산마다 큰 값을 더해주기만 하면 된다. 그리고 매 연산마다 해당 노드를 기준으로 이어진 길이를 최대값으로 갱신해 주면 결국 가장 긴 경로를 구할 수 있다.

DFS순회를 통해 탑다운 방식으로 풀이할 수 있었다. 교재에서는 백트래킹을 사용했다고 하는데 어느 부분이 백트래킹인지 이해가 잘 되지 않는다..

이 문제에 몇 시간을 꼴아박으면서 내가 아직도 재귀에 얼마나 약한지 알았다.. 별 한개 짜리 문제임에도 결국 포기한 게 너무 분했다.. 재귀 관련 문제를 많이 풀어봐야 할 것 같다.
