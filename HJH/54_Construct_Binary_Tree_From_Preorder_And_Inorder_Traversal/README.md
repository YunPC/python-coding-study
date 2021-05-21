## 풀이

### 54_Construct_Binary_Tree_From_Preorder_And_Inorder_Traversal - 허재혁

> [https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

> 트리의 전위, 중위 순회 결과를 입력값으로 받아 이진 트리를 구축하라.

**나의 풀이**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            idx = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx + 1:])

            return node
```
- 분할정복 문제다.
- preorder에서 pop(0)은 subtree의 root이다.
- preorder의 pop(0)을 기준으로 왼쪽의 요소들은 왼쪽 자식들, 오른쪽 요소들은 오른쪽 자식들이다.
- 이를 재귀적으로 구현해준다.
