> 두 트리를 받아서 합친다. 만약 양쪽에 노드가 있다면, 값을 더하고 한쪽에만 노드가 있다면 해당 노드로 합쳐진다.

# 문제 풀이

비교적 어렵지 않게 풀었다. 처음에는 양쪽의 노드를 함께 순회하면서 root1에 root2의 값을 더하는 방법으로 할까 하다가 그렇게 하면 null 노드에 대한 처리가 어려워 질 것 같아서 그냥 새롭게 노드를 생성하면서 나아가게 만들었다.

```python
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def dfs(node1, node2):
            if node1 and node2:
                return TreeNode(node1.val+node2.val, dfs(node1.left, node2.left), dfs(node1.right, node2.right))
            if node1 or node2:
                return TreeNode(node1.val if node1 else node2.val,
                                dfs(node1.left if node1 else None, node2.left if node2 else None),
                                dfs(node1.right if node1 else None, node2.right if node2 else None))
            return None

        return dfs(root1, root2)
```

교재를 보니 훨씬 간결하게 풀이했다.

```python
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node
        else:
            return root1 or root2
```

생각 해 보니 양쪽중에 하나만 있다면.. 그 하나를 달아주면 되는 것이다..! 한쪽 노드에만 있다면 없는 쪽의 자식노드까지 비교할 일은 절대 없으니까.. 정말 조금만 생각하면 할 수 있는 최적화였다. 이럴수가.
