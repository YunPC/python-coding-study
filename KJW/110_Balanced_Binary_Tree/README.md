> 양 쪽의 노드의 깊이를 비교해서 깊이가 2이상 차이나면 false 모든 노드의 깊이가 2이상 차이나지 않으면 true를 반환하면 된다.

# 문제 풀이

처음에 접근은 루트에서 양쪽의 노드의 깊이를 가져와서 그 차이를 비교해서 2보다 작으면 true 아니면 false를 리턴할 생각이었으나, 루트 노드에서만 비교하면 의미가 없었다.

모든 노드에서 양쪽 자식노드의 깊이를 비교해 한 번이라도 2이상 차이가 나면 바로 False를 리턴해야 한다. 단 빈 노드의 경우 true이므로 마지막 리턴할 때 조건을 추가해야 한다.

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left is False or right is False:
                return False
            if abs(left - right) > 1:
                return False
            return max(left, right) + 1
        result = dfs(root)
        if result is not False and 0 <= result:
            return True
        return False
```

교재의 방법은 내 코드보다 간결하지만 원리는 비슷하다.
